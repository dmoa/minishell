def startup():
    import os
    import time
    rows, columns = os.popen('stty size', 'r').read().split()
    for i in range(1, int(columns) + 1):
        print("*"*i)
        time.sleep(0.01)
    print("TERMINAL UWU?")


def terminal():

    variables = {}


    while True:
        user_input = input("$ ").lower()

        command = user_input.split(maxsplit=1)[0]

        if command == user_input:
            bad_input(command)

        if command in ["exit", "die", "toasterbath", "lavabucket"]:
            break
        elif command == "echo":
            if user_input[5] == "$" and user_input[6:] in variables:
                print(variables[user_input[6:]])
            else:
                print(user_input[5:])
        elif command == "add":
            try:
                passing = user_input[4:].split(" ")
                nums = []
                for arg in passing:
                    if arg[0] == "$":
                        nums.append(variables[arg[1:]])
                    else:
                        nums.append(int(arg))

                print(sum(nums))
            except:
                bad_input(command)
        elif command == "f":
            try:    print(factorial(int(user_input[2:])))
            except: bad_input(command)
        elif command == "set":
            try:
                passing = user_input[4:].split(" ", maxsplit=1)
                variable_name = passing[0]
                value = passing[1] if not passing[1].isnumeric() else int(passing[1])
                variables[variable_name] = value
                print("variable set")
            except: bad_input(command)


def bad_input(command):
    docs = {
        "echo": "echo string...",
        "add": "add num1 num2 num3...",
        "f": "f number",
        "set": "set variable_name value"
    }

    if command in docs:
        print( "Incorrect Usage\nUsage: " + docs[command] )
    else:
        print( "Command doesn't exit!" )

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)


startup()
terminal()