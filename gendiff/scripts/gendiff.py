import argparse
from gendiff.generate_diff import difference, get_final, get_data


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
    )
    args = parser.parse_args()
    date_1 = get_data(args.first_file)
    date_2 = get_data(args.second_file)
    format_ = args.format

    result = difference(date_1, date_2)
    if format_ == 'plain':
        print('\n'.join(sorted(result)))
    else:
        print(get_final(result).replace('  +', '+').replace('  -', '-').replace('  0', ''))


if __name__ == '__main__':
    main()