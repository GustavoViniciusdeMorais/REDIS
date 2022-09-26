from pickle import FALSE
from flask import Flask, request, jsonify
import redis

model = None
app = Flask(__name__)

redis = redis.Redis(
     host= 'redis',
     port= '6379')

@app.route('/')
def home_endpoint():
    return 'Test ssss!'

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()  # Get data posted as a json
    if 'key' in data:
        key = data['key']
        value = data['value']
        redis.set(key,value)
        return jsonify(key,value)
    
    return FALSE

@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for k in redis.keys('*'):
        redis_keys = []
        redis_keys.append(redis.get(k))
        user = '\n'.join(key.decode('utf-8', 'ignore') for key in redis_keys)
        users.append([k.decode("utf-8"),user])
    
    return users

if __name__ == '__main__':
    # app.run(host="0.0.0.0", debug=True)
    app.run(host='0.0.0.0', port=8000, debug=True)