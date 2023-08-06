# Simple PYthon Dependepncy Injection Library (SPYDI)
## What the hell is it?
A dependency injection library which is intended to utilize python's type annotations to build the dependency tree.
No attempt has been made to optimize it since the only intended usage is right on app start so a slight slowness is acceptable in the majority of cases.

## Motivation
A brief research has shown there is no such library in the whole internet. Other solutions either:
 * Rely on manual binding-by-name;
 * Requires deep integration into a source code;
 * Do not play well with python async features and context-managed dependencies;
 * Do not work with my beloved `typing.NamedTuple`;
 * Doesn't work at all;

## How to use it
SPYDI does not require a deep integration into your application. Just design your app following the SOLID principles and SPYDI will handle the binding for you.
A brief example could be found here (or refer to tests)
```python
import typing

from spydi.context import DependencyContext
from spydi.factory import DependencyFactory


class Foo(typing.NamedTuple):
    a: int
    b: int
    c: str


def try_create_me(foo: Foo, bar):
    return foo.c + bar


ctx = DependencyContext()
ctx.bind(2, to='a')
ctx.bind(3, to='b')
ctx.bind('qwe', to='c')
ctx.bind('rty', to='bar')

factory = DependencyFactory(ctx)
result = factory.create(try_create_me)
assert result == 'qwerty'
```

## Licensing
This project is licensed under Apache 2.0 License