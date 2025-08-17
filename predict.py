import re, json, os
import joblib

def normalize_opcode(opcode):
    if isinstance(opcode, list):
        opcode = " ".join(opcode)
    opcode = str(opcode)
    opcode = re.sub(r"\s+", " ", opcode).strip()
    opcode = re.sub(r"0x[0-9a-fA-F]+", "CONST", opcode)
    return opcode

model_dir = os.path.join(os.path.dirname(__file__), "trained_data")

xgb_model = joblib.load(os.path.join(model_dir, 'xgb_model.joblib'))
label_binarizer = joblib.load(os.path.join(model_dir, 'label_binarizer.joblib'))
tfidf_vectorizer = joblib.load(os.path.join(model_dir, 'vectorizer.joblib'))

def predict_vulnerabilities(json_path: str):
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"The file does not found: {json_path}")
    
    if os.path.getsize(json_path) == 0:
        raise ValueError(f"The file is empty: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {json_path}")
    
    if not data or not isinstance(data, dict):
        raise ValueError("Input JSON is empty or not a valid object.")

    contracts = data.get("contracts", {})
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

if __name__ == "__main__":
    test_json = "test/sample_opcode.json"
    results = predict_vulnerabilities(test_json)
    print(results)