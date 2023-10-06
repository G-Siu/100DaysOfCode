# with open("file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("/Users/garys/OneDrive/Desktop/new_file.txt") as file:  # First / is root (C drive)
#     print(file.read())

with open("../../../../Desktop/new_file.txt") as file:  # ../ to go up a directory
    print(file.read())
