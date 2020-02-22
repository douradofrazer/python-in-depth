# Keys in dictionaries have to be immutable
# hence we can't use something like a list but we can use a tuple
# the values can be of any data type, even another dictionary itself
bike = {"make": "Honda", "model": "250 dream", "color": "red", "engine_size": 250}
print(bike["engine_size"])
print(bike["color"])
