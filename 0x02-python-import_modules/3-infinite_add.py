#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)
    print("{}".format(total))
