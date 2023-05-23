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
* RAIN - state responsible for rain
* CALL - state responsible for sudden work call
* ALARM - state responsible for air alarm

### Simulation
Automata starts from state START which is our starting point. It inevitably will get to sleep state( some activities is possible because of random event ). Sleep will have from 5 - 10 hours, depending on random. Than after waking up automata will get in EAT state, from which it can go almost anywhere, depending on random factor and exrta variables.

### Extra variables
There are three extra variables which influence on decisions:
* sleepy - stands for willingness to sleep
* hungry - stands for willingness to eat
* exhausted - stands for willingness to have a rest

### Graph
![image](https://github.com/maksDev123/automata/assets/116755445/0c2ad60a-6a18-4311-b46f-dd9519115a1c)

### Result
![image](https://github.com/maksDev123/automata/assets/116755445/a4b37602-3ecb-4f2a-a63d-725439d5bc1d)

