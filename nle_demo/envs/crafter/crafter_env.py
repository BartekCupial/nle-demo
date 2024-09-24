from pathlib import Path
from typing import Optional

import crafter
import gym
from nle_utils.wrappers import GymV21CompatibilityV0, NLEDemo

from nle_demo.envs.crafter.wrapper import CrafterWrapper


def make_crafter_env(env_name, cfg, env_config, render_mode: Optional[str] = None):
    crafter.constants.items["health"]["max"] = cfg.health
    crafter.constants.items["health"]["initial"] = cfg.health

    size = list(cfg.size)
    size[0] = size[0] or cfg.window[0]
    size[1] = size[1] or cfg.window[1]

    env = crafter.Env(area=cfg.area, view=cfg.view, length=cfg.length, seed=cfg.seed)
    env = CrafterWrapper(env, size)
    savedir = Path(cfg.demodir) / env_name
    env = NLEDemo(env, savedir, f"seed_{cfg.seed}", save_every_k=cfg.save_every_k)
    env = GymV21CompatibilityV0(env=env)

    if render_mode:
        env.render_mode = render_mode

    return env
