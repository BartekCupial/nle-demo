import pprint

from nle_demo.envs.babaisai.record_babaisai import parse_babaisai_args, register_babaisai_components
from nle_demo.view_demo import view_demo


def main():
    register_babaisai_components()
    cfg = parse_babaisai_args()
    info = view_demo(cfg)
    pprint.pprint(info)


if __name__ == "__main__":
    main()
