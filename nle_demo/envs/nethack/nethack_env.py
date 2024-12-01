from pathlib import Path
from typing import Optional

import gym
import nle  # NOQA: F401
from balrog_demo.envs.nethack.wrapper import NLEWrapper
from nle_utils.wrappers import (
    FinalStatsWrapper,
    GymV21CompatibilityV0,
    NLEDemo,
    NLETimeLimit,
    TaskRewardsInfoWrapper,
    TtyrecInfoWrapper,
)

NETHACK_ENVS = []
for env_spec in gym.envs.registry.all():
    id = env_spec.id
    if "NetHack" in id:
        NETHACK_ENVS.append(id)


def make_nethack_env(env_name, cfg, env_config, render_mode: Optional[str] = None):
    observation_keys = (
        "message",
        "blstats",
        "tty_chars",
        "tty_colors",
        "tty_cursor",
        # ALSO AVAILABLE (OFF for speed)
        # "specials",
        # "colors",
        # "chars",
        "glyphs",
        "inv_glyphs",
        "inv_strs",
        "inv_letters",
        "inv_oclasses",
    )

    kwargs = dict(
        observation_keys=observation_keys,
        character=cfg.character,
        penalty_step=cfg.penalty_step,
        penalty_time=cfg.penalty_time,
        penalty_mode=cfg.fn_penalty_step,
        savedir=cfg.savedir,
        save_ttyrec_every=cfg.save_ttyrec_every,
    )

    if cfg.max_episode_steps is not None:
        kwargs["max_episode_steps"] = cfg.max_episode_steps

    env = gym.make(env_name, **kwargs)
    env = NLEWrapper(env)

    # wrap NLE with timeout
    env = NLETimeLimit(env)

    env = TaskRewardsInfoWrapper(env, done_only=False)
    env = FinalStatsWrapper(env, done_only=False)
    env = TtyrecInfoWrapper(env, done_only=False)
    env = GymV21CompatibilityV0(env=env, render_mode=render_mode)

    savedir = Path(cfg.demodir) / env_name
    game_name = f"seed_{cfg.seed}"
    paths = [path.stem for path in savedir.iterdir() if game_name in path.stem]
    if paths:
        game_name = paths[0]
    env = NLEDemo(env, savedir, game_name, save_every_k=cfg.save_every_k)

    return env
