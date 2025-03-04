string = input("Enter a string: ")
substring = input("Enter the substring to find: ")

sub_finder = string.find(substring)

if sub_finder != -1:
    print(f"The substring \"{substring}\" is found at index {sub_finder}")
else:

    print(f"The substring \"{substring}\" is not found in the string.")

