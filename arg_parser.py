import sys
import argparse

parser = argparse.ArgumentParser(description='Add two numbers')
parser.add_argument("num1", type=int)
parser.add_argument("num2", type =int)
args = parser.parse_args()


def add_two_nums(num1, num2):
    return num1 + num2


if __name__ == "__main__":
    print(add_two_nums(args.num1, args.num2))
