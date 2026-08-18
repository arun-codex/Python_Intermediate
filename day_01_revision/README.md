## 1. Variables and data types

```
# 1. Variables and data types

name = "Arun"
Age = 20
Gender = "Male"
marks = [80, 50,88,96]
persentage = 77.8

print(type(name))
print(type(Age))
print(type(marks))
print(type(persentage))

print(name)
print(Age)
print(Gender)
print(marks[0])
print(persentage)

```


## 2. Strings

``` 
# 2. Strings

text = "Python Cybersecurity"

len(text)
text.lower()
text.upper()
text.capitalize()
text.replace("Python", "Advance Python")
text.split

text[0]
text[-1]

print(len(text))
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.replace("Python","Advance Python"))
print(text.split(" "))
print(text[0])
print(text[-1])

```

## 3. Lists

```
# 3. Lists

marks = [85, 72, 91, 66, 88]

print(len(marks))
print(sum(marks))
print((max(marks)))
print(min(marks))

marks.append(95)
print(marks)

marks.remove(66)
print(marks)

marks.sort()
print(marks)

print(sorted(marks))

```


## 4. Dictionaries

```
# 4. Dictionaries


student = {
    "name": "Arun",
    "age": 23,
    "marks": 85
}

print(student["name"])
print(student["age"])
print(student["marks"])

student["course"] = "BCA"

print(student)

```



## 5. Conditions

```
# 5. Conditions


marks = int(input("Enter your marks: "))

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("C")
    
```

# LOOP

## 6. for loops

```
# 6. for loops


for i in range(1,11):
    print(i)
```

## 7. while loops

```
# 7. while loops


numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
```
