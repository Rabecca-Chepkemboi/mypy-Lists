# 1. Write a Python program to find the second largest number in a list.

list_int = [23, 6, 45, 89, 22, 34]
list_int.sort()                             #sort the number to be in ascending order
print(list_int[-2])    
                     #print the second largest(-2)

# 2. Write a Python program to find the sum of all the elements in a list.

list = [4, 9, 6, 2, 5]
print(list)
print(sum(list))


# 3. Write a Python program to reverse a list.

names = ["Clarah", "Ambrose", "Vince", "Dinah"]
print(names)
names.reverse()
print(names)


# 4. Write a Python program to sort a list in descending order.

numbers = [23, 56, 12, 32, 14, 45]  
numbers.sort()
print(numbers)

# 5. Write a Python program to find the average of a list.

def average(nums):
    sum = 0
    for x in nums:
        sum = sum + x
    avg = sum / len(nums)
    return avg
print(average[23, 12, 32, 22]) 



#                           some of the takeaway keys include
# 1. Accessing list elements: You can access individual elements in a list using their index. For example, if my_list is a list, my_list[0] returns the first element in the list.

# 2. Modifying list elements: You can modify individual elements in a list by assigning a new value to their index. For example, my_list[0] = 'new value' will change the first element in the list to 'new value'.

# 3. Appending to a list: You can add new elements to a list using the append() method. For example, my_list.append('new element') adds the string 'new element' to the end of the list.
