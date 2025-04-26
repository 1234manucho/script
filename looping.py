def add_numbers(a, b):
    """This function takes two numbers and returns their sum."""
    return a + b

add_numbers(10, 3)
sum=add_numbers(10, 3)
print(sum)
def greeting(name):
    """This function takes a name and returns a greeting message."""
    return f"Hello, {name}!"
print(greeting("Alice"))

def kids_age(age):
    """This function takes a child's age and returns a message."""
    if age < 13:
        return "You are a child."
    elif 13 <= age < 20:
        return "You are a teenager."
    else:
        return "You are an adult."
print(kids_age(50))  # Output: You are a child.



a=10
type(str(a))



name=input("Enter your name: ")
print(f"My name is{name}")