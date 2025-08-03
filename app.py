from flask import Flask, render_template, request
from Helpers.sol_compilation import package_assemble

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'File is not found'

    solfile = request.files['file']
    if solfile:
        return package_assemble(solfile)
    return None

if __name__ == '__main__':
    app.run(debug=True)