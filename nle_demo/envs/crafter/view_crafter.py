from nle_demo.envs.crafter.record_crafter import parse_crafter_args, register_crafter_components
from nle_demo.view_demo import view_demo


def main():
    register_crafter_components()
    cfg = parse_crafter_args()
    view_demo(cfg)


if __name__ == "__main__":
    main()
