import pickle
import random
import timeit

import numpy as np
from nle_utils.envs.create_env import create_env
from nle_utils.utils.attr_dict import AttrDict


def view_demo(cfg):
    render_mode = "human"
    if cfg.no_render:
        render_mode = None

    env = create_env(
        cfg.env,
        cfg=cfg,
        env_config=AttrDict(worker_index=0, vector_index=0, env_id=0),
        render_mode=render_mode,
    )

    if cfg.seed is not None:
        np.random.seed(cfg.seed)
        random.seed(cfg.seed)
    obs, info = env.reset(seed=cfg.seed)

    steps = 0
    reward = 0.0
    total_reward = 0.0

    total_start_time = timeit.default_timer()
    start_time = total_start_time

    with open(env.game_path, "rb") as f:
        data = pickle.load(f)

    recorded_actions = data["actions"]
    recorded_rewards = data["rewards"]

    for i, (recorded_action, recorded_reward) in enumerate(zip(recorded_actions, recorded_rewards)):
        obs, reward, terminated, truncated, info = env.step(recorded_action)
        # assert reward == recorded_reward
        steps += 1
        total_reward += reward

        if not (terminated or truncated):
            continue

        time_delta = timeit.default_timer() - start_time

        if cfg.verbose:
            print("Final reward:", reward)
            print("End status:", info.get("end_status", ""))
            print(f"Total reward: {total_reward}, Steps: {steps}, SPS: {steps / time_delta}", total_reward)

        break

    # do not close, we could overwrite the demo file
    # env.close()

    return info
