# # 1. Countdown

# def countdown(num):
#     list = []
#     while num >= 0:
#         list.append(num)
#         num = num - 1
#     return list
# print(countdown(5))


# # 2. Print and Return

# def print_and_return(list):
#     print(list[0])
#     return list[1]
# print(print_and_return([1,2]))


# # 3. First Plus Length

# def first_plus_length(list):
#     sum = list[0] + len(list)
#     return sum
# print(first_plus_length([1,2,3,4,5]))


# 4. Values Greater than Second

def values_greater_than_second(list):
    new_list = []
    count = 0
    if len(list) < 2:
        return False
    else:
        for i in range(len(list)):
            if list[i] > list[1]:
                new_list.append(list[i])
                count+=1
        print(count)
        return new_list
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))
            
    
# 5. This Length, That Value

def length_and_value(int1, int2):
    list = []
    for i in range(int1):
        list.append(int2)
    return list
print(length_and_value(4,7))
print(length_and_value(6,2))