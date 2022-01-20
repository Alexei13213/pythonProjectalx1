string_sample = "Hello world world"
string_sample2 = "first LetteR is lowErcase"
string_sample3 = " extra whitespace string "
german_sample = "der FluB"
hello_spl = "hello"
sample = '''hello world'''

a, b = 'ab'


print(string_sample.find('world'))
print(string_sample[string_sample.find('world'):])
print(string_sample[string_sample.find('world'):(string_sample.find('world') + len('world'))])
print(string_sample[6:11])
x = 23423234231111
print(len(str(x)))

print(string_sample.count('world'))

print(str(x).count(str(1)))

