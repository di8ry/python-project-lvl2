import argparse
from gendiff.generate_diff import difference, get_final, get_data


def main(date_1=None, date_2=None, format_=None):
    if not date_1:
        parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
        parser.add_argument('first_file')
        parser.add_argument('second_file')
        parser.add_argument(
            '-f',
            '--format',
            help='set format of output',
            default='json'
        )
        args = parser.parse_args()
        date_1 = args.first_file
        date_2 = args.second_file
        format_ = args.format

    result = difference(get_data(date_1), get_data(date_2), format=format_)
    if format_ == 'plain':
        return '\n'.join(sorted(result))
    else:
        return get_final(result).replace('  +', '+').replace('  -', '-').replace('  0', '')


if __name__ == '__main__':
    main()