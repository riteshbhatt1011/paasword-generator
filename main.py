import random

lowerchar = 'abcdefghijklmnopqrstuvwxyz'

upperchar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numbers = '1234567890'

symbols = '!@#$%^&*().'

string = lowerchar + upperchar+ symbols + numbers

lenghtofpass = 14

password = "".join(random.sample(string,lenghtofpass))

print('your new password is ', password)
