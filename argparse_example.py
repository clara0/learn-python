import math
import argparse

# POSITIONAL ARGUMENTS
# parser = argparse.ArgumentParser(description='Calculate volume of a cylinder')
# parser.add_argument('radius', type=int, help='Radius of cylinder')
# parser.add_argument('height', type=int, help='Height of cylinder')
# args = parser.parse_args()
#
# OPTIONAL ARGUMENTS
# parser.add_argument('-r', '--radius', type=int, help='Radius of cylinder')
# parser.add_argument('-H', '--height', type=int, help='Height of cylinder') --> '-H' because '-h' is for help
#
# BETTER LOOKING HELP MESSAGE
# parser.add_argument('radius', type=int, metavar='', help='Radius of cylinder')
# parser.add_argument('height', type=int, metavar='', help='Height of cylinder')
#
# MAKING SOMETHING REQUIRED
# parser.add_argument('radius', type=int, required=True, help='Radius of cylinder')
# parser.add_argument('height', type=int, required=True, help='Height of cylinder')
#
# blah
parser = argparse.ArgumentParser(description='Calculate volume of a cylinder')
parser.add_argument('radius', type=int, help='Radius of cylinder')
parser.add_argument('height', type=int, help='Height of cylinder')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()


def cylinderVolume(radius, height):
    vol = math.pi * (radius ** 2) * height
    return vol


if __name__ == '__main__':
    volume = cylinderVolume(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print (f'Volume of a cylinder with radius {args.radius} and height {args.height} is {volume}.')
    else:
        print(f'Volume of a cylinder: {volume}')
