string_sample = "Hello world world"
string_sample2 = "first LetteR is lowErcase"
string_sample3 = " extra whitespace string "
german_sample = "der FluB"
hello_spl = "hello"
sample = '''hello world'''
print(hello_spl in string_sample)
print(string_sample.upper())

string_sample = string_sample.upper()
print(string_sample)

print(german_sample.lower())
print(german_sample.casefold())
print(string_sample[5:12].upper())
print(sample.capitalize())

print(string_sample.replace("wolrd", "").replace(' ',''))
print(string_sample.replace("world", "planet"))

a, b, c = string_sample.split()
print(a)
print(b)
print(c)
print(string_sample.split())

a, b, c = input("Please enter something").split()
print(a)
print(b)
print(c)