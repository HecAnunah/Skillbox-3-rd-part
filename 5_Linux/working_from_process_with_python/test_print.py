import sys


def defoult():
    print("Print in stdout")
    print("Print in stderr", file=sys.stderr)
    user_input = input("Enter something: ")
    print('User input: "{}"'.format(user_input))


if __name__ == "__main__":
    defoult()
