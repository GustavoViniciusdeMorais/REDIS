from pickle import FALSE
from flask import Flask, request, jsonify
import redis
import json

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

'''
    GET user by id
    SET user cache after first route execution
    CACHE EXAMPLE
'''
@app.route('/users/<id>', methods=['GET'])
def get_user_by_id(id):
    cache_string = 'cache:user'
    cache_user = redis.get(cache_string)

    if cache_user == None:
        key = 'user' + str(id)
        user = redis.get(key)
        redis.set(cache_string,user)
        redis.expire(cache_string,5) # set a five seconds cache expire time
        data = {}
        data['user'] = user.decode('utf-8', 'ignore')
        return jsonify(str(data))
    else:
        userc = redis.get(cache_string)
        data = {}
        data['user cache'] = userc.decode('utf-8', 'ignore')
        return jsonify(str(data))

if __name__ == '__main__':
    # app.run(host="0.0.0.0", debug=True)
    app.run(host='0.0.0.0', port=8000, debug=True)