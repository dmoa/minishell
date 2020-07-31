def startup():
    import os
    import time
    rows, columns = os.popen('stty size', 'r').read().split()
    for i in range(1, int(columns) + 1):
        print("*"*i)
        time.sleep(0.01)
    print("TERMINAL UWU?")


def terminal():


    while True:
        user_input = input("$ ").lower()

        command = user_input.split(maxsplit=1)[0]

        if command == user_input:
            bad_input(command)

        if command in ["exit", "die", "toasterbath", "lavabucket"]:
            break
        elif command == "echo":
            print(user_input[5:])
        elif command == "add":
            try:
                nums = map(int, user_input[4:].split(" "))
                print(sum(nums))
            except:
                bad_input(command)
        elif command == "f":
            try:    print(factorial(int(user_input[2:])))
            except: bad_input(command)


def bad_input(command):
    docs = {
        "echo": "echo string...",
        "add": "add num1 num2 num3...",
        "f": "f number"
    }

    if command in docs:
        print( "Incorrect Usage\nUsage: " + docs[command] )
    else:
        print( "Command doesn't exit!" )

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)


startup()
terminal()