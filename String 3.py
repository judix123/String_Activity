string = input("Enter a string: ")
prefix_checker = input("Enter a prefix to check: ")

if string.startswith(prefix_checker):
    print(f"The string starts with {prefix_checker}")

else:
    print(f"The string does not start with {prefix_checker}")
