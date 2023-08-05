import sys


def print_sorted_syspath() -> None:
    print('\nsys.path:')
    for path in sorted(sys.path, reverse=True):
        print(f'\t{path}')
