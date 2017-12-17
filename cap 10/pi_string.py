filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in form mmddyy: ")
if birthday in pi_string:
    print("Your birthday is on the first one million digits of pi !!")
else:
    print("Your birthday isnt on pi ")
