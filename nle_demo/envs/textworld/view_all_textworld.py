import copy
import pprint
from collections import defaultdict

from nle_demo.envs.textworld.record_textworld import parse_textworld_args, register_textworld_components
from nle_demo.view_demo import view_demo


def main():
    cfg = parse_textworld_args()
    register_textworld_components(cfg)
    run_cfg = copy.deepcopy(cfg)
    reward = defaultdict(int)
    for i in range(25):
        run_cfg.seed = i
        info = view_demo(run_cfg)
        reward[i] = info["score"]
        if info["won"]:
            pprint.pprint(info)
            print(i)
            break
        else:
            max_key = max(reward, key=reward.get)
            print(f"seed: {max_key}, reward: {reward[max_key]}")


if __name__ == "__main__":
    main()
