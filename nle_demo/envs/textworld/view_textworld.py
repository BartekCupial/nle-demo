import pprint

from nle_demo.envs.textworld.record_textworld import parse_textworld_args, register_textworld_components
from nle_demo.view_demo import view_demo


def main():
    cfg = parse_textworld_args()
    register_textworld_components(cfg)
    info = view_demo(cfg)
    pprint.pprint(info)


if __name__ == "__main__":
    main()
