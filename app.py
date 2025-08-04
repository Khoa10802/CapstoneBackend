from flask import Flask, request, jsonify
from flask_cors import CORS   # <-- thêm dòng này
from Helpers.sol_compilation import package_assemble

app = Flask(__name__)
CORS(app)   # <-- bật CORS cho toàn bộ app

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Backend running 🚀"})

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "File not found"}), 400

    solFile = request.files['file']
    sol_str = solFile.read().decode('utf-8')

    if sol_str:
        result = package_assemble(sol_str)
        return jsonify({"status": "success", "result": result})

    return jsonify({"error": "Empty file"}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
