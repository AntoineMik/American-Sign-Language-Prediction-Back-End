from helpers import *
from flask import Flask
from flask import jsonify
from flask import request
from flask import send_file
app = Flask(__name__)

# Generate random images based on length
@app.route("/images/random", methods=["POST"])
def raw():
    try:
        length = int(request.form.get('length'))
    except Exception as e:
        return jsonify({'message': 'Invalid request'}), 500
    if generate_user_raw(length):
        rand_img = display_img(user_test_path)
        rand_img.savefig("user_rand.jpg")
        return send_file("user_rand.jpg", mimetype='image/jpeg')
    else:
        return jsonify({'data': "failed"})

# Get process users random images with mediapipe
@app.route("/images/process", methods=["POST"])
def proc():
    try:
        length = int(request.form.get('length'))
    except Exception as e:
        return jsonify({'message': 'Invalid request'}), 500
    if generate_user_processed(length):
        rand_img = display_img(user_processed_path)
        rand_img.savefig("process_rand.jpg")
        return send_file("process_rand.jpg", mimetype='image/jpeg')
    else:
        return jsonify({'data': "failed"})

# Predict users randomly generated processed images
@app.route("/images/predict", methods=["POST"])
def pred():
    try:
        length = int(request.form.get('length'))
    except Exception as e:
        return jsonify({'message': 'Invalid request'}), 500

    prediction_img = predict_img(user_processed_path)
    if not prediction_img:
        return jsonify({'Failed': "Generate random images before prediction"})
    else:
        prediction_img.savefig("user_pred.jpg")
        return send_file("user_pred.jpg", mimetype='image/jpeg')

# Get random predicted images
@app.route("/images/random/predict", methods=["POST"])
def rand():
    try:
        length = int(request.form.get('length'))
    except Exception as e:
        return jsonify({'message': 'Invalid request'}), 500

    prediction_img = show_rand_pred(length, original_processed_path)
    prediction_img.savefig("rand_pred.jpg")

    return send_file("rand_pred.jpg", mimetype='image/jpeg')


@app.route("/", methods=["POST"])
def main():
    try:
        length = int(request.form.get('length'))
    except Exception as e:
        return jsonify({'message': 'Invalid request'}), 500

    result = jsonify({'Server': "Operational", 'Data':length})

    return result

# Get the size of images
@app.route("/images/size", methods=["GET"])
def get_size():
    size = get_len()
    return jsonify(size)



# Health Check
@app.route("/check", methods=["GET"])
def healthCheck():
    return "Server Operational", 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")