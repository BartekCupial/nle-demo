from pathlib import Path
from typing import Optional

from nle_utils.wrappers import NLEDemo

from nle_demo.envs.textworld import global_textworld_context
from nle_demo.envs.textworld.wrappers import GymV21CompatibilityV0, TextWorldWrapper


def make_textworld_env(env_name, cfg, env_config, render_mode: Optional[str] = None):
    textworold_context = global_textworld_context(cfg)

    env = textworold_context(env_name)
    env = TextWorldWrapper(env)
    savedir = Path(cfg.demodir) / env_name
    env = NLEDemo(env, savedir, f"seed_{cfg.seed}", save_every_k=cfg.save_every_k)
    env = GymV21CompatibilityV0(env=env)

    if render_mode:
        env.render_mode = render_mode

    return env
