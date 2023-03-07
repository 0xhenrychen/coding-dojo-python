# 1. Update values in Dictionaries and Lists

# x = [ [5,2,3], [10,8,9] ]
# x[1][0] = 15 # 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# print(x)

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# students[0]['last_name'] = 'Bryant' # 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
# print(students[0]['last_name'])

# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0] = 'Andres' # 3. In the sports_directory, change 'Messi' to 'Andres'
# print(sports_directory['soccer'][0])

# z = [ {'x': 10, 'y': 20} ]
# z[0]['y'] = 30 # 4. Change the value 20 in z to 30
# print(z[0]['y'])


#####


# 2. Iterate Through a List of Dictionaries

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(some_list):
#     # for key in some_list:
#     #     print("first_name - " + key["first_name"] + ", last_name - " + key["last_name"])
    
#     for i in range(0, len(some_list)):
#         result = ""
#         for key, value in some_list[i].items():
#             result += f" {key} - {value}"
#         print(result)   

# iterateDictionary(students)


#####


# 3. Get Values From a List of Dictionaries

# def iterateDictionary2(key_name, some_list):
#     for i in range(0, len(some_list)):
#         for key, value in some_list[i].items():
#             if key == key_name:
#                 print(value)
    
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)


#####


# 4. Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, value in some_dict.items():
        print("")
        print(f"{len(value)} {key.upper()}")
        for i in range(0, len(value)):
            print(value[i])
    
printInfo(dojo)