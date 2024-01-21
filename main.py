import random

lowerchar = 'abcdefghijklmnopqrstuvwxyz'

upperchar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numbers = '1234567890'

symbols = '!@#$%^&*().'

string = lowerchar + upperchar+ symbols + numbers

lenghtofpass = int(input('enter your password length'))

password = "".join(random.sample(string,lenghtofpass))

print('your new password is ', password)
