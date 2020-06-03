#!/usr/bin/env python3
import string
import random
import argparse

simple_string = string.ascii_letters + string.digits
complex_string = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
parser = argparse.ArgumentParser(description='A basic password generator')
parser.add_argument('integer', nargs='?', type=int, default=10, help='Add an integer such as 17 to set the length of the password. If none is given, the default will be used')
parser.add_argument('-c', help="enable strong passwords", action="store_true")
arg = parser.parse_args()

# https://stackoverflow.com/questions/16878315/what-is-the-right-way-to-treat-python-argparse-namespace-as-a-dictionary

#passwd = []
passwd_complexity = False
inputs = vars(arg)

if arg.c:
    passwd_complexity = simple_string
else:
    passwd_complexity = complex_string

inputs = vars(arg)

int = inputs['integer']
new_password = ""

for i in range(int):
    random_number = random.randint(0, len(passwd_complexity) - 1)
    new_password += passwd_complexity[random_number]

print(new_password)
