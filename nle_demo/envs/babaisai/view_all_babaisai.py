import pprint
import sys

from nle_utils.cfg.arguments import parse_args, parse_full_cfg
from nle_utils.utils.context import global_env_registry

from nle_demo.cfg.cfg import add_extra_params_demo
from nle_demo.envs.babaisai.babaisai_params import add_extra_params_babaisai_env
from nle_demo.envs.babaisai.record_babaisai import register_babaisai_components
from nle_demo.view_demo import view_demo


def parse_babaisai_args(argv=None):
    argv = sys.argv[1:] + argv
    parser, partial_cfg = parse_args(argv=argv)
    add_extra_params_babaisai_env(parser)
    add_extra_params_demo(parser)
    final_cfg = parse_full_cfg(parser, argv)
    return final_cfg


def main():
    register_babaisai_components()
    env_registry = global_env_registry()
    for env_name in env_registry.keys():
        print(env_name)
        try:
            cfg = parse_babaisai_args(argv=[f"--env={env_name}"])
            info = view_demo(cfg)
            pprint.pprint(info)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
