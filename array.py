# python uses lists to simulate arrays
# pure arrays doesn't exist in python
# but we can use third party libraries like numpy
# to get real arrays

array = list([1, 2, 3, 4])

if __name__ == '__main__':
    print(array)
    print(array[2])  # prints 3

    size = len(array)
    print(size)

    print('---for 1---')
    for index in range(size):
        print(array[index])

    print('---for 2---')
    for item in array:
        print(item)
