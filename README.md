# REDIS

This repository is about REDIS.

Created by: Gustavo Vinicius de Morais

### Python Docker
```
docker-compose up -d --build
docker exec -it -u 0 python sh
python app.py

GET http://localhost/users

POST http://localhost/users
{
    "key":"user2",
    "value": "asfasdf"
}

```

### Redis Commands
```

redis-cli # access redis database

SET user gustavo # build a string key 'user' with value 'gustavo'

GET user # get the value of the key user

MSET user1 gustavo email1 gustavo@email.com # build many pairs of key value [key value]

MGET user1 email1 # get the values of multiple keys by once

DEL user # delete key

keys * # show all the keys

type user1 # shows the type of the value of the key

DUMP email1 # dumps a serialized value of some key

RESTORE test1 0 "\x00\x11gustavo@email.com\n\x00@\xe8\xa9\x14\x04\xab\x8b\xe2" # restore the serialized value to some key, with no expiration time [0]

EXISTS user1 # verify if some key exists, returns 1 for true and 0 for false

RENAME user1 user2 # renames a key to another name

SCAN 0 # show the keys, the 0 number is a cursor ID

SCAN 0 MATCH *us* COUNT 10 # brings 10 keys with the 'us' letters

OBJECT REFCOUNT user1 # return the qty of references of the pattern

OBJECT ENCODING user1 # encoding representation of the key value

OBJECT IDLETIME user1 # returns the amount of seconds that the object is without beeing called

```