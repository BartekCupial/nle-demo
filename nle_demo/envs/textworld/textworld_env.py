from pathlib import Path
from typing import Optional

from balrog_demo.envs.textworld import global_textworld_context
from balrog_demo.envs.textworld.wrapper import TextWorldWrapper
from nle_utils.wrappers import GymV21CompatibilityV0, NLEDemo


def make_textworld_env(env_name, cfg, env_config, render_mode: Optional[str] = None):
    textworold_context = global_textworld_context(cfg)

    env = textworold_context(env_name, seed=cfg.seed)
    env = TextWorldWrapper(env)
    savedir = Path(cfg.demodir) / env_name
    env = GymV21CompatibilityV0(env=env, render_mode=render_mode)
    env = NLEDemo(env, savedir, f"seed_{cfg.seed}", save_every_k=cfg.save_every_k)

    return env
