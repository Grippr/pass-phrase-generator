# ------------------------------------------------------------------------------
#   Imports
# ------------------------------------------------------------------------------
from argparse import ArgumentParser
import os
import random
from math import log2

# ------------------------------------------------------------------------------
#   Constants
# ------------------------------------------------------------------------------
DEFAULT_ENTROPY = 80
DEFAULT_WORD_LIST = os.path.join(os.path.dirname(__file__), 'word_lists', 'mit_eprice_wordlist.10k')

# ------------------------------------------------------------------------------ 
#   Read word list
# ------------------------------------------------------------------------------ 
def read_word_list(word_list_file, max_word_len=None):
    ret = []
    with open(word_list_file, 'r') as f:
        for line in f.readlines():
            word = line.strip()
            if max_word_len is None or len(word) <= max_word_len:
                ret.append(word)
    return ret

# ------------------------------------------------------------------------------ 
#   Main 
# ------------------------------------------------------------------------------ 
def main(): 
    ################################ 
    # Parse command line arguments # 
    ################################ 
    parser = ArgumentParser(description="Generate a pass phrase from a set of common words")

    parser.add_argument(
        "-e", "--entropy", 
        type=float, 
        default=DEFAULT_ENTROPY,
        help=f"Bits of entropy of the pass phrase. Default={DEFAULT_ENTROPY}"
    )

    parser.add_argument(
        "-m", "--max-word-len",
        type = int,
        default=None,
        help="Maximum length of a word in the pass phrase. Default=No limit",
    )

    parser.add_argument(
        "-w", "--word-list",
        type=str,
        default=DEFAULT_WORD_LIST,
        help="File containing the list of words to use in the pass phrase:",
    )

    args = parser.parse_args()

    ####################################
    # Seed the random number generator #
    ####################################
    random.seed(os.urandom(128))

    ####################################
    # Read the word list
    ####################################
    words = read_word_list(args.word_list, args.max_word_len)
    if len(words) == 0:
        print(f"Error: No words found in {args.word_list}")
        return
    
    if args.max_word_len is not None:
        print(f"Using {len(words)} words with a maximum length of {args.max_word_len}")

    ####################################
    # Generate pass phrase
    ####################################
    entropy = 0
    pass_phrase = ""

    while entropy < args.entropy:
        word = random.choice(words)
        pass_phrase += word + " "
        entropy += log2(len(words))
    
    print(pass_phrase.strip())