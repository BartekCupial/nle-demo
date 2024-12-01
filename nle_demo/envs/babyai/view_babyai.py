import pprint

from balrog_demo.envs.babyai.record_babyai import parse_babyai_args, register_babyai_components
from balrog_demo.view_demo import view_demo


def main():
    register_babyai_components()
    cfg = parse_babyai_args()
    info = view_demo(cfg)
    pprint.pprint(info)


if __name__ == "__main__":
    main()
