# map, zip, filter, lambda

# enumearte str

string = "Let's go"
listt = [1, 2, 3, 4, 5]
dict = {}
for i, l in enumerate(string.lower().strip().replace(" ", "")):
    print(f"{l}:{i}")
    dict[l] = i
print(dict)

unique = set(string)
print("".join(unique).islower())

for k, v in dict.items():
    print(k, v * 10)



# ***************************  Common functions   *********************************

# lambda
'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
'''
x = lambda a, b : a * b
print("LAMBDA function")
print(x(5, 6))

'''
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with 
an unknown number:
'''


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


# MAP
def myfunc(a):
    return len(a)


x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
# convert the map into a list, for readability:
print("Map function")
print(list(x))


def myfunc2(a, b):
    return a + b


x = map(myfunc2, ('apple', 'banana', 'cherry'),
        ('orange', 'lemon', 'pineapple'))
print("Map function")
print(list(x))

# zip
'''
The zip() function returns a zip object, which is an iterator of 
tuples where the first item in each passed iterator is paired together,
and then the second item in each passed iterator are paired together etc.

If the passed iterators have different lengths, the iterator with the 
least items decides the length of the new iterator.
'''
a = ["John", "Charles", "Mike"]
b = ["Jenny", "Christy", "Monica", "Vicky"]

x = zip(a, b)
print("ZIP function")
print(list(x))

# filter
'''
The filter() function returns an iterator were the items are filtered 
through a function to test if the item is accepted or not.
'''
ages = [5, 12, 17, 18, 24, 32]


def myFunc3(x):
    if x < 18:
        return False
    else:
        return True




adults = filter(myFunc3, ages)
print("FILTER function")
print(list(adults))

filter_example = filter(lambda x: x * 2, ages)
print(list(filter_example))

def is_odd(x):
    return x % 2 != 0

def add_7(x):
    return x+7

a = [1,2,3,4,5,6,7,8,9,10]
b = list(filter(is_odd, a))
print(b)
print(b)

print("Map+FILTER function")
c = list(map(add_7, filter(is_odd, a)))
print(c)