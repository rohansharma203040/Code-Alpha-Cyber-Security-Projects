# Task 3: Secure Coding Review

## Introduction
This task focuses on reviewing a Python authentication application to identify
security vulnerabilities and apply secure coding best practices to mitigate risks.

## Application Overview
The application simulates a simple user login system. Two versions are provided:
- `vulnerable_app.py` – contains intentional security flaws
- `secure_app.py` – improved version following secure coding principles

## Identified Vulnerabilities
- Hardcoded credentials
- Plain-text password handling
- Logging of sensitive information
- Lack of input validation
- No error handling

## Security Impact
These issues can lead to credential leakage, unauthorized access, and data exposure.

## Secure Coding Improvements
- Password hashing using SHA-256
- Secure password input using `getpass`
- Removal of sensitive data from logs
- Input validation and exception handling
- Modular and maintainable code structure

## Conclusion
This review demonstrates how insecure coding practices can introduce serious
security risks and how applying secure coding standards significantly improves
application security.
