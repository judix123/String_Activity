string = input("Enter a string: ")
suffix_checker = input("Enter a prefix to check: ")

if string.endswith(suffix_checker):
    print(f"The string ends with {suffix_checker}")

else:
    print(f"The string does not end with {suffix_checker}")
