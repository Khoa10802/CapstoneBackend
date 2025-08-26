import io
import time  # 🆕 Thêm để đo thời gian

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from docx import Document
from solcx.exceptions import SolcError, UnsupportedVersionError

# Custom imports
from sol_compilation import package_assemble, ExternalInclusionError, VersionNotFoundError
from predict import predict_vulnerabilities, predict_contract  # Gộp cả 2 hàm predict

app = Flask(__name__, template_folder="templates")
CORS(app)

# ─────────────────────────────────────────────
# GET route to serve the main page
@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

# ─────────────────────────────────────────────
# POST route to upload file and run vulnerability prediction
@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "File not found"}), 400

    sol_file = request.files['file']
    if sol_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        start_time = time.time()  # ⏱️ Bắt đầu tính thời gian

        if sol_file.filename.lower().endswith('.docx'):
            # Read and extract text from docx
            docx_file = io.BytesIO(sol_file.read())
            doc = Document(docx_file)
            docx_text = [para.text for para in doc.paragraphs]
            if len(docx_text) <= 1 and docx_text[0] == '':
                return jsonify({"error": f"{sol_file.filename} is maybe empty"}), 400
            compiled_sol = package_assemble('\n'.join(docx_text))
        else:
            # Handle raw Solidity (.sol) files
            sol_str = sol_file.read().decode('utf-8')
            if len(sol_str) <= 0:
                return jsonify({"error": f"{sol_file.filename} is maybe empty"}), 400
            compiled_sol = package_assemble(sol_str)

        result = predict_vulnerabilities(compiled_sol)

        end_time = time.time()
        duration_seconds = round(end_time - start_time, 2)  # ⏱️ Tính thời gian chạy

        result["duration"] = duration_seconds  # ✅ Thêm field duration vào JSON response

        return result

    except ExternalInclusionError:
        return jsonify({"error": f"{sol_file.filename} may contain external library"}), 400
    except VersionNotFoundError:
        return jsonify({"error": f"{sol_file.filename} may not define pragma version"}), 400
    except SolcError:
        return jsonify({"error": "Compilation failed"}), 400
    except UnsupportedVersionError:
        return jsonify({"error": "Does not support this file version"}), 400
    except ValueError:
        return jsonify({"error": "No contracts found"}), 400

# ─────────────────────────────────────────────
# Optional: Raw Solidity string (via API)
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    try:
        source_code = file.read().decode('utf-8')
        result = predict_contract(source_code)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ─────────────────────────────────────────────
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
