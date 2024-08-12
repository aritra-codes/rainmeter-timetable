import logging
import sys

from selenium_satchel_one.main import main
from utils.arguparse import setup_argparse, PosArg, Arg

if __name__ == "__main__":
    try:
        args = setup_argparse(pos_args=[PosArg("settings_path", optional=False)],
                              args=[Arg("tl", "timetable_light_image_path"), Arg("td", "timetable_dark_image_path"), Arg("d", "date")])

        main(args.settings_path, args.timetable_light_image_path, args.timetable_dark_image_path, args.date)
    except Exception as e:
        logging.error(e)

        sys.exit(1)
