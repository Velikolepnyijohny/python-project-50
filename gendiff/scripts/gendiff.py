import argparse
import json

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
    
    
    with open(args.first_file, 'r') as file1, open(args.second_file, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
    
    print("First file data:")
    print(data1)
    print("\nSecond file data:")
    print(data2)
    print(f"\nOutput format: {args.format}")

if __name__ == '__main__':
    main()
