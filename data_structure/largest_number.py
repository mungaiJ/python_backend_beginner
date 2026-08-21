numbers = [12, 45, 7, 89, 23]

def find_largest(numbers):
    largest = numbers[0]
    if numbers[1] > largest:
        largest = numbers[1]
    if numbers[2] > largest:
        largest = numbers[2]
    if numbers[3] > largest:
        largest = numbers[3]
    if numbers[4] > largest:
        largest = numbers[4]

    return largest
result = find_largest(numbers)
print(result)
