def greet(name):
      print('Здравствуйте, меня зовут', name)

greet('Dasha')
####################################
def square(number):
    return number**2

print(square(3))
###########################
def max_of_two(x, y):
    if x>y:
        return x
    else:
        return y

print(max_of_two(4,10))
###############################

def describe_person(name, age = 30):
    print('Имя человека: ', name,',возраст: ', age)

describe_person('Dasha')

####################
def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True and x > 1

print(is_prime())