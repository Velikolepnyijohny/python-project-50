import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        add_help=False
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')
    
    args = parser.parse_args()
    
    if args.help:
        print_help()
        return
    
    print(f"Comparing {args.first_file} and {args.second_file}")

def print_help():
    help_text = """
usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help  show this help message and exit
    """
    print(help_text.strip())

if __name__ == "__main__":
    main()
