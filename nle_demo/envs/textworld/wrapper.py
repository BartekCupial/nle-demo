from typing import Any, Tuple

import gym


class TextWorldWrapper(gym.Wrapper):
    def __init__(self, env: gym.Env):
        super().__init__(env)
        # dummy spaces
        self.observation_space = gym.spaces.Discrete(1)
        self.action_space = gym.spaces.Discrete(1)
        self.current_seed = None

    @property
    def unwrapped(self):
        return self

    def get_seeds(self):
        return self.current_seed

    def seed(self, seed):
        self.current_seed = seed
        return super().seed(seed=seed)

    def reset(self, **kwargs) -> Any | tuple[Any, dict]:
        obs, infos = super().reset(**kwargs)
        return obs

    def step(self, action: Any) -> Tuple[Any, float, bool, dict]:
        return super().step(action)
