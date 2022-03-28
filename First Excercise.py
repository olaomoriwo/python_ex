Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
total_passenger = 80,000
total_driver - 4500
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    total_driver - 4500
NameError: name 'total_driver' is not defined
print(total_passenger)
(80, 0)
print(total_driver)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(total_driver)
NameError: name 'total_driver' is not defined
total_driver = 80000
total_passenger = 12.345
print(total_driver)
80000
print(total_passenger)
12.345
x,y,z = ("all", "leg", "fits", "all")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x,y,z = ("all", "leg", "fits", "all")
ValueError: too many values to unpack (expected 3)
print(x,y,z)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(x,y,z)
NameError: name 'x' is not defined
x,y,z=("all", "leg", "fits", "all")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x,y,z=("all", "leg", "fits", "all")
ValueError: too many values to unpack (expected 3)
print(x)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
x,y,z = "all", "fingers", "are", "equal"
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x,y,z = "all", "fingers", "are", "equal"
ValueError: too many values to unpack (expected 3)
x,y,z = "all" "fingers", "collenge"
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x,y,z = "all" "fingers", "collenge"
ValueError: not enough values to unpack (expected 3, got 2)
_val_sent = 20fold
SyntaxError: invalid decimal literal
_val_sent = foldable
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    _val_sent = foldable
NameError: name 'foldable' is not defined. Did you mean: 'callable'?
_val_sent = "20fold"
print(_val_sent)
20fold
fruits = ("apple", "banana", "cherry")
x, y, z = fruits
print(x)
apple
print(y)
banana
print(z)
cherry
x = ("Python is yo yo yo awesome and and ewwwwwww wa wa wa")
print(x)
Python is awesome

y = "Sunny Carabean"
print(y)


