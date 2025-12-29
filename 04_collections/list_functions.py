numbers = [4, 8, 15, 16, 23, 42]

numbers.append(99)
print(numbers)

numbers.insert(1, 100)
print(numbers)

numbers.remove(15)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(16))
print(numbers.count(8))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
