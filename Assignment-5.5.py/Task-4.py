#task 4
#1.Insecure login code
username = input("Username: ")
password = input("Password: ")
if password == "admin123":
    print("Login successful")
else:
    print("Login failed")

#2.Secure login code with hashed passwords
import hashlib
def hash_password(password):
    return
    hashlib.sha256(password.encode()).hexdigest()
stored_hashed_password = hash_password("admin123")
username = input("Username: ")
password = input("Password: ")
if hash_password(password) == stored_hashed_password:
    print("Login successful")
else:
    print("Login failed")