from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def api():

    # Try to get the data from the request, and if successful print it to the console and return a success message
    try:
        data = request.get_json()
        print("Array received: ", data)
        return jsonify(data), 200

    # If the request fails, print the error to the console and return an error message
    except:
        print ("Error: JSON could not be parsed")
        return jsonify({'error': 'Invalid request'}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)