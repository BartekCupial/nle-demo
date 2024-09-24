from pathlib import Path
from typing import Optional

import babyai
import gym
from nle_utils.wrappers import GymV21CompatibilityV0, NLEDemo

from nle_demo.envs.babyai.wrapper import BabyAIWrapper

# see discussion starting here: https://github.com/Farama-Foundation/Minigrid/pull/381#issuecomment-1646800992
broken_bonus_envs = {
    "BabyAI-PutNextS5N2Carrying-v0",
    "BabyAI-PutNextS6N3Carrying-v0",
    "BabyAI-PutNextS7N4Carrying-v0",
    "BabyAI-KeyInBox-v0",
}


# get all babyai envs (except the broken ones)
BABYAI_ENVS = []
for env_spec in gym.envs.registry.all():
    id = env_spec.id
    if id.split("-")[0] == "BabyAI":
        if id not in broken_bonus_envs:
            BABYAI_ENVS.append(id)


def make_babyai_env(env_name, cfg, env_config, render_mode: Optional[str] = None):
    env = gym.make(env_name)
    env = BabyAIWrapper(env)
    savedir = Path(cfg.demodir) / env_name
    env = NLEDemo(env, savedir, f"seed_{cfg.seed}", save_every_k=cfg.save_every_k)
    env = GymV21CompatibilityV0(env=env)

    if render_mode:
        env.render_mode = render_mode

    return env
