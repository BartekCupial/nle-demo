from pathlib import Path
from typing import Optional

import crafter
import gym
from nle_utils.wrappers import GymV21CompatibilityV0, NLEDemo

from nle_demo.envs.crafter.wrapper import CrafterWrapper


def make_crafter_env(env_name, cfg, env_config, render_mode: Optional[str] = None):
    crafter.constants.items["health"]["max"] = cfg.health
    crafter.constants.items["health"]["initial"] = cfg.health

    env = crafter.Env(area=cfg.area, view=cfg.view, length=cfg.length, size=cfg.size, seed=cfg.seed)
    env = CrafterWrapper(env)
    savedir = Path(cfg.demodir) / env_name
    env = GymV21CompatibilityV0(env=env, render_mode=render_mode)
    env = NLEDemo(env, savedir, f"seed_{cfg.seed}", save_every_k=cfg.save_every_k)

    return env
