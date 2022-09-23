# REDIS

This repository is about REDIS.

Created by: Gustavo Vinicius de Morais

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

```