# "A palindrome is a string that reads the same forward and backward"
#
# For example: radar or madam
#
# Our task is to design an optimal algorithm for checking whether a given string is palindrome or not!
def is_palindrome(s):

    orginal_string = s
    reversed_string = reverse(s)

    if orginal_string == reversed_string:
        return  True
    return  False

def reverse(data):

    # string in to list
    data = list(data)


    start_index = 0
    end_index = len(data)-1

    while end_index > start_index:
        data[end_index],data[start_index] = data[start_index],data[end_index]
        start_index = start_index + 1
        end_index = end_index - 1
    #trabform letter to string
    return ''.join(data)

print(is_palindrome('car'))
print(is_palindrome("madam"))


######python way ####################
def palindrome_pythom(s):
    #checking whether palidrome or not
    if s == s[::-1]:
        return True
    return False

print(palindrome_pythom('car'))
print(palindrome_pythom("tat"))