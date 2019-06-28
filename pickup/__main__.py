import sys

from . import find_all_numbers


try:
    url = sys.argv.pop()
    find_all_numbers(url)
except Exception as e:
    print(f"Error occured: {e}")