from pip._vendor.distlib.compat import raw_input

print("HELLO WORLD!")

resume = True
while (resume):
    print("Welcome to the Unit Converter. Please enter kilometers to convert them into miles.")
    input = float(raw_input())
    result = float(0.621371 * input)
    print("%.2f" % result)
    print("Would you like to convert another number?")
    input_again = raw_input()

    if (input_again == "No" or input_again == "no"):
        resume = False
