# 0x02-python_async_comprehension

Asynchronous comprehensions are only allowed inside an async def function.

In principle, asynchronous generator expressions are allowed in any context.
However, in Python 3.6, due to async and await soft-keyword status,
asynchronous generator expressions are only allowed in an async def function.
Once async and await become reserved keywords in Python 3.7, this restriction will be removed.

Examples:

- set comprehension: {i async for i in agen()};
- list comprehension: [i async for i in agen()];
- dict comprehension: {i: i ** 2 async for i in agen()};
- generator expression: (i ** 2 async for i in agen())
