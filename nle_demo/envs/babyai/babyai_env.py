from pathlib import Path
from typing import Optional

import gymnasium as gym
import minigrid
from nle_utils.wrappers import NLEDemo

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
for env_spec in gym.envs.registry:
    id = env_spec
    if id.split("-")[0] == "BabyAI":
        if id not in broken_bonus_envs:
            BABYAI_ENVS.append(id)

BABYAI_ENVS += [
    "BabyAI-MixedTrainLocal-v0/goto",
    "BabyAI-MixedTrainLocal-v0/pickup",
    "BabyAI-MixedTrainLocal-v0/open",
    "BabyAI-MixedTrainLocal-v0/putnext",
    "BabyAI-MixedTrainLocal-v0/pick_up_seq_go_to",
]


def make_babyai_env(env_name, cfg, env_config, render_mode: Optional[str] = None):
    if env_name.startswith("BabyAI-MixedTrainLocal-v0/"):
        base_task, goal = env_name.split("/")
        while 1:
            env = gym.make(base_task, render_mode=render_mode)
            if env.unwrapped.action_kinds[0].replace(" ", "_") == goal:
                break

    env = BabyAIWrapper(env)
    savedir = Path(cfg.demodir) / env_name
    env = NLEDemo(env, savedir, f"seed_{cfg.seed}", save_every_k=cfg.save_every_k)

    return env
