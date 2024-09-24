import ast

from nle_utils.utils.utils import str2bool


def add_extra_params_babaisai_env(parser):
    """
    Specify any additional command line arguments for NetHack environments.
    """
    # TODO: add help
    p = parser
    p.add_argument("--add_ruleset", type=str2bool, default=True)
