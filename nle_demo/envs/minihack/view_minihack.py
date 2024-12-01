import pprint

from balrog_demo.cfg.cfg import add_extra_params_demo
from balrog_demo.envs.minihack.minihack_env import MINIHACK_ENVS, make_minihack_env
from balrog_demo.view_demo import view_demo
from nle_utils.cfg.arguments import parse_args, parse_full_cfg
from nle_utils.envs.env_utils import register_env
from nle_utils.envs.minihack.minihack_params import add_extra_params_minihack_env


def register_minihack_envs():
    for env_name in MINIHACK_ENVS:
        register_env(env_name, make_minihack_env)


def register_minihack_components():
    register_minihack_envs()


def parse_minihack_args(argv=None):
    parser, partial_cfg = parse_args(argv=argv)
    add_extra_params_minihack_env(parser)
    add_extra_params_demo(parser)
    final_cfg = parse_full_cfg(parser, argv)
    return final_cfg


def main():
    register_minihack_components()
    cfg = parse_minihack_args()
    info = view_demo(cfg)
    pprint.pprint(info)


if __name__ == "__main__":
    main()
