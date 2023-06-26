import argparse
import os
from typing import Sequence


def check_file_age(file: str, maxage: int) -> int:
    retv = 1

    age = os.path.getmtime(file)
    print(file, age, maxage)

    return retv


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument(
        '--file', type=str, default="",
        help='File to check',
    )
    parser.add_argument(
        '--maxage', type=int, default=500,
        help='Maximum allowable seconds age',
    )
    args = parser.parse_args(argv)

    return check_file_age(
        args.file,
        args.maxage,
    )


if __name__ == '__main__':
    raise SystemExit(main())
