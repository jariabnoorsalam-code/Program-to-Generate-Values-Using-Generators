
# Program to Generate Values Using Generators

## Objective
To learn how to generate values using Python Generators and the yield keyword.

## Description
This program uses a generator function to generate values one by one.

## Source Code
```python
def generate_values():
    for i in range(1, 6):
        yield i

result = generate_values()

print("Generated Values:")

for value in result:
    print(value)
```

## Output
Generated Values:
1
2
3
4
5

## Language
Python

## Author
Jariab Noor Salam
