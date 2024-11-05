import pprint

import pygame
from nle_utils.cfg.arguments import parse_args, parse_full_cfg
from nle_utils.envs.env_utils import register_env
from nle_utils.play import play

from nle_demo.cfg.cfg import add_extra_params_demo
from nle_demo.envs.babyai.babyai_env import BABYAI_ENVS, make_babyai_env
from nle_demo.envs.babyai.babyai_params import add_extra_params_babyai_env


def register_babyai_envs():
    for env_name in BABYAI_ENVS:
        register_env(env_name, make_babyai_env)


def register_babyai_components():
    register_babyai_envs()


def parse_babyai_args(argv=None):
    parser, partial_cfg = parse_args(argv=argv)
    add_extra_params_babyai_env(parser)
    add_extra_params_demo(parser)
    final_cfg = parse_full_cfg(parser, argv)
    return final_cfg


def get_action(env, play_mode, obs):
    keys_to_action = {
        (pygame.K_UP,): env.unwrapped.actions.forward,
        (pygame.K_LEFT,): env.unwrapped.actions.left,
        (pygame.K_RIGHT,): env.unwrapped.actions.right,
        (pygame.K_SPACE,): env.unwrapped.actions.toggle,
        (pygame.K_COMMA,): env.unwrapped.actions.pickup,
        (pygame.K_d,): env.unwrapped.actions.drop,
        (pygame.K_SEMICOLON,): env.unwrapped.actions.done,
    }
    relevant_keys = set(sum(map(list, keys_to_action.keys()), []))
    pressed_keys = []

    while True:
        # process pygame events
        for event in pygame.event.get():
            # test events, set key states
            if event.type == pygame.KEYDOWN:
                if event.key in relevant_keys:
                    pressed_keys.append(event.key)
            elif event.type == pygame.QUIT:
                return None

        action = keys_to_action.get(tuple(sorted(pressed_keys)), None)  # TODO: was 0
        pressed_keys = []

        if action is not None:
            return action

        env.render()


def main():
    register_babyai_components()
    cfg = parse_babyai_args()
    info = play(cfg, get_action=get_action)
    pprint.pprint(info)


if __name__ == "__main__":
    main()
