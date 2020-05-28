#!/usr/bin/env python3
import string
import random
import argparse

simple_string = string.ascii_letters + string.digits
complex_string = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
parser = argparse.ArgumentParser(description='A basic password generator')
parser.add_argument('integer', nargs='?', type=int, default=10, help='Add an integer such as 17 to set the length of the password. If none is given, the default will be used')
arg = parser.parse_args()

# https://stackoverflow.com/questions/16878315/what-is-the-right-way-to-treat-python-argparse-namespace-as-a-dictionary

#passwd = []
passwd_complexity = False
inputs = vars(arg)

int = inputs['integer']
if int < 63:
    pass
else:
    raise ValueError("Password length greater than 62 is not support at this time")

if passwd_complexity == True:
    passwd = random.sample(complex_string, inputs['integer'])
elif passwd_complexity == False:
    passwd = random.sample(simple_string, inputs['integer'])

print("".join(passwd)) # Prints Password without array

