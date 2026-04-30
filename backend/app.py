from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection using environment variable
mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017/")

client = MongoClient(mongo_url)
db = client["mydatabase"]
collection = db["users"]

@app.route('/')
def home():
    return jsonify({"message": "Backend is running!"})

@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return jsonify({"users": users})

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json

    user = {
        "name": data.get("name"),
        "age": data.get("age")
    }

    collection.insert_one(user)
    return jsonify({"message": "User added successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)