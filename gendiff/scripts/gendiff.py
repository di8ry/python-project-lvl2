from gendiff.cli import parser
from gendiff.generate_diff import generate_diff, get_data
from gendiff.formatters import formatter

def main():
    args = parser()
    date_1 = args.first_file
    date_2 = args.second_file
    format_ = args.format

    result = generate_diff(get_data(date_1), get_data(date_2), format=format_)
    return formatter(result, format_)


if __name__ == '__main__':
    print(main())