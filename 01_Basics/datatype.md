# Data Types in Python

Python has several built-in data types that can be categorized as follows:

## 1. Numeric Types
- **int**: Integer numbers (e.g., `10`, `-5`)
- **float**: Floating-point numbers (e.g., `3.14`, `-0.001`)
- **complex**: Complex numbers (e.g., `2+3j`)

## 2. Sequence Types
- **str**: Strings (e.g., `'hello'`, `"world"`)
- **list**: Ordered, mutable collection (e.g., `[1, 2, 3]`)
- **tuple**: Ordered, immutable collection (e.g., `(1, 2, 3)`)

## 3. Set Types
- **set**: Unordered, unique collection (e.g., `{1, 2, 3}`)
- **frozenset**: Immutable set (e.g., `frozenset({1, 2, 3})`)

## 4. Mapping Type
- **dict**: Key-value pairs (e.g., `{"name": "John", "age": 25}`)

## 5. Boolean Type
- **bool**: Represents `True` or `False`

## 6. Binary Types
- **bytes**: Immutable byte sequence (e.g., `b'hello'`)
- **bytearray**: Mutable byte sequence (e.g., `bytearray([65, 66, 67])`)
- **memoryview**: Memory view object (e.g., `memoryview(bytes(5))`)

## Type Checking and Conversion
- Use `type(variable)` to check a variable's type.
- Convert types using functions like `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, `dict()`, `bool()`, etc.