# imports to use to reset the console once
# Tests and experiments
import sys
import subprocess
import os


# TERM environment variable not set
#  Linux related issue occurring
def clear_screen():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)


def clear_screen_2():
    operating_system = sys.platform
    if operating_system == "linux":
        subprocess.run("clear", shell=True)
        # os.getenv('TERM', None)
        os.system("clear")


def clear_screen_3():
    """Clear the terminal screen"""
    # 'posix' = linux and Mac 'nt' = Windows
    term = os.getenv('TERM', None)
    if term:
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")


# print(sys.platform)
# print(os.name)

print("Beginning")
input("Enter ")

# TERM environment variable not set
clear_screen()
print("Refresh")
