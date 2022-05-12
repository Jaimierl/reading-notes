import re
#your code goes here
number = input()
pattern =  r"[1|8|9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
if re.match(number,pattern):
    print("Valid")
else:
    print("Invalid")

    def concatenate(*args):
    print("-".join(args))
print(concatenate("I", "love", "Python", "!"))