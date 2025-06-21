from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, DevSecOps!"
@app.route('/cmd')
def run_cmd():
    cmd = request.args.get('c')  # Параметр ?c=whoami
    return subprocess.getoutput(cmd)  # Уязвимость RCE!
if __name__ == '__main__':
    app.run()
