# this function is going to take a first name and a last name and going to change it to titlecase

# 1
# def format_name(f_name, l_name):
#     first = f_name.capitalize()
#     second = l_name.capitalize()
#     print(first, second)
#
#
# name = input("What is your first name? ").lower()
# surname = input("What is your last name? ").lower()
#
# format_name(name, surname)

# 2
# def format_name(f_name, l_name):
#     name = (f_name + " " + l_name).title()
#     print(name)
#
#
# first_name = input("What is your first name? ")
# surname = input("What is your last name? ")
#
# format_name(f_name=first_name, l_name=surname)

# 3
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


first_name = input("What is your first name? ")
surname = input("What is your last name? ")

#  the call function becomes the output and can save in a variable for use
print(format_name(first_name, surname))


# the difference between a print statement and return
def function_1(text):
    return text + text


def function_2(text):
    return text.title()


'''
function 1 has an input "hello" and return changes the call to a value which is used in function 2 as input 
its then returned and the whole line becomes the value
'''
output = function_2(function_1("hello"))
print(output)
