from pathlib import Path
from typing import Optional

from nle.env.tasks import (
    NetHackChallenge,
    NetHackEat,
    NetHackGold,
    NetHackOracle,
    NetHackScore,
    NetHackScout,
    NetHackStaircase,
    NetHackStaircasePet,
)
from nle_utils.wrappers import (
    FinalStatsWrapper,
    GymV21CompatibilityV0,
    NLEDemo,
    NLETimeLimit,
    TaskRewardsInfoWrapper,
    TtyrecInfoWrapper,
)

NETHACK_ENVS = {
    "NetHackStaircase-v0": NetHackStaircase,
    "NetHackScore-v0": NetHackScore,
    "NetHackStaircasePet-v0": NetHackStaircasePet,
    "NetHackOracle-v0": NetHackOracle,
    "NetHackGold-v0": NetHackGold,
    "NetHackEat-v0": NetHackEat,
    "NetHackScout-v0": NetHackScout,
    "NetHackChallenge-v0": NetHackChallenge,
}


def nethack_env_by_name(name):
    if name in NETHACK_ENVS.keys():
        return NETHACK_ENVS[name]
    raise Exception("Unknown NetHack env")


def make_nethack_env(env_name, cfg, env_config, render_mode: Optional[str] = None):
    env_class = nethack_env_by_name(env_name)

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

    env = env_class(**kwargs)

    # wrap NLE with timeout
    env = NLETimeLimit(env)

    env = TaskRewardsInfoWrapper(env, done_only=False)
    env = FinalStatsWrapper(env, done_only=False)
    env = TtyrecInfoWrapper(env, done_only=False)
    savedir = Path(cfg.demodir) / env_name
    game_name = f"seed_{cfg.seed}"
    paths = [path.stem for path in savedir.iterdir() if game_name in path.stem]
    if paths:
        game_name = paths[0]
    env = NLEDemo(env, savedir, game_name, save_every_k=cfg.save_every_k)

    env = GymV21CompatibilityV0(env=env)

    if render_mode:
        env.render_mode = render_mode

    return env
