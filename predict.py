import pickle

from flask import Flask, request, jsonify

app = Flask('attended')

model_file = 'model_C=1.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


@app.route('/predict', methods=['POST'])
def predict():
    member = request.get_json()

    X = dv.transform([member])
    y_pred = model.predict_proba(X)[0, 1]
    attended = y_pred >= 0.5

    result = {
        'attended_probability': float(y_pred),
        'attended': bool(attended)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5454)