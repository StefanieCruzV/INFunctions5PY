# 1Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
from hmac import new


def countDown(a):
    for x in range(a, 0, -1):
        print(x)


count_down = countDown(5)
print("-----------------------------------------------1")
# 2Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2


def returnCreate(list):
    print(list[0])
    return list[1]


print(returnCreate([1, 2]))
print("-----------------------------------------------2")
# 3First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)


def plusLength(list):
    sum = list[0] + len(list)
    return sum


print(plusLength([1, 2, 3, 4, 5]))
print("-----------------------------------------------3")
# 4Values Greater than Second - Write a function that accepts a list and creates a new list
# containing only the values from the original list that are greater than its 2nd value.
#  Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False


def greaterthanSecond(list):
    if len(list) < 2:
        return False
    newList = []
    for i in list:
        if i > list[1]:
            newList.append(i)
            # print(newList)
    print(f" the values are: {len(newList)}")
    return newList


# print(greaterthanSecond([5, 2, 3, 2, 1, 4]))
print(greaterthanSecond([3]))

print("-----------------------------------------------4")
# 5This Length, That Value - Write a function that accepts two integers as parameters: size and value.
#  The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def lenthatValue (size,value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList

print(lenthatValue(4,7))
print(lenthatValue(6,2))

print("-----------------------------------------------5")
