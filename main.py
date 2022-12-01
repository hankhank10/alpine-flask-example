from flask import Flask, render_template, request, redirect, url_for, jsonify
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def api():

    # For demonstration purposes we will have the server return a simulated failure 70% of the time
    pct_chance_of_simulated_failure = 70
    if random.randint(0, 100) < pct_chance_of_simulated_failure:
        return jsonify({'success': False, 'message': 'Simulated failure'}), 500

    # Try to get the data from the request, and if successful print it to the console and return a success message
    try:
        data = request.get_json()
        print("Array received successfully: ", data)
        return jsonify(data), 200

    # If the request fails, print the error to the console and return an error message
    except:
        print ("Error: JSON could not be parsed")
        return jsonify({'error': 'Invalid request'}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)