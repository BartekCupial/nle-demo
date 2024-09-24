import ast

from nle_utils.utils.utils import str2bool


def add_extra_params_babyai_env(parser):
    """
    Specify any additional command line arguments for NetHack environments.
    """
    # TODO: add help
    p = parser
