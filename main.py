# function = A block of reusable code
# place () after the function name to invoke it

#def happy_birthday(name, age):
   # print(f"Happy birthday to {name}!")
    #print(f"You are {age} years old!")
    #print("Happy birthday to you!")
   # print()

#happy_birthday("Bro", 20)
#appy_birthday("Eivind", 30)
#happy_birthday("Kim", 40)

#def display_invoice(username, amount, due_date):
    #print(f"Hello {username}")
    #print(f"Your bill of ${amount:.2f} is due: {due_date}")

    #display_invoice("JoeSchmo", 100.01, "01/02")

#return = statement used to end a function
#         and send a result back to the caller


def add(x, y):
    z = x + y
    return z

def  subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))