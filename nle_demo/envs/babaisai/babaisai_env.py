from pathlib import Path
from typing import Optional

from baba import make
from balrog_demo.envs.babaisai.wrapper import BabaIsAIWrapper
from nle_utils.wrappers import GymV21CompatibilityV0, NLEDemo


def make_babaisai_env(env_name, cfg, env_config, render_mode: Optional[str] = None):
    env_kwargs = dict(add_ruleset=cfg.add_ruleset)
    env = make(env_name, **env_kwargs)
    env = BabaIsAIWrapper(env)
    savedir = Path(cfg.demodir) / env_name
    env = GymV21CompatibilityV0(env=env, render_mode=render_mode)
    env = NLEDemo(env, savedir, f"seed_{cfg.seed}", save_every_k=cfg.save_every_k)

    return env
