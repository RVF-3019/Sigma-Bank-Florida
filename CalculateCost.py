
price = 10
product = 50

print("Sky is blue")
def square(number):
    return number * number

def emoji_convert(message):
    words = message.split(" ")
    emojis = {
        ":)": "Q",
        ":(": "Z"
    }
    output = ""
    for word in words:
        output+= emojis.get(word,word)

    return output







result = square(price)
# message = input(">")
#words = message.split(" ")




class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()

point1.move()
    # pascal naming convention

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(f"{age} risk: {risk}")
except ZeroDivisionError:

    print("Age cannot be 0")
except ValueError:
    print('Invalid Value')






# print(result)

