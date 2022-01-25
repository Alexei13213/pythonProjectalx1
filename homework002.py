example_string1 = "Hello bro"
a = example_string1[0:2]
b = example_string1[7:]
print(a + b)

example_string2 = "jack Is My NAME"
print(example_string2.replace("jack Is My NAME", "Jack is my name"))

example_string3 = "*Get rid of stars please*"
print(example_string3.strip('*'))

example_string4 = "hello my name is jack"
print(example_string4.replace("hello my name is jack", "Hello my name is Jack"))

# Write a code to return formatted string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
print(var2.replace("hello", "Hello"), var3.replace("MY NAME IS", "my name is"), var1.replace("jack", "Jack"))

# Write a code to return byte_string text value
byte_string = b"\316\273"
print(byte_string.decode())

# Write a code to return True if cost is greater than 500$
example_string5 = "It cost me 1000.00$"
print(example_string5[-8: -1])