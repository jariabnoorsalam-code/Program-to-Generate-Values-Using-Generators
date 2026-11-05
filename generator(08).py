# Program to Generate Values Using Generators
def generate_values():
    for i in range(1, 6):
        yield i
result = generate_values()
print("Generated Values:")
for value in result:
    print(value)
