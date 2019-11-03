print ("Please enter your number")

text = int(input())
if (text > 100):
    print("please enter a number between 1 and 100.")
else:

    for x in range(1,text):
        if (x % 3 == 0):
            print("fizz")
        elif (x % 5 == 0):
            print("buzz")
        elif (x % 3 == 0 and x % 5 == 0):
            print("fizzbuzz")
        else:
            print(x)