# Vulnerable Authentication Program
# NOTE: This code contains intentional security flaws for learning purposes

username = input("Enter username: ")
password = input("Enter password: ")

# ❌ Hardcoded credentials (bad practice)
if username == "admin" and password == "admin123":
    print("Login successful")

    # ❌ Sensitive data written directly to file
    with open("login_logs.txt", "a") as file:
        file.write(f"User {username} logged in with password {password}\n")
else:
    print("Login failed")
