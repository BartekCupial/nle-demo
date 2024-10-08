import random
from typing import Any, Tuple

import gym
import pygame
from gym.utils.play import display_arr


class BabaIsAIWrapper(gym.Wrapper):
    def __init__(self, env: gym.Env):
        super().__init__(env)
        # dummy spaces
        self.observation_space = gym.spaces.Discrete(1)
        self.action_space = gym.spaces.Discrete(1)
        self.current_seed = None

        self.video_size = None
        self.screen = None
        self.clock = pygame.time.Clock()
        self.fps = 30

    @property
    def unwrapped(self):
        return self

    def seed(self, seed):
        self.current_seed = seed
        return super().seed(seed=seed)

    def get_seeds(self):
        return self.current_seed

    def reset(self, **kwargs) -> Any | tuple[Any, dict]:
        obs = super().reset(**kwargs)
        return obs

    def step(self, action: Any) -> Tuple[Any, float, bool, dict]:
        obs, reward, done, info = super().step(action)
        if done:
            print(reward)

        return obs, reward, done, info

    def render(self, mode="human", **kwargs):
        if mode is not None:
            rendered = self.env.render(mode="rgb_array")

            if self.video_size is None:
                self.video_size = [rendered.shape[1], rendered.shape[0]]

            if self.screen is None:
                self.screen = pygame.display.set_mode(self.video_size)

            display_arr(self.screen, rendered, transpose=True, video_size=self.video_size)

            pygame.display.flip()
            self.clock.tick(self.fps)

    def close(self):
        if self.screen is not None:
            pygame.quit()
            self.screen = None

        return super().close()
