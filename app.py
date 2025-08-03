from flask import Flask, render_template, request
from Helpers.sol_compilation import package_assemble

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'File is not found'

        solfile = request.files['file']
        sol_str = solfile.read().decode('utf-8')

        if solfile:
            return package_assemble(sol_str)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)