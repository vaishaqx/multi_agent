from flask import Flask, render_template, request, jsonify
from agents.main_agent import handle_query

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = handle_query(user_input)
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(debug=True)