#task3
filename = input("Enter file name: ")
try:
    file = open(filename, "r")
    data = file.read()
    print("File Content:")
    print(data)
    file.close()
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print("An unexpected error occurred:", e)