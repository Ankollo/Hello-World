filename = 'test.txt'
list1 = ['0','1','2']

with open(filename, 'w') as file:
    file.write("write test:\n")

for x in list1:
    with open(filename, 'a') as file:
        file.write(x+'\n')

with open(filename, 'r') as file:
    print(file.read())

#traceback
def devide(num1, num2):
    print("The devide result is: " + str(num1/num2))

try:
    devide(5,3)
except ZeroDivisionError as e:
    print(e)
else:
    print("You are right.")
