from argparse import ArgumentParser, Namespace

ON_OFF_ACTION = "store_true"

class Arg:
    def __init__(self, short: str, long: str, action: str="store", arg_help: str="") -> None:
        self.short = short
        self.long = long
        self.action = action
        self.help = arg_help


class PosArg:
    def __init__(self, name: str, arg_help: str="", optional: bool=True) -> None:
        self.name = name
        self.help = arg_help
        self.optional = optional

def setup_argparse(description: str="", pos_args: list[PosArg] | None=None, args: list[Arg] | None=None) -> Namespace:
    if pos_args is None:
        pos_args = []
    if args is None:
        args = []

    p = ArgumentParser(
        description=description)

    for arg in args:
        p.add_argument(f"-{arg.short}", f"--{arg.long}", action=arg.action, help=arg.help)

    for arg in pos_args:
        p.add_argument(arg.name, help=arg.help, nargs="?" if arg.optional else None)

    return p.parse_args()
