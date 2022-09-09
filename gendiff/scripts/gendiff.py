from gendiff.cli import parse_args
from gendiff.generate_diff import generate_diff, get_data


def main():
    args = parse_args()
    date_1 = get_data(args.first_file)
    date_2 = get_data(args.second_file)

    print(generate_diff(date_1, date_2, args.format))


if __name__ == '__main__':
    main()
