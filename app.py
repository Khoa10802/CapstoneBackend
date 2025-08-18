import io
from docx import Document

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from solcx.exceptions import SolcError, UnsupportedVersionError

from Compilation.sol_compilation import package_assemble, ExternalInclusionError, VersionNotFoundError
from predict import predict_vulnerabilities

app = Flask(__name__, template_folder="templates")
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "File not found"}), 400

    sol_file = request.files['file']
    if sol_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        if sol_file.filename.lower().endswith('.docx'):
            docx_file = io.BytesIO(sol_file.read())
            doc = Document(docx_file)
            docx_text = []
            for para in doc.paragraphs:
                docx_text.append(para.text)
            if len(docx_text) <= 1 and docx_text[0] == '':
                return jsonify({"error": f"{sol_file.filename} is maybe empty"}), 400
            compiled_sol = package_assemble('\n'.join(docx_text))
        else:
            sol_str = sol_file.read().decode('utf-8')
            if len(sol_str) <= 0:
                return jsonify({"error": f"{sol_file.filename} is maybe empty"}), 400
            compiled_sol = package_assemble(sol_str)
        return predict_vulnerabilities(compiled_sol)

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

if __name__ == "__main__":
    app.run(debug=True, port=5000)
