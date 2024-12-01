import pprint

from balrog_demo.cfg.cfg import add_extra_params_demo
from balrog_demo.envs.nethack.nethack_env import NETHACK_ENVS, make_nethack_env
from nle_utils.cfg.arguments import parse_args, parse_full_cfg
from nle_utils.envs.env_utils import register_env
from nle_utils.envs.nethack.nethack_params import add_extra_params_nethack_env
from nle_utils.play import play
from nle_utils.scripts.play_nethack import get_action


def register_nethack_envs():
    for env_name in NETHACK_ENVS:
        register_env(env_name, make_nethack_env)


def register_nethack_components():
    register_nethack_envs()


def parse_nethack_args(argv=None):
    parser, partial_cfg = parse_args(argv=argv)
    add_extra_params_nethack_env(parser)
    add_extra_params_demo(parser)
    final_cfg = parse_full_cfg(parser, argv)
    return final_cfg


def main():
    register_nethack_components()
    cfg = parse_nethack_args()
    info = play(cfg, get_action=get_action)
    pprint.pprint(info)


if __name__ == "__main__":
    main()
