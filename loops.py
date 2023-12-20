number = 0

while(number <= 10):
    print(number)
    number += 1

#FOR LOOP

for num in range(0, 10):
    print(num)

for letter in "Python":
    print("t" in "python ")

#Nested Loop

lines = int(input("How many lines ?"))
row = 0
while (row < lines):
    col = 0
    print("*", end= '')
    col += 1
    row += 1
    print()
