import pprint

from balrog_demo.envs.crafter.record_crafter import parse_crafter_args, register_crafter_components
from balrog_demo.view_demo import view_demo


def main():
    register_crafter_components()
    cfg = parse_crafter_args()
    info = view_demo(cfg)
    pprint.pprint(info)


if __name__ == "__main__":
    main()
