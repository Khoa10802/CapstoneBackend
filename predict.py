import re
import json
import os
import joblib

from Compilation.sol_compilation import package_assemble, ExternalInclusionError, VersionNotFoundError
from solcx.exceptions import SolcError, UnsupportedVersionError

# ─────────────────────────────────────────────
# Tiền xử lý opcode
def normalize_opcode(opcode):
    if isinstance(opcode, list):
        opcode = " ".join(opcode)
    opcode = str(opcode)
    opcode = re.sub(r"\s+", " ", opcode).strip()
    opcode = re.sub(r"0x[0-9a-fA-F]+", "CONST", opcode)
    return opcode

# ─────────────────────────────────────────────
# Load mô hình và công cụ tiền xử lý
model_dir = os.path.join(os.path.dirname(__file__), "trained_data")

xgb_model = joblib.load(os.path.join(model_dir, 'xgb_model.joblib'))
label_binarizer = joblib.load(os.path.join(model_dir, 'label_binarizer.joblib'))
tfidf_vectorizer = joblib.load(os.path.join(model_dir, 'vectorizer.joblib'))

# ─────────────────────────────────────────────
# Dự đoán từ JSON đã biên dịch
def predict_vulnerabilities(compiled_json: dict):
    contracts = compiled_json.get("contracts", {})
    if not contracts:
        raise ValueError("No contracts found in JSON")
    
    results = {}

    for contract_name, opcode in contracts.items():
        cleaned_opcode = normalize_opcode(opcode)
        X = tfidf_vectorizer.transform([cleaned_opcode])
        y_pred = xgb_model.predict(X)
        predicted_labels = label_binarizer.inverse_transform(y_pred)
        results[contract_name] = predicted_labels[0] if predicted_labels else []

    return results

# ─────────────────────────────────────────────
# API /predict – phân tích từ source code Solidity raw
def predict_contract(source_code: str):
    try:
        compiled_sol = package_assemble(source_code)
        return predict_vulnerabilities(compiled_sol)
    except ExternalInclusionError:
        return {"error": "Contract may contain external library"}
    except VersionNotFoundError:
        return {"error": "Contract may not define pragma version"}
    except SolcError:
        return {"error": "Compilation failed"}
    except UnsupportedVersionError:
        return {"error": "Unsupported Solidity version"}
    except ValueError:
        return {"error": "No contracts found"}
