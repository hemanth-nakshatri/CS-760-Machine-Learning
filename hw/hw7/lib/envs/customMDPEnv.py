import numpy as np
import gym
from gym import spaces

class CustomMDPEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    name = "CustomMDP"

    def __init__(self):
        super(CustomMDPEnv, self).__init__()
        # Define the action and observation space
        # Two states: A (0) and B (1)
        self.observation_space = spaces.Discrete(2)
        # Two actions: move (0) and stay (1)
        self.action_space = spaces.Discrete(2)
        # Start in state A
        self.state = 0

    def step(self, action):
        # Implement the MDP's dynamics
        if action == 0:  # move
            self.state = 1 if self.state == 0 else 0
            reward = 0
        elif action == 1:  # stay
            reward = 1
        else:
            raise ValueError("Invalid action")

        # This MDP does not have a natural episode end
        done = False

        return self.state, reward, done, {}

    def reset(self):
        # Reset the state to A
        self.state = 0
        return self.state

    def render(self, mode='human', close=False):
        print(f"Current State: {'A' if self.state == 0 else 'B'}")
