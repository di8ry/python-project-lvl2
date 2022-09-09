from gendiff.cli import parse_args
from gendiff.generate_diff import generate_diff, get_data
from gendiff.formatters import formatter


def main():
    args = parse_args()
    date_1 = args.first_file
    date_2 = args.second_file
    format_ = args.format

    result = generate_diff(get_data(date_1), get_data(date_2), format=format_)
    print(formatter(result, format_))


if __name__ == '__main__':
    main()
