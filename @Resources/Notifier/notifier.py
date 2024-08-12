from argparse import ArgumentParser, Namespace
from tkinter import messagebox

def main():
  args = setup_argparse(pos_args=[PosArg("title", optional=False), PosArg("message", optional=False)])

  messagebox.showerror(title=args.title, message=args.message)

# Modified utils.arguparse
class PosArg:
    def __init__(self, name: str, arg_help: str="", optional: bool=True, default=None) -> None:
        self.name = name
        self.help = arg_help
        self.optional = optional
        self.default = default

def setup_argparse(description: str="", pos_args: list[PosArg] | None=None) -> Namespace:
    p = ArgumentParser(
        description=description)
    
    if pos_args is None:
        pos_args = []

    for arg in pos_args:
        p.add_argument(arg.name, help=arg.help, nargs="?" if arg.optional else None, default=arg.default)

    return p.parse_args()

if __name__ == "__main__":
  main()
