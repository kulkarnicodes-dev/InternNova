# task4_scope.py
x = "I am a GLOBAL variable"

def show_scope():
    x = "I am a LOCAL variable"
    print("Inside function:", x)

def modify_global():
    global x
    x = "Global variable modified inside function"

show_scope()
print("Outside function:", x)

modify_global()
print("After modify_global():", x)
