import pprint

from balrog_demo.cfg.cfg import add_extra_params_demo
from balrog_demo.envs.textworld import global_textworld_context
from balrog_demo.envs.textworld.textworld_env import make_textworld_env
from balrog_demo.envs.textworld.textworld_params import add_extra_params_textworld_env
from nle_utils.cfg.arguments import parse_args, parse_full_cfg
from nle_utils.envs.env_utils import register_env
from nle_utils.play import play


def register_textworld_envs(cfg):
    textworold_context = global_textworld_context(cfg)

    for env_name in textworold_context.env_ids.keys():
        register_env(env_name, make_textworld_env)


def register_textworld_components(cfg):
    register_textworld_envs(cfg)


def parse_textworld_args(argv=None):
    parser, partial_cfg = parse_args(argv=argv)
    add_extra_params_textworld_env(parser)
    add_extra_params_demo(parser)
    final_cfg = parse_full_cfg(parser, argv)
    return final_cfg


def get_action(env, mode, typing):
    command = input("> ")
    return command


def main():
    cfg = parse_textworld_args()
    register_textworld_components(cfg)
    info = play(cfg, get_action=get_action)
    pprint.pprint(info)


if __name__ == "__main__":
    main()
