# Gymgrid

The gridworld environment contains simple environments in RL book and compatible with OpenAI-gym.

## Installation

```
pip install gymgird
```

## Usage

```
import gym
import gymgrid
env = env = gym.make('cliff-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
print("env closed")
```

## Environments

- Sample1
- Sample2
- Cliff: Example 6.5: Cliff Walking
- WindyGridWorld: Exercise 6.9 Windy Gridworld with King's Moves