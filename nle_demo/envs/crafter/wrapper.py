import random
from typing import Any, Tuple

import gym
import pygame

# from gym.utils.play import display_arr


class CrafterWrapper(gym.Wrapper):
    def __init__(self, env: gym.Env):
        super().__init__(env)
        # dummy spaces
        self.observation_space = gym.spaces.Discrete(1)
        self.action_space = gym.spaces.Discrete(1)
        self.current_seed = None

        self.screen = None
        self.clock = pygame.time.Clock()
        self.fps = 30

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
            rendered = self.env.render()

            if self.screen is None:
                self.screen = pygame.display.set_mode(rendered.shape[:2])

            display_arr(self.screen, rendered, video_size=rendered.shape[:2], transpose=False)

            pygame.display.flip()
            self.clock.tick(self.fps)

    def close(self):
        if self.screen is not None:
            pygame.quit()
            self.screen = None

        return super().close()


def display_arr(screen, arr, video_size, transpose=True):
    # Create a surface that supports alpha
    surface = pygame.Surface(video_size, pygame.SRCALPHA)

    if transpose:
        arr = arr.swapaxes(0, 1)

    # Convert RGBA array to surface using pixel-by-pixel copying
    pygame_surface_array = pygame.surfarray.pixels3d(surface)
    pygame_surface_array[:, :, :3] = arr[:, :, :3]
    del pygame_surface_array  # Release the surface lock

    # Handle alpha channel separately
    if arr.shape[2] == 4:
        alpha_surface = pygame.surfarray.pixels_alpha(surface)
        alpha_surface[:] = arr[:, :, 3]
        del alpha_surface

    screen.blit(surface, (0, 0))
