# Secure Authentication Program
import hashlib
import getpass
from datetime import datetime
# ✅ Credentials stored securely (hashed)
STORED_USERNAME = "admin"
STORED_PASSWORD_HASH = hashlib.sha256("admin123".encode()).hexdigest()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(username: str, password: str) -> bool:
    if not username or not password:
        return False

    return (
        username == STORED_USERNAME and
        hash_password(password) == STORED_PASSWORD_HASH
    )

def log_login_attempt(username: str, success: bool):
    status = "SUCCESS" if success else "FAILED"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ✅ No sensitive data logged
    with open("secure_login_logs.txt", "a") as file:
        file.write(f"{timestamp} | User: {username} | Status: {status}\n")

def main():
    try:
        username = input("Enter username: ").strip()
        password = getpass.getpass("Enter password: ")

        is_authenticated = authenticate_user(username, password)
        log_login_attempt(username, is_authenticated)

        if is_authenticated:
            print("Login successful")
        else:
            print("Login failed")

    except Exception as error:
        print("An unexpected error occurred.")

if __name__ == "__main__":
    main()