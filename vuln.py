import os

# Уязвимость: команда с пользовательским вводом
def execute_command():
    user_input = input("Enter command: ")
    os.system(user_input)  # HIGH RISK: Command Injection

# Уязвимость: хардкод пароля
DB_PASSWORD = "admin123!"  # HIGH RISK: Hardcoded secret
