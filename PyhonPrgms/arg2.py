import argparse
from ast import arg
import sys
import base64

parser = argparse.ArgumentParser(description="Python script to decode base64 and base32",
usage='%(prog)s --b64 --b32 cipher', 
epilog= "Example  %(prog)s aGVsbG8NCg== ")

parser.add_argument("--b64", "--base64" ,           help="decode base 64 encoding" ,
metavar="base64",
dest="b64",
nargs="+")


parser.add_argument("--b32", "--base32" ,           help="decode base 32 encoding" ,
metavar="base32",
dest="b32",
nargs="+")


parser.add_argument("-v",
help="version",
action="version",
version="%(prog)s 1.0.0")

args = parser.parse_args()

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit()

b64 = args.b64   
b32 = args.b32   


if b64:
    for i in b64:
        print((base64.b64decode(i)).decode())


if b32:
    for i in b32:
        print((base64.b32decode(i)).decode())        