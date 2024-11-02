import sys

from selenium_timetable.main import main
from utils.arguparse import setup_argparse, PosArg, Arg

if __name__ == "__main__":
    try:
        args = setup_argparse(pos_args=[PosArg("settings_path", "path of .ini file with settings", optional=False),
                                        PosArg("timestamp", "POSIX timestamp of start of week", optional=False)],
                              args=[Arg("lp", "light_image_path"), Arg("dp", "dark_image_path")])

        main(args.settings_path, int(args.timestamp), args.light_image_path, args.dark_image_path)
    except Exception as e:
        sys.exit(1)
