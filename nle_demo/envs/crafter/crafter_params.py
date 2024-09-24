import ast

from nle_utils.utils.utils import str2bool


def add_extra_params_crafter_env(parser):
    """
    Specify any additional command line arguments for NetHack environments.
    """
    # TODO: add help
    p = parser
    p.add_argument("--area", nargs=2, type=int, default=(64, 64))
    p.add_argument("--view", type=int, nargs=2, default=(9, 9))
    p.add_argument("--length", type=int, default=None)
    p.add_argument("--health", type=int, default=9)
    p.add_argument("--window", type=int, nargs=2, default=(600, 600))
    p.add_argument("--size", type=int, nargs=2, default=(0, 0))
    p.add_argument("--record", type=str, default=None)
    p.add_argument("--fps", type=int, default=5)
    p.add_argument("--wait", type=str2bool, default=False)
    p.add_argument("--death", type=str, default="reset", choices=["continue", "reset", "quit"])
