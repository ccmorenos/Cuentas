"""Main file for the check app."""
from check.check_mng import CheckManager
import argparse

parser = argparse.ArgumentParser(
    description="Sensor Collecting.",
    formatter_class=argparse.RawTextHelpFormatter
)
parser.add_argument(
    '-d',  "--delimiter", type=str,
    default=",",
    help="Delimiter for the csv file. [Default: ',']"
)
parser.add_argument(
    '-f',  "--file", type=str,
    default="check.csv",
    help="Check file with all the data. [Default: check.csv]"
)
parser.add_argument(
    '-v',  "--verbose", type=int, default=1,
    help="""Set the verbose level from 0 to 2. Default"""
)
args = parser.parse_args()

check = CheckManager(args.file, args.delimiter)

try:

    while True:
        print("""Check menu:
    1: New Entry
    2: Remove Entry
    3: Show Check
    q: Exit""")

        val = input(">>> ")

        if val == "1":
            check.add_entry()

        elif val == "2":
            check.remove_entry()

        elif val == "3":
            check.get_check()

        elif val == "q":
            break

except KeyboardInterrupt:
    print()

except EOFError:
    print()
