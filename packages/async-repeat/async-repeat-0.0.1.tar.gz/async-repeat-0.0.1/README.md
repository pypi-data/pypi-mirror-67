#AsyncRepeat
A simple decorator for repeating async functions. The main idea is that a coroutine can only be awaited for one time. In
some special case that an async function needs to be run for multiple times, use this tool for an easy approach

## Get started
First install it with pip:
```bash
pip install async-repeat
```
Then in your program:
```python
import asyncio
from async_repeat import repeat

@repeat(3)
async def foo():
    print("foo")

asyncio.run(foo())
```
The result will be:
```bash
foo
foo
foo
```

The repeat decorator has two modes:

- Concurrent: The function will create tasks and run the tasks at the same time
- Synchronous: The coroutines will run one by one