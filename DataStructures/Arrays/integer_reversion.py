# design an efficient algorithm to reverse a given integer.
# For example if the input of the algorithm is 1234 then the output should be 4321.


def reversed_int(n):


    reversed_integer = 0
    while n > 0:
        remainder = n%10
        n = n//10  #integer division
        reversed_integer = reversed_integer*10 +remainder

    return reversed_integer

print(reversed_int(1234897))
