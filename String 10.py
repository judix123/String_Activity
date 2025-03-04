string = input("Enter a words separated by space: ").split()
delimiter = input("Enter a delimiter: ")

join_string = delimiter.join(string)

print(f"Joined Strings:", join_string)