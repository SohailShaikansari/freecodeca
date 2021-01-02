import math
print("Hello World")
print('Hello World')
print("Hello\nWorld")
print('   /|')
print(' / |')
print(' /  |')
print('/___|')
print('Hello\'World')
character_name = "abraham"
character_age = "28"
print("there once was a man named " + character_name)
print("he was" + character_age + "years old")
character_name = "mike"
character_age = "58"
print("he raelly liked the name" + character_name)
print("but he didn't like being " + character_age)
print('Giraffe Academy')
print("Giraffe\nAcademy")
print('Giraffe\'Academy')
phrase = "Giraffe Academy"
print(phrase)
print(phrase + " is cool ")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[8])
print(phrase[0])
print(phrase.index("y"))
print(phrase.index("Acad"))
# print(phrase.index("to"))
print(phrase.replace("Giraffe", "Elephant"))
print(2)
print("2")
print(-2.098)
print(3+4.5)
print(3*4+5)
print(3*(4+5))
print(10 % 3)
print(10/3)
print(3**3)
print(10//3)
my_num = 5
print(str(my_num) + " is my fav num")
#print((my_num) + " is my fav num")
print(abs(my_num))
print(pow(3, 2))
print(min(3, 2))
print(max(3, 2))
print(round(3.2))
print(round(3.7))
# print(floor(3.2))
# print(ceil(3.2))
# print(sqrt(36))
'''
name = input("Enter your name")
print("Hi" + name)
age = input("Enter your age")
print("Hi" + age)
num1 = input("Enter a number")
num2 = input("Enter another number")
num3 = float(num1) + float(num2)
print(str(num3) + " is my favourite number")
'''
'''
friends = ["kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends.index("kevin"))
print(friends[1:])
print(friends[:3])
print(friends[:])
friends[1] = "mike"
print(friends)
'''
'''
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("creed")
print(friends)
friends = ["kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "kelly")
print(friends)
friends.remove("Jim")
print(friends)
friends.pop()
print(friends)
print(friends.count("Jim"))
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends2 = friends.copy()
print(friends2)
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0])
print(number_grid[0][0])
for row in number_grid:
    for col in row:
        print(col)

coordinates = (4, 5)
print(coordinates)
'''

'''
def say_hi():
    print("Hello World")


say_hi()
'''

'''
def say_hi(name, age):
    print("Hello " + name + " You are " + str(age) + " years old")


say_hi("Sohail", "24")


def cube(num):
    return num * num * num


print(cube(3))
'''
'''
ismale = False
istall = False
if ismale or istall:
    print("you are a tall male")
elif ismale and istall:
    print("you are a male")
else:
    print("you are a female")
'''

'''
def maxthree(a, b, c):
    if a >= b and a >= c:
        print(str(a) + "is bigger ")
    elif b >= a and b >= c:
        print(str(b) + "is bigger")
    else:
        print(str(c) + "is bigger")


maxthree(3, 4, 5)
'''

'''
i = 1
while(i < 10):
    print(i)
    i += 1
    print(str(i) + " updated")
print("Done with loop")
'''
'''
for x in "Giraffe Academy":
    print(x)

friends = ["jim", "Karen", "Kevin"]
for x in range(len(friends)):
    print(friends[x])
'''

'''
def pownum(base, exp):
    result = 1
    for x in range(exp):
        result = result * base
    return result


print(pownum(2, 3))
'''
'''
monthconversions = {
    "jan": "January",
    "Feb": "February",
    "0": "Zero",
}
print(monthconversions["jan"])
print(monthconversions.get("love", "Not a Valid key"))
'''
