from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from bson import ObjectId
import uuid
import hashlib
import json

app = Flask(__name__)

# MongoDB Configuration (change if needed)
app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"
mongo = PyMongo(app)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API route - reads JSON data
@app.route('/api')
def api_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

# To-Do form route
@app.route('/todo')
def todo_page():
    return render_template('todo.html')

# Backend route for submitting To-Do items
@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.get_json()
    itemName = data.get('itemName')
    itemDescription = data.get('itemDescription')
    mongo.db.todos.insert_one({
        "itemName": itemName,
        "itemDescription": itemDescription
    })
    return jsonify({"status": "success", "message": "To-Do Item Added"})

if __name__ == '__main__':
    app.run(debug=True)
