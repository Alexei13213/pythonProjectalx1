string_sample = "Hello world world"
string_sample2 = "first LetteR is lowErcase"
string_sample3 = " extra whitespace string "
german_sample = "der FluB"
hello_spl = "hello"

a = 'Hello'
b = 'world'
print(a, b, 'planet of Earth')

salary = 2000
first = 'Bob'
last = 'Smith'
sample = 'Hello {2} {1}. Yor salary is {0}. Is your name {0}. You are from {3}'
print(sample.format(first, last, salary, 'London'))



byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(byte_sting.decode('utf-16'))