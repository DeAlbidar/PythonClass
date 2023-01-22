# List
# Write a program to find the largest number in a list.
#

def largest_num():
    numbers = [4, 7, 5, 21, 3, 14, 20, 8, 10]
    max_number = 0
    for i in numbers:
        if i > max_number:
            max_number = i
    print(max_number)


# List Methods
# Write a program to remove the duplicates in a list
def rem_duplicates_num():
    numbers = [4, 7, 5, 21, 5, 3, 14, 4, 8, 10]
    num_lists = []
    for i in numbers:
        if i not in num_lists:
            num_lists.append(i)
    print(num_lists)
