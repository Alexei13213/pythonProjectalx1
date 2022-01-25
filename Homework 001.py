import datetime

print('Hello!')
user_name = input('Enter your name: ')
user_surname = input('Enter your surname: ')
print("Enter your day of birth:")
day = int(input())
print("Enter your month of birth:")
month = int(input())
print("Enter your age of birth:")
year = int(input())

birthday = datetime.date(year, month, day) .strftime("%Y%m%d")
today = datetime.date.today() .strftime("%Y%m%d")

let = (int(today) - int(birthday)) // 10000
x = 152
y = 132
a = x % y
b = a * 13
sqrt = b ** (0.5)
# code parts
code_1 = '354'
code_2 = int(sqrt)
code_3 = '132'

print("Hello", user_name,  user_surname, 'you are', str(let),  "years old!", 'Your secret code is:', code_1 + '-' + str(code_2) + '-' + code_3)
