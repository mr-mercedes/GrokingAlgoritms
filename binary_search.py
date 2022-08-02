def binary_search(array, item):
    low_number = 0
    high_number = len(array) - 1

    while low_number <= high_number:
        mid_number = (low_number + high_number) // 2
        guess = array[mid_number]
        if guess == item:
            return mid_number
        elif guess > item:
            high_number = mid_number - 1
        else:
            low_number = mid_number + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, int(input('Введите число для поиска: '))))
