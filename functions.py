def add(a, b):
    return a + b

def subtract(a, b):
    return a + b  # <--- intentional bug, fix later

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    return multiply(subtract(fahrenheit, 32), 9 / 5)  # also buggy