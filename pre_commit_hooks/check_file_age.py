import argparse
from typing import Sequence


def check_file_age(filenames: Sequence[str], maxage: int) -> int:
    retv = 0

    print(filenames)
    print(maxage)

    return retv


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument(
        '--maxage', type=int, default=500,
        help='Maximum allowable seconds age',
    )
    args = parser.parse_args(argv)

    return check_file_age(
        args.filenames,
        args.maxage,
    )


if __name__ == '__main__':
    raise SystemExit(main())
