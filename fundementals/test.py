#from fundementals.calculator.cal_method import div

#print(div(50, 2))

import array as arr

# Write a Python program to convert an array to an ordinary list with the same items
def array_to_list():
    array = arr.array('i', [1, 2, 3, 4, 5])
    print('Given array:', array)
    print('Converting an array to list by tolist():', array.tolist())
    print('Converting an array to list by list():', list(array))

# Write a Python program to remove a specified item using the index from an array.
def remove_element():
    array = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
    num_list = array.tolist()
    n = int(input("Enter index value:"))
    if n > len(num_list):
        print("index out of range! Please,enter index between 0 and", len(num_list))
    else:
        for i in num_list:
            if num_list[n] == i:
                del num_list[n]
        print(num_list)

# Pattern program
def pattern():
    row = int(input("Enter number of rows you want:"))
    for i in range(row + 1):
        for j in range(i):
            print("* ", end='')
        print('\n')

# Triangle Pattern Program
def triangle():
    row = int(input("Enter number of rows you want:"))
    k = row - 1
    for i in range(row):
        for j in range(k):
            print(end=' ')
        k = k - 1
        for j in range(i+1):
            print('* ', end='')
        print('\n')



