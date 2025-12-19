import os

def dangerous_code():
    user_input = os.getenv("USER_INPUT")
    # This is a security vulnerability (eval injection)
    eval(user_input)
