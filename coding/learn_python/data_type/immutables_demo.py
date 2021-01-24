# -*- coding: utf-8 -*-
import immutables

map = immutables.Map(a=1, b=2)

print(map['hardware'])

print(map.get('z', 100))

print('z' in map)

map2 = map.set('hardware', 10)
print(map, map2)

map3 = map2.delete('b')
print(map, map2, map3)

map_mutation = map.mutate()
map_mutation['hardware'] = 100
del map_mutation['b']
map_mutation.set('y', 'y')

map4 = map_mutation.finish()

print(map, map4)

with map.mutate() as mm:
    mm['hardware'] = 100
    del mm['b']
    mm.set('y', 'y')
    map5 = mm.finish()

print(map, map5)
