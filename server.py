from helpers import *
from flask import Flask
from flask import jsonify
from flask import request
from flask import send_file
app = Flask(__name__)

@app.route('/images/<path:path>')
def func_send_image(path):
    try:
        return send_file(path, mimetype='image/jpeg')
    except Exception as e:
        return jsonify({'message': 'Server could not send file'}), 800

# Generate random images based on length
@app.route("/images/random", methods=["POST"])
def raw():
    try:
        length = int(request.form.get('length'))
    except Exception as e:
        return jsonify({'message': 'Invalid request, Could not get the size'}), 500
    
    try:
        if generate_user_raw(length):
            rand_img = display_img(user_test_path)
            rand_img.savefig("user_rand.jpg")
        else:
            return jsonify({'message': "Could not generate processed images"}), 700
    except Exception as e:
        return jsonify({'message': 'Server could not save random images'}), 700
    
    try:
        return send_file("user_rand.jpg", mimetype='image/jpeg')
    except Exception as e:
        return jsonify({'message': 'Server could not send file'}), 800


# Get process users random images with mediapipe
@app.route("/images/process", methods=["POST"])
def proc():
    try:
        length = int(request.form.get('length'))
    except Exception as e:
        return jsonify({'message': 'Invalid request, Could not get the size'}), 500
    
    try:
        if generate_user_processed(length):
            rand_img = display_img(user_processed_path)
            rand_img.savefig("process_rand.jpg")
        else:
            return jsonify({'message': "Could not generate processed images"}), 700
    except Exception as e:
        return jsonify({'message': 'Server could not save processed images'}), 700

    try:
        return send_file("process_rand.jpg", mimetype='image/jpeg')
    except Exception as e:
        return jsonify({'message': 'Server could not send file'}), 800


# Predict users randomly generated processed images
@app.route("/images/predict", methods=["POST"])
def pred():
    try:
        length = int(request.form.get('length'))
    except Exception as e:
        return jsonify({'message': 'Invalid request, Could not get the size'}), 500

    try:
        prediction_img = predict_img(user_processed_path)
        if not prediction_img:
            return jsonify({'Failed': "Please Generate random images before prediction"}), 600
        else:
            prediction_img.savefig("user_pred.jpg")
    except Exception as e:
        return jsonify({'message': 'Server could not save predicted images'}), 700

    try:
        return send_file("user_pred.jpg", mimetype='image/jpeg')
    except Exception as e:
        return jsonify({'message': 'Server could not send file'}), 800


# Get random predicted images
@app.route("/images/random/predict", methods=["POST"])
def rand():
    try:
        length = int(request.form.get('length'))
    except Exception as e:
        return jsonify({'message': 'Invalid request, Could not get the size'}), 500

    try:
        prediction_img = show_rand_pred(length, original_processed_path)
        prediction_img.savefig("rand_pred.jpg")
    except Exception as e:
        return jsonify({'message': 'Server could not save predicted images'}), 700
    
    try:
        return send_file("rand_pred.jpg", mimetype='image/jpeg')
    except Exception as e:
        return jsonify({'message': 'Server could not send file'}), 800 


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