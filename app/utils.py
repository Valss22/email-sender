import asyncio


def nonblock(task, *args, **kwargs):
    loop = asyncio.get_event_loop()
    loop.create_task(task(*args, **kwargs))
