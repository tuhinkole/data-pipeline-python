# File I/O
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a basic Python script.\n")
# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File content:")
    print(content)