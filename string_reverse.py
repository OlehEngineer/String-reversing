# this script can make reversing any strings in few ways
# the main idea is collect few way string reversing methods for python beginners like me:)
# I will really happy if someone add more variants of string reversing
# it is just for fun

# variant #1 using converting string into list, reverse it and that using map for joining list into string back
def reversing_1(my_string):
    new_list=[]
    for each in my_string:
        new_list.append(each)
    new_list.reverse()
    new_string=''.join(map(str,new_list))
    print(new_string)

# variant #2 the shortest way using simple slicing from right side of string
def reversing_2(my_string):
    new_string=my_string[::-1]
    print(new_string)

# variant #3 using "for" loop and right side slicing
def reversing_3(my_string):
    new_string=''
    for i in range(len(my_string),0,-1):
        new_string+=my_string[i-1]
    print(new_string)

# variant #4 using recurtion for string reversing
def reversing_4(my_string):
    if len(my_string)==0:
        return my_string
    else:
        return reversing_4(my_string[1:])+my_string[0]

my_string=input('Please input any string you wish.\n')

# all functions gives the same result
reversing_1(my_string)
reversing_2(my_string)
reversing_3(my_string)
print(reversing_4(my_string))
