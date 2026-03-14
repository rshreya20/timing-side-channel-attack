import time

real_password = "secure123"

def check_password(user_input):
    for i in range(len(real_password)):
        if i >= len(user_input) or user_input[i] != real_password[i]:
            return False
        
        # intentional delay to simulate timing leak
        time.sleep(0.2)

    return len(user_input) == len(real_password)


user = input("Enter password: ")

if check_password(user):
    print("Access Granted")
else:
    print("Access Denied")