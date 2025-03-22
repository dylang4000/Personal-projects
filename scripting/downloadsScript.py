import sys

from getpass import getuser

userpath = fr"C:\Users\{getuser()}"

for a in userpath:
    print(a)