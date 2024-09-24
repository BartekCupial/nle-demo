import random
from typing import Any, Tuple

import gym
import pygame
from gym.utils.play import display_arr


class BabyAIWrapper(gym.Wrapper):
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

    def get_seeds(self):
        return self.current_seed

    def seed(self, seed):
        self.current_seed = seed
        return super().seed(seed=seed)

    def reset(self, **kwargs) -> Any | Tuple[Any | dict]:
        obs, descriptions = super().reset(**kwargs)
        print(obs["mission"])

        return obs

    def render(self, mode="human", **kwargs):
        if mode is not None:
            rendered = self.env.render(mode="rgb_array")

            if self.video_size is None:
                video_size = [rendered.shape[1], rendered.shape[0]]

            if self.screen is None:
                self.screen = pygame.display.set_mode(video_size)

            display_arr(self.screen, rendered, transpose=True, video_size=video_size)

            pygame.display.flip()
            self.clock.tick(self.fps)

    def close(self):
        if self.screen is not None:
            pygame.quit()
            self.screen = None

        return super().close()
