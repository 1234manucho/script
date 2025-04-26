#variables
a=10
b=3
sum=a+b
print(sum)
# Example of logical operators
x = True
y = False

# Logical AND
print(x and y)  # Output: False

# Logical OR
print(x or y)   # Output: True

# Logical NOT
print(not x)    # Output: False

# Example of comparison operators
num1 = 5
num2 = 10

# Greater than
print(num1 > num2)  # Output: False

# Less than
print(num1 < num2)  # Output: True

# Equal to
print(num1 == num2)  # Output: False

# Not equal to
print(num1 != num2)  # Output: True

# Greater than or equal to
print(num1 >= num2)  # Output: False

# Less than or equal to
print(num1 <= num2)  # Output: True


#data structures
# List
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Tuple
coordinates = (10, 20)
print(coordinates)

# Set
unique_numbers = {1, 2, 3, 4}
print(unique_numbers)

# Dictionary
person = {"name": "John", "age": 30}
print(person)

car ={"brand":"ford",
      "model":"mustang",
      "year":1964,
      "user":"john",
      "color":"red",
      "engine":"v8",
      }

# Accessing dictionary values
print(car["brand"])  # Output: ford
print(car["color"])  # Output: red
print(car["engine"])  # Output: v8  
print(len(car["color"]))  # Output: 3 (length of the string "red")
print(car["year"])  # Output: 1964

name=["john","simiyu","wetende","wamboi","james","eric","smith"] 
print(name)  # Output: ['john', 'jane', 'doe', 'smith', 'james']
print(name[-2])  # Output: john
print(name[0:3])  # Output: ['john', 'jane', 'doe']
print(name[1:4])  # Output: ['jane', 'doe', 'smith']

# Append "waitherero" to the list
name.append("waitherero")
print(name[1])  # Output: ['john', 'jane', 'doe', 'wamboi', 'james', 'waitherero']

print(name[1:3])  

