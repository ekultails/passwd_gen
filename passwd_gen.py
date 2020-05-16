#!/usr/bin/env python3
import string
import random
import argparse

string = string.ascii_letters + string.digits
parser = argparse.ArgumentParser(description='A basic password generator')
parser.add_argument('integer', nargs='?', type=int, default=10, help='Add an integer such as 17 to set the length of the password. If none is given, the default will be used')
number = parser.parse_args()

# https://stackoverflow.com/questions/16878315/what-is-the-right-way-to-treat-python-argparse-namespace-as-a-dictionary

inputs = vars(number)

arg = inputs['integer']

if arg < 63:
    pass
else:
    raise ValueError("Password length greater than 62 is not support at this time")
    #exit(code=1)

passwd = random.sample(string, inputs['integer'])
print("".join(passwd)) # Prints Password without array


