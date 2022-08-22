import json
import yaml


def get_format(file_path):
    return file_path.split('.')[-1]


def get_data(file_path):
    file_format = get_format(file_path)
    if file_format == 'json':
        with open('./tests/fixtures/' + file_path, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    elif file_format == 'yaml':
        with open('./tests/fixtures/' + file_path, 'r', encoding='utf-8') as fy:
            return yaml.load(fy, Loader=yaml.FullLoader)


def generate_diff(date_1, date_2, format='stylish', parent=None):
    result = {}
    result_plain = []
    for key in date_1:
        if key in date_2:
            if date_1[key] == date_2[key]:
                result[f'{key} 0'] = date_1[key]
            else:
                if type(date_1[key]) == dict and type(date_2[key]) == dict:
                    if format == 'stylish':
                        result[f'{key} 0'] = generate_diff(date_1[key], date_2[key], format='stylish')
                    elif format == 'plain':
                        value_1 = date_1[key]
                        value_2 = date_2[key]
                        if parent:
                            key = parent + '.' + key
                        result_plain += generate_diff(value_1, value_2, format='plain', parent=key)
                else:
                    if format == 'stylish':
                        result[f'{key} 1'] = date_1[key]
                        result[f'{key} 2'] = date_2[key]
                    elif format == 'plain':
                        value_1 = to_plain(date_1[key])
                        value_2 = to_plain(date_2[key])
                        if parent:
                            key = parent + '.' + key
                        result_plain.append(f"Property '{key}' was updated. From {value_1} to {value_2}")
        else:
            if format == 'stylish':
                result[f'{key} 1'] = date_1[key]
            elif format == 'plain':
                if parent:
                    key = parent + '.' + key
                result_plain.append(f"Property '{key}' was removed")
    for key in date_2:
        if key not in date_1:
            if format == 'stylish':
                result[f'{key} 2'] = date_2[key]
            elif format == 'plain':
                value = to_plain(date_2[key])
                if parent:
                    key = parent + '.' + key
                result_plain.append(f"Property '{key}' was added with value: {value}")
    if format == 'plain':
        return result_plain
    return result


def to_plain(value):
    if type(value) == str:
        return "\'" + value + "\'"
    elif type(value) in (int, float):
        return value
    elif type(value) == bool:
        return str(value).lower()
    elif not value:
        return "null"
    elif type(value) == dict:
        return '[complex value]'


# if __name__ == '__main__':
#     date_1 = get_data("simple_before.json")
#     date_2 = get_data("simple_after.json")
#     result = (difference(date_1, date_2))
#     print(result)
    # with open('result2.txt', 'w') as f:
    #     final_str = get_final(result).replace('  +', '+').replace('  -', '-').replace('  0', '')
    #     f.write(final_str)
