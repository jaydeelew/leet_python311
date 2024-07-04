from collections import namedtuple

thing = namedtuple("thing", "color size shape")

my_thing = thing("red", "small", "sphere")

print(my_thing)
print(my_thing.shape)
