import hmac

real_password = "secure123"

user = input("Enter password: ")

if hmac.compare_digest(user, real_password):
    print("Access Granted")
else:
    print("Access Denied")