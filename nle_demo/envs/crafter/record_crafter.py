import pygame
from nle_utils.cfg.arguments import parse_args, parse_full_cfg
from nle_utils.envs.env_utils import register_env
from nle_utils.play import play

from nle_demo.cfg.cfg import add_extra_params_demo
from nle_demo.envs.crafter.crafter_env import make_crafter_env
from nle_demo.envs.crafter.crafter_params import add_extra_params_crafter_env


def register_crafter_envs():
    register_env("default", make_crafter_env)


def register_crafter_components():
    register_crafter_envs()


def parse_crafter_args(argv=None):
    parser, partial_cfg = parse_args(argv=argv)
    add_extra_params_crafter_env(parser)
    add_extra_params_demo(parser)
    final_cfg = parse_full_cfg(parser, argv)
    return final_cfg


keys_to_action = {
    (pygame.K_a,): "move_left",
    (pygame.K_d,): "move_right",
    (pygame.K_w,): "move_up",
    (pygame.K_s,): "move_down",
    (pygame.K_SPACE,): "do",
    (pygame.K_TAB,): "sleep",
    (pygame.K_r,): "place_stone",
    (pygame.K_t,): "place_table",
    (pygame.K_f,): "place_furnace",
    (pygame.K_p,): "place_plant",
    (pygame.K_1,): "make_wood_pickaxe",
    (pygame.K_2,): "make_stone_pickaxe",
    (pygame.K_3,): "make_iron_pickaxe",
    (pygame.K_4,): "make_wood_sword",
    (pygame.K_5,): "make_stone_sword",
    (pygame.K_6,): "make_iron_sword",
}


def get_action(env, play_mode, obs):
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
            return env.action_names.index(action)

        env.render()


def main():
    print("Actions:")
    for key, action in keys_to_action.items():
        print(f"  {pygame.key.name(key[0])}: {action}")

    register_crafter_components()
    cfg = parse_crafter_args()
    play(cfg, get_action=get_action)


if __name__ == "__main__":
    main()
