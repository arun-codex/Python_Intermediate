# 1. Variables and data types

# code are in readme.md 



# 2. Strings

# code are in readme.md


# 3. Lists

# code are in readme.md

# 4. Dictionaries


# code are in readme.md

# 5. Conditions

# code are in readme.md

# 6. for loops

# code are in readme.md
# code are in readme.md


# 7. while loops

# code are in readme.md
# code are in readme.md


# Also write a while loop that counts from 1 to 5.

# code are in readme.md

# 8. Functions

# Basic function:

# code are in readme.md

# Function with parameter:

# code are in readme.md

# Function with return:

# code are in readme.md

# CHALLENGE 1 — EVEN NUMBER

# code are in readme.md


# CHALLENGE 2 — PRIME NUMBER

def prime_number(number):
    if number <= 1:
        return False

    for i in range(2, int(number)):
        if number % i == 0:
            return False

    return True

number = int(input("Enter a number: "))

if prime_number(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")