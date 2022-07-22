# Show cases how to use argparse and a typical template for a console app
# To see the help:
# python program_with_arguments.py --help
import argparse
import os

def parse_args():
    arg_parser = argparse.ArgumentParser()
    # Str arg
    arg_parser.add_argument('--api_key', type=str, help="API key to do the requests", required=True)
    # Non required Str arg with default
    arg_parser.add_argument('--endpoint', type=str, default="https://api.google.com", help="Endpoint used for the api calls", required=False)
    # Int arg with default value got from the system (cpu count)
    arg_parser.add_argument('--threads', type=int, default=os.cpu_count(), help=f"Number of threads, default number of cores, {os.cpu_count()}", required=False)
    # Flag arg without value
    arg_parser.add_argument('--verbose', action='store_true', help="Be verbose my friend", required=False)
    # Mutually exclusive options
    group = arg_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--slow_and_painful', action='store_true', help="(Slow) Will check every option", required=False)
    group.add_argument('--fast_and_furious', action='store_true', help="(Fast) Will guess what to look for", required=False)
    
    return arg_parser.parse_args()

def do_something_cool(api_key, endpoint, threads, verbose, slow_and_painful, fast_and_furious):
    print(api_key, endpoint, threads, verbose, slow_and_painful, fast_and_furious)

def main():
    args = parse_args()
    do_something_cool(args.api_key, args.endpoint, args.threads, args.verbose, args.slow_and_painful, args.fast_and_furious)

if __name__ == "__main__":
    main()
