from typing import Any, Tuple

import gymnasium as gym


class BabyAIWrapper(gym.Wrapper):
    def __init__(self, env: gym.Env):
        super().__init__(env)
        # # dummy spaces
        self.observation_space = gym.spaces.Discrete(1)
        self.action_space = gym.spaces.Discrete(1)
        self.current_seed = None

    def get_seeds(self):
        return self.current_seed

    def seed(self, seed):
        self.current_seed = seed
        return super().seed(seed=seed)

    def reset(self, **kwargs) -> Any | Tuple[Any | dict]:
        obs, info = super().reset(**kwargs)
        print(obs["mission"])
        print(info["descriptions"])

        return obs, info

    def step(self, action: Any) -> Tuple[Any | float | bool | dict]:
        obs, reward, terminated, truncated, info = super().step(action)
        done = terminated or truncated
        print(info["descriptions"])

        if done:
            print(f"reward: {reward}")

        return obs, reward, terminated, truncated, info
