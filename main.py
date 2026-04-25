# main.py
import sys

def sort_list(words, reverse=False):
    return sorted(words, reverse=reverse)

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        words = [line.strip() for line in f]

    result = sort_list(words)
    print(result)