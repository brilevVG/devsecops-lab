import subprocess

def safe_execute(command):
    subprocess.run([command], shell=False)  # Безопасный вызов
import os
DB_PASSWORD = os.getenv("DB_PASS")  # Безопасное хранение
