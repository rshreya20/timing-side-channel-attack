# Timing Side Channel Attack Demonstration

This project demonstrates a **Timing Side Channel Attack** on a vulnerable authentication system.  
It shows how an attacker can recover a secret password by analyzing **response time differences** during password verification.

---

## Project Overview

In many systems, passwords are compared **character by character**.  
If a delay occurs after each correct character, the system unintentionally leaks information through **timing differences**.

An attacker can exploit this by:

- Sending multiple password guesses
- Measuring the response time of the authentication system
- Inferring correct characters based on longer response times
- Gradually reconstructing the entire password

This project simulates that attack and also demonstrates how to **mitigate the vulnerability**.

---

## Key Concepts Demonstrated

- Side Channel Attacks
- Timing Attacks
- Password Authentication Vulnerabilities
- Secure Constant-Time Comparisons
- Automated Attack Scripts
- Security Mitigation Techniques

---

## Project Structure
SIDE_CHANNEL_PRJCT
│
├── password_checker.py
├── attack_script.py
├── secure_password_checker.py
├── vulnerable_server.py
├── timing_attack.py
├── timing_graph.py
└── timing_results.txt


---

## File Descriptions

### `password_checker.py`
- Simulates a **vulnerable authentication system**
- Compares password characters sequentially
- Introduces a delay after each correct character
- Creates a timing side-channel vulnerability

### `attack_script.py`
- Performs a **local timing attack**
- Measures execution time for different password guesses
- Recovers the password character by character

### `secure_password_checker.py`
- Demonstrates the **secure implementation**
- Uses constant-time comparison (`hmac.compare_digest`)
- Prevents timing leaks

### `vulnerable_server.py`
- Implements a **Flask-based login API**
- Simulates a real-world vulnerable web authentication system

### `timing_attack.py`
- Sends automated **HTTP requests** to the vulnerable server
- Measures response times
- Infers correct password characters using timing differences

### `timing_graph.py`
- Visualizes timing leakage
- Generates a graph showing how response time increases with correct characters

### `timing_results.txt`
- Stores timing measurements collected during the attack

---

## How the Attack Works

1. The attacker sends multiple password guesses to the system.
2. The system compares characters one-by-one with a delay.
3. If more characters match, the response takes longer.
4. The attacker measures the response time.
5. The attacker identifies the character causing the longest delay.
6. This process repeats until the full password is recovered.


---

## Security Mitigation

To prevent timing attacks:

- Use **constant-time comparison functions**
- Avoid character-by-character password checks
- Implement proper authentication frameworks

Example secure comparison:

```python
import hmac
hmac.compare_digest(user_input, real_password)
