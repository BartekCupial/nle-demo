import random
from typing import Any, Tuple

import gym
import pygame
from gym.utils.play import display_arr


class CrafterWrapper(gym.Wrapper):
    def __init__(self, env: gym.Env, video_size=None):
        super().__init__(env)
        # dummy spaces
        self.observation_space = gym.spaces.Discrete(1)
        self.action_space = gym.spaces.Discrete(1)
        self.current_seed = None

        self.video_size = video_size
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
        self.achievements = set()
        print("Diamonds exist:", self.env._world.count("diamond"))
        return super().reset(**kwargs)

    def step(self, action: Any) -> Tuple[Any | float | bool | dict]:
        obs, reward, done, info = super().step(action)

        # Achievements.
        unlocked = {
            name for name, count in self.env._player.achievements.items() if count > 0 and name not in self.achievements
        }
        for name in unlocked:
            self.achievements |= unlocked
            total = len(self.env._player.achievements.keys())
            print(f"Achievement ({len(self.achievements)}/{total}): {name}")
            if self.env._step > 0 and self.env._step % 100 == 0:
                print(f"Time step: {self.env._step}")
            if reward:
                print(f"Reward: {reward}")

        return obs, reward, done, info

    def render(self, mode="human", **kwargs):
        if mode is not None:
            rendered = self.env.render(self.video_size)

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
