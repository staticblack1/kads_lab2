from unicodedata import decimal
import math
name = 'kadeyen'
age = 20
height = 5.7
favorite_color = 'Blue'
print(name)
print(age)
print(height)
print(favorite_color)
print(name ,age , height ,favorite_color)
print(f"my name is {name}, i am {age} calender years.")
print(f"""
    name: {name}
age: {age}
""")

radius=5
circle_area= 3/4 * math.pi * radius**3
print(F"circle_area: {circle_area:.1f}")


sqrt= math.sqrt(age)
print(round(sqrt,2))
sin=math.sin(height)
print(round(sin,1))
cos=math.cos(height)
print(round(cos,2))

sum= age * 5
Difference=height - 4
quotient = height // 2
remainder= age / 3
power= age ** 2
print(f"""sum: {sum}
Difference: {round(Difference, 2)}
quotient: {quotient}
remainder: {round(remainder, 2)}
power: {power}""")

Fahrenheit= float(input("Enter temperature in Fahrenheit: "))
celsius= (Fahrenheit-32) * 5/9
print(round(celsius, 2))
