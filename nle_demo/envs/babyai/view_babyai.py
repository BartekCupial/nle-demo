from nle_demo.envs.babyai.record_babyai import parse_babyai_args, register_babyai_components
from nle_demo.view_demo import view_demo


def main():
    register_babyai_components()
    cfg = parse_babyai_args()
    view_demo(cfg)


if __name__ == "__main__":
    main()