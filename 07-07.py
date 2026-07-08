# Dictionary
d = {"name": "Ayush", "age": 20}
print(d.get("name"))
print(d.keys())
print(d.values())
d.update({"city": "Rajkot"})
print(d)
d.pop("age")
print(d)

# List
l = [10, 20, 30]
l.append(40)
print(l)
l.insert(1, 15)
print(l)
l.remove(20)
print(l)
l.sort()
print(l)
l.pop()
print(l)

# Tuple
t = (1, 2, 3, 2, 5)
print(t.count(2))
print(t.index(3))
print(len(t))
print(max(t))
print(min(t))

# Set
s = {1, 2, 3}
s.add(4)
print(s)
s.remove(2)
print(s)
s.discard(5)
print(s)
s.pop()
print(s)
s.clear()
print(s)

# if
a = 10
if a > 5:
    print("Greater")

# if else
b = 7
if b % 2 == 0:
    print("Even")
else:
    print("Odd")

# if elif else
m = 80
if m >= 90:
    print("A")
elif m >= 70:
    print("B")
else:
    print("C")

# Nested if
x = 10
if x > 0:
    if x > 5:
        print("Positive and Greater than 5")
    else:
        print("Positive")
else:
    print("Negative")

# Break
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Pass
for i in range(1, 4):
    if i == 2:
        pass
    print(i)

# Input
name = input("Enter your name: ")
print("Hello", name)

# Range
for i in range(5):
    print(i)

# len
text = "Python"
print(len(text))

# type
n = 10
print(type(n))

# For loop
for i in range(3):
    print("Hello")

# While loop
i = 1
while i <= 3:
    print(i)
    i += 1
