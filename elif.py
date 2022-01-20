isikukood = input("Please enter ID: ")
if len(isikukood) == 11:
    print('ID is ok')
elif len(isikukood) > 11:
    print('ID is too long')
else:
    print('ID is too short')

if len(isikukood) != 11:
    if len(isikukood) > 11:
        print('ID is too long')
    else:
        print('ID is to short')



sample = 'Hello world'

if "HELLO" in sample.upper():
    print('Condition is ok')