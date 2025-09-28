from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Data retrieved successfully!'})

if __name__ == '__main__':
    app.run(debug=True)