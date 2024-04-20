from mss import mss
import pydirectinput
import cv2
import numpy as np
import pytesseract
from matplotlib import pyplot as plt
import time
from gym import Env
from gym.spaces import Box,Discrete




class Webgame(Env):
  
    def __init__(self):
        
        super().__init__()
        self.observation_space = Box(low=0, high=255,shape=(1,83,100), dtype=np.uint8)
        self.action_space = Discrete(3)
        pass
    def step(self,action):
        pass
    def render(self):
        pass
    def reset(self):
        pass
    def close(self):
        pass
    def get_observation(self):
        pass
    
    def set_done(self):
        pass
    
    
env = Webgame()
env.action_space.sample()
plt.imshow(env.observation_space.sample()[0])