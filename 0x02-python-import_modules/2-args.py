#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("Number of argument(s): .")
    else:
        print(f"Number of argument(s): {num_args}")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
