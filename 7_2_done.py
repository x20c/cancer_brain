from flask import Flask, jsonify, request

# Create a Flask application instance

app = Flask(__name__)

request_count = 0


@app.route('/count-requests', methods=['GET'])
def count_requests():
    global request_count
    request_count += 1
    return jsonify({'request_count': request_count})


@app.route('/reset-counter', methods=['POST'])
def reset_requests():
    global request_count
    request_count = 0
    return jsonify({'message': 'Counter reset successfully', 'request_count': request_count})


if __name__ == '__main__':
    app.run(debug=True)