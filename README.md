# Day simulation using automata theory

### States
Day has following states:
* START - responsible for starting simulation
* SLEEP - state responsible for sleeping
* EAT - state responsible for eating
* STUDY - state responsible for studing
* WALK - state responsible for walking in the park
* CENTER - state responsoble for going to center
* SHOP - state responsible for shopping
* VIDEO - state responsible for watching videos

### Simulation
Automata starts from state START which is our starting point. It inevitably will get to sleep state( some activities is possible because of random event ). Sleep will have from 5 - 10 hours, depending on random. Than after waking up automata will get in EAT state, from which it can go almost anywhere, depending on random.

### Extra variables
There are three extra variables which influence on decisions:
* sleepy - stands for willingness to sleep
* hungry - stands for willingness to eat
* exhausted - stands for willingness to have a rest

### Graph
![image](https://github.com/maksDev123/automata/assets/116755445/ef0a887f-b106-44d1-bac7-1e2994d3991c)

### Result
![image](https://github.com/maksDev123/automata/assets/116755445/100af3d4-31da-40b4-81e1-c4c3a3dfc2cf)
