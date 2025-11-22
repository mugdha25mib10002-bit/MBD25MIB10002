from getpass import getpass

USERS = {"teacher":{"password":"teach1002","role":"teaching"},
         "principal":{"password":"princ1001","role":"head"},}

def login():
    print("=== LOGIN ===")
    username = input("Username: ").strip()
    password = getpass("Password: ").strip()
    user= USERS.get(username)
    if user and user["password"]==password:
        print(f"Login success ({user['role']}).")
        return user
    print("Invalid login.")
    return None