def find_max(numbers:list):
    """Return the maximum number from a list of numbers."""
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
numbers = [3, 5, 2, 8, 1]
if len(numbers) == 0:
    print("The list is empty.")
else:
    max_number = find_max(numbers)
    print("Maximum number:", max_number)    