import argparse
from gendiff import generate_diff

def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        add_help=False
    )
    
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    
    
    parser.add_argument('-f', '--format', 
                        metavar='FORMAT',
                        help='set format of output',
                        default='stylish')
    
    
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='show this help message and exit')
    
    
    args = parser.parse_args()
    

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
