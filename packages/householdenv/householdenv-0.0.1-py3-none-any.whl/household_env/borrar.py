import json
from collections import namedtuple
from enum import Enum
from household_env.envs.house_env import Tasks

import numpy as np

Rewards = namedtuple('Rewards', ['bump_into_wall',
                                 'walking',
                                 'turn_on_tv'])
Reward = Rewards(-1, -0.01, 10)

print(Reward.bump_into_wall)

print(Tasks.to_binary_list(6))
print(Tasks.to_binary_list(2))
print(Tasks.to_binary_list(1))
print(Tasks.to_binary_list(10))
print(Tasks.to_dec(Tasks.to_binary_list(10)))

print(Tasks.to_dec([0, 0, 1, 1, 0]) == Tasks.TURN_ON_TV.value)
print(Tasks.to_dec([0, 0, 1, 1, 0]) == Tasks.TURN_ON_DISHWASHER.value)

isinstance(Tasks.TURN_ON_DISHWASHER, Tasks)


with open('operability.json') as json_file:
    aux = json.load(json_file)
operability = {}
for key in aux.keys():
    operability[key] = [tuple(i) for i in aux[key]]
