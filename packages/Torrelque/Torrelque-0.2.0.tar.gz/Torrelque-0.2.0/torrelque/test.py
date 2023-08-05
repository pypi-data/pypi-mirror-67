import time
import asyncio

import aredis
import asynctest

from . import Torrelque


class TestTorrelque(asynctest.TestCase):

    redis = None
    testee = None

    async def setUp(self):
        super().setUp()

        self.redis = aredis.StrictRedis(db=1, decode_responses=True)
        self.testee = Torrelque(self.redis)

        await self.redis.flushdb()

    def test_instantiation_error(self):
        with self.assertRaises(ValueError) as ctx:
            Torrelque(object())
        self.assertEqual('aredis.StrictRedis instance expected', str(ctx.exception))

        with self.assertRaises(ValueError) as ctx:
            Torrelque(aredis.StrictRedis(db=1, decode_responses=False))
        self.assertEqual(
            'aredis.StrictRedis is expected with decode_responses=True', str(ctx.exception)
        )

    async def _get_state(self):
        pending = await self.redis.lrange(self.testee.keys['pending'], 0, -1)
        working = await self.redis.zrange(self.testee.keys['working'], 0, -1, withscores=True)
        delayed = await self.redis.zrange(self.testee.keys['delayed'], 0, -1, withscores=True)
        tasks = await self.redis.hgetall(self.testee.keys['tasks'])
        return pending, working, delayed, tasks

    async def test_enqueue(self):
        now = time.time()

        task_id1 = await self.testee.enqueue({'foo': 123}, task_timeout=5)
        task_id2 = await self.testee.enqueue({'bar': [1, 2, 3]})

        uuid, timeout = task_id1.split('-')
        self.assertEqual(32, len(uuid))
        self.assertEqual('5', timeout)

        uuid, timeout = task_id2.split('-')
        self.assertEqual(32, len(uuid))
        self.assertEqual('120', timeout)

        actual = await self.testee.get_stats()
        self.assertEqual({'working': 0, 'pending': 2, 'delayed': 0, 'tasks': 2}, actual)

        actual = await self.testee.get_task_stats(task_id1)
        self.assertAlmostEqual(now, actual.pop('enqueue_time'), delta=0.1)
        self.assertEqual({
            'last_requeue_time': None,
            'last_dequeue_time': None,
            'requeue_count': 0,
            'dequeue_count': 0
        }, actual)

        pending, working, delayed, tasks = await self._get_state()
        self.assertEqual([task_id2, task_id1], pending)
        self.assertEqual([], working)
        self.assertEqual([], delayed)
        self.assertEqual({
            task_id1: '{"foo": 123}',
            task_id2: '{"bar": [1, 2, 3]}'
        }, tasks)

    async def test_dequeue(self):
        now = time.time()

        task_id1 = await self.testee.enqueue({'foo': 123}, task_timeout=5)
        task_id2 = await self.testee.enqueue({'bar': [1, 2, 3]})

        task_id, task_data = await self.testee.dequeue()
        self.assertEqual(task_id1, task_id)
        self.assertEqual({'foo': 123}, task_data)

        actual = await self.testee.get_stats()
        self.assertEqual({'working': 1, 'pending': 1, 'delayed': 0, 'tasks': 2}, actual)

        actual = await self.testee.get_task_stats(task_id1)
        self.assertAlmostEqual(now, actual.pop('enqueue_time'), delta=0.1)
        self.assertAlmostEqual(now, actual.pop('last_dequeue_time'), delta=0.2)
        self.assertEqual({
            'last_requeue_time': None,
            'requeue_count': 0,
            'dequeue_count': 1
        }, actual)

        pending, working, delayed, tasks = await self._get_state()
        self.assertEqual([task_id2], pending)


        self.assertEqual(1, len(working))
        self.assertEqual(task_id1, working[0][0])
        self.assertAlmostEqual(now + 5, working[0][1], delta=0.2)

        self.assertEqual([], delayed)
        self.assertEqual({
            task_id1: '{"foo": 123}',
            task_id2: '{"bar": [1, 2, 3]}'
        }, tasks)


        task_id, task_data = await self.testee.dequeue()
        self.assertEqual(task_id2, task_id)
        self.assertEqual({'bar': [1, 2, 3]}, task_data)

        actual = await self.testee.get_stats()
        self.assertEqual({'working': 2, 'pending': 0, 'delayed': 0, 'tasks': 2}, actual)

        actual = await self.testee.get_task_stats(task_id1)
        self.assertAlmostEqual(now, actual.pop('enqueue_time'), delta=0.1)
        self.assertAlmostEqual(now, actual.pop('last_dequeue_time'), delta=0.2)
        self.assertEqual({
            'last_requeue_time': None,
            'requeue_count': 0,
            'dequeue_count': 1
        }, actual)

        pending, working, delayed, tasks = await self._get_state()
        self.assertEqual([], pending)

        self.assertEqual(2, len(working))
        self.assertEqual(task_id1, working[0][0])
        self.assertAlmostEqual(now + 5, working[0][1], delta=0.2)
        self.assertEqual(task_id2, working[1][0])
        self.assertAlmostEqual(now + 120, working[1][1], delta=0.2)

        self.assertEqual([], delayed)
        self.assertEqual({
            task_id1: '{"foo": 123}',
            task_id2: '{"bar": [1, 2, 3]}'
        }, tasks)


        task_id, task_data = await self.testee.dequeue(timeout=1)
        self.assertIsNone(task_id)
        self.assertIsNone(task_data)

    async def test_dequeue_concurrent(self):
        task_id1 = await self.testee.enqueue({'foo': 123}, task_timeout=5)
        task_id2 = await self.testee.enqueue({'bar': [1, 2, 3]})

        actual = set()

        async def create_consumer():
            queue = Torrelque(aredis.StrictRedis(db=1, decode_responses=True))
            while True:
                task_id, _ = await queue.dequeue()
                if task_id is None:
                    break
                actual.add(task_id)
                await queue.release(task_id)

        async def run_consumers():
            await asyncio.gather(*[create_consumer() for _ in range(8)])

        consumer_task = self.loop.create_task(run_consumers())

        while True:
            size = await self.redis.hlen(self.testee.keys['tasks'])
            if not size:
                break
            await asyncio.sleep(0.1)

        self.assertEqual({task_id1, task_id2}, actual)

        consumer_task.cancel()

    async def test_requeue(self):
        now = time.time()

        task_id1 = await self.testee.enqueue({'foo': 123}, task_timeout=5)
        task_id2 = await self.testee.enqueue({'bar': [1, 2, 3]})

        task_id, _ = await self.testee.dequeue()
        await self.testee.requeue(task_id, delay=None)

        actual = await self.testee.get_stats()
        self.assertEqual({'working': 0, 'pending': 2, 'delayed': 0, 'tasks': 2}, actual)

        actual = await self.testee.get_task_stats(task_id1)
        self.assertAlmostEqual(now, actual.pop('enqueue_time'), delta=0.1)
        self.assertAlmostEqual(now, actual.pop('last_dequeue_time'), delta=0.2)
        self.assertAlmostEqual(now, actual.pop('last_requeue_time'), delta=0.2)
        self.assertEqual({
            'requeue_count': 1,
            'dequeue_count': 1
        }, actual)

        pending, working, delayed, tasks = await self._get_state()
        self.assertEqual([task_id1, task_id2], pending)
        self.assertEqual([], working)
        self.assertEqual([], delayed)
        self.assertEqual({
            task_id1: '{"foo": 123}',
            task_id2: '{"bar": [1, 2, 3]}'
        }, tasks)

    async def test_requeue_delayed(self):
        now = time.time()

        task_id1 = await self.testee.enqueue({'foo': 123}, task_timeout=5)
        task_id2 = await self.testee.enqueue({'bar': [1, 2, 3]})

        task_id, _ = await self.testee.dequeue()
        await self.testee.requeue(task_id, delay=3600)

        actual = await self.testee.get_stats()
        self.assertEqual({'working': 0, 'pending': 1, 'delayed': 1, 'tasks': 2}, actual)

        actual = await self.testee.get_task_stats(task_id1)
        self.assertAlmostEqual(now, actual.pop('enqueue_time'), delta=0.1)
        self.assertAlmostEqual(now, actual.pop('last_dequeue_time'), delta=0.2)
        self.assertEqual({
            'last_requeue_time' : None,
            'requeue_count': 0,
            'dequeue_count': 1
        }, actual)

        pending, working, delayed, tasks = await self._get_state()
        self.assertEqual([task_id2], pending)

        self.assertEqual([], working)

        self.assertEqual(1, len(delayed))
        self.assertEqual(task_id1, delayed[0][0])
        self.assertAlmostEqual(now + 3600, delayed[0][1], delta=0.2)

        self.assertEqual({
            task_id1: '{"foo": 123}',
            task_id2: '{"bar": [1, 2, 3]}'
        }, tasks)

    async def test_release(self):
        await self.testee.enqueue({'foo': 123}, task_timeout=5)
        task_id2 = await self.testee.enqueue({'bar': [1, 2, 3]})

        task_id, _ = await self.testee.dequeue()
        await self.testee.release(task_id)

        actual = await self.testee.get_stats()
        self.assertEqual({'working': 0, 'pending': 1, 'delayed': 0, 'tasks': 1}, actual)

        actual = await self.testee.get_task_stats(task_id)
        self.assertIsNone(actual)

        pending, working, delayed, tasks = await self._get_state()
        self.assertEqual([task_id2], pending)
        self.assertEqual([], working)
        self.assertEqual([], delayed)
        self.assertEqual({task_id2: '{"bar": [1, 2, 3]}'}, tasks)

    async def test_sweep(self):
        actual = await self.testee.sweep()
        self.assertEqual(0, actual)

        now = time.time()

        task_id1 = await self.testee.enqueue({'foo': 123}, task_timeout=0.1)
        task_id2 = await self.testee.enqueue({'bar': [1, 2, 3]})

        await self.testee.dequeue()
        await self.testee.dequeue()
        await self.testee.requeue(task_id2, delay=0.25)

        actual = await self.testee.sweep()
        self.assertEqual(0, actual)

        actual = await self.testee.get_stats()
        self.assertEqual({'working': 1, 'pending': 0, 'delayed': 1, 'tasks': 2}, actual)

        for id in (task_id1, task_id2):
            actual = await self.testee.get_task_stats(id)
            self.assertAlmostEqual(now, actual.pop('enqueue_time'), delta=0.1)
            self.assertAlmostEqual(now, actual.pop('last_dequeue_time'), delta=0.1)
            self.assertEqual({
                'last_requeue_time': None,
                'requeue_count': 0,
                'dequeue_count': 1
            }, actual)

        pending, working, delayed, tasks = await self._get_state()
        self.assertEqual([], pending)

        self.assertEqual(1, len(working))
        self.assertEqual(task_id1, working[0][0])
        self.assertAlmostEqual(now + 0.1, working[0][1], delta=0.1)

        self.assertEqual(1, len(delayed))
        self.assertEqual(task_id2, delayed[0][0])
        self.assertAlmostEqual(now + 0.25, delayed[0][1], delta=0.1)

        self.assertEqual({
            task_id1: '{"foo": 123}',
            task_id2: '{"bar": [1, 2, 3]}'
        }, tasks)

        await asyncio.sleep(0.25)

        requeue_time = time.time()
        actual = await self.testee.sweep()
        self.assertEqual(2, actual)

        actual = await self.testee.get_stats()
        self.assertEqual({'working': 0, 'pending': 2, 'delayed': 0, 'tasks': 2}, actual)

        for id in (task_id1, task_id2):
            actual = await self.testee.get_task_stats(id)
            self.assertAlmostEqual(now, actual.pop('enqueue_time'), delta=0.1)
            self.assertAlmostEqual(now, actual.pop('last_dequeue_time'), delta=0.1)
            self.assertAlmostEqual(requeue_time, actual.pop('last_requeue_time'), delta=0.1)
            self.assertEqual({
                'requeue_count': 1,
                'dequeue_count': 1
            }, actual)

        pending, working, delayed, tasks = await self._get_state()
        self.assertEqual([task_id2, task_id1], pending)
        self.assertEqual([], working)
        self.assertEqual([], delayed)
        self.assertEqual({
            task_id1: '{"foo": 123}',
            task_id2: '{"bar": [1, 2, 3]}'
        }, tasks)

    async def test_sweep_schedule(self):
        self.testee = Torrelque(self.redis)
        self.testee.sweep_interval = 0.2

        task_id1 = await self.testee.enqueue({'foo': 123}, task_timeout=0.1)
        task_id2 = await self.testee.enqueue({'bar': [1, 2, 3]})

        await self.testee.dequeue()
        await self.testee.dequeue()
        await self.testee.requeue(task_id2, delay=0.15)

        self.testee.schedule_sweep()

        pending, _, _, _ = await self._get_state()
        self.assertEqual([], pending)

        await asyncio.sleep(0.2)

        pending, _, _, _ = await self._get_state()
        self.assertEqual([task_id2, task_id1], pending)


        await self.testee.dequeue()
        await self.testee.dequeue()
        await self.testee.release(task_id1)
        await self.testee.release(task_id2)

        task_id1 = await self.testee.enqueue({'foo': 123}, task_timeout=0.1)
        task_id2 = await self.testee.enqueue({'bar': [1, 2, 3]})

        await self.testee.dequeue()
        await self.testee.dequeue()
        await self.testee.requeue(task_id2, delay=0.15)

        self.testee.unschedule_sweep()

        pending, _, _, _ = await self._get_state()
        self.assertEqual([], pending)

        await asyncio.sleep(0.2)

        pending, _, _, _ = await self._get_state()
        self.assertEqual([], pending)
