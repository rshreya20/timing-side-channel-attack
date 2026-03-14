from flask import Flask, request
import time

app = Flask(__name__)

real_password = "secure123"

def check_password(user_input):
    for i in range(len(real_password)):
        if i >= len(user_input) or user_input[i] != real_password[i]:
            return False
        
        # timing leak
        time.sleep(0.2)

    return len(user_input) == len(real_password)

@app.route("/login", methods=["POST"])
def login():

    password = request.form.get("password")

    if check_password(password):
        return "Access Granted"
    else:
        return "Access Denied"

if __name__ == "__main__":
    app.run(debug=True)