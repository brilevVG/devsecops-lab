import subprocess
import os
def safe_execute(command):
    subprocess.run([command], shell=False)  # Безопасный вызов

# Уязвимость: хардкод пароля

DB_PASSWORD = os.getenv("DB_PASS")  # Безопасное хранение
