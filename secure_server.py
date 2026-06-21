from flask import Flask, request
import hmac
 
app = Flask(__name__)
real_password = "secure123"
 
def check_password(user_input):
    if user_input is None:
        return False
    return hmac.compare_digest(user_input, real_password)
 
@app.route("/login", methods=["POST"])
def login():
    password = request.form.get("password")
    if check_password(password):
        return "Access Granted"
    else:
        return "Access Denied"
 
if __name__ == "__main__":
    
    app.run(port=5001)
 