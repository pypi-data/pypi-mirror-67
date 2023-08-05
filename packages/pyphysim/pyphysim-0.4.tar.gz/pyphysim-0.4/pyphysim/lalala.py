from typing import TypeVar, Any
import numpy as np
import pandas as pd

Array = TypeVar("Array")

X = TypeVar("X", int, float, str, complex, np.ndarray)


def identity(x: X) -> X:
    return x


# if __name__ == '__main__':
y = identity(5)
z = identity(5.5)
x = identity(np.array([1, 2, 3, 4]))

data = data = {"a": [1, 2, 3, 4], "b": [10, 11, 12, 13]}
df = pd.DataFrame(data=data)
a = identity(data)
b = identity(df)
# reveal_type(y)
# reveal_type(z)
# reveal_type(x)
# reveal_type(x.shape)
# reveal_type(a)

# Question in stackoverflow
# tags: [python] [mypy] [typing] [type-hinting]
