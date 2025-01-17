# ------------------------------------------------------------------------------
#   Imports
# ------------------------------------------------------------------------------
from argparse import ArgumentParser

# ------------------------------------------------------------------------------
#   Constants
# ------------------------------------------------------------------------------
DEFAULT_ENTROPY = 80

# ------------------------------------------------------------------------------
#   Main
# ------------------------------------------------------------------------------
def main():
    parser = ArgumentParser(description="Generate a pass phrase from a set of common words")

    parser.add_argument(
        "-e", "--entropy", 
        type=float, 
        default=DEFAULT_ENTROPY,
        help=f"Bits of entropy of the pass phrase. Default={DEFAULT_ENTROPY}"
    )

    args = parser.parse_args()
    print("Generating pass phrase with {} words".format(args.num_words))
