import argparse

def parse_args_main() -> argparse.Namespace:

    parser = argparse.ArgumentParser(description="Datavant toy example")

    # features is a json. key: features. value: list of strings
    parser.add_argument(
        "--run-for",
        type=int,
        help="seconds to run script for",
        default=60
    )

    parser.add_argument(
        "--sleep-for",
        type=int,
        help="seconds between calls",
        default=30
    )

    parser.add_argument(
        '--verbose',
        type=str,
        default='false',
        help='print stuff'
    )
    
    return parser.parse_args()

