#calc.py

import argparse

parser = argparse.ArgumentParser(description = "CLI calculator.")

subparsers = parser.add_subparsers(help = "sub-command help", dest="command")

add = subparsers.add_parser("add", help = "add integers")
add.add_argument("ints_to_sum", nargs='*', type=int)

sub = subparsers.add_parser("sub", help = "sub integers")
sub.add_argument("ints_to_sub", nargs=2, type=int)

def aec_subtract(ints_to_sub):
    if len(ints_to_sub) != 2:
        raise ValueError("Subtraction requires exactly two arguments.")
    our_sub = ints_to_sub[0] - ints_to_sub[1]
    if our_sub < 0:
        our_sub = 0
    print(f"The subtracted result of our values is: {our_sub}")
    return(our_sub)

multi = subparsers.add_parser("multi", help = "multiply integers")
multi.add_argument("ints_to_multi", nargs='*', type=int)

div = subparsers.add_parser("div", help = "divide integers")
div.add_argument("ints_to_div", nargs=2, type=int)

def aec_divide(ints_to_div):
    if len(ints_to_div) != 2:
        raise ValueError("Division requires exactly two arguments.")
    try:
        our_div = ints_to_div[0] / ints_to_div[1]
        print(f"The divided result of our values is: {our_div}")
        return(our_div)
    except ZeroDivisionError:
        print( "Cannot Divide")
        return 0
        
    

if __name__ == "__main__":
    args = parser.parse_args()

    if args.command == "add": 
        our_sum = sum(args.ints_to_sum)
        print(f"The sum of our values is: {our_sum}")

    if args.command == "sub": 
        aec_subtract(args.ints_to_sub)

    if args.command == "multi":
        from functools import reduce 
        our_multi = reduce(lambda x,y: x*y, args.ints_to_multi)
        print(f"The multiplied result of our values is: {our_multi}")

    if args.command == "div":
        aec_divide(args.ints_to_div)