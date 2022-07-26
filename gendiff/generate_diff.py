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


def difference(date_1, date_2, plain=True, parent=None):
    result = {}
    result_plain = []
    for key in date_1:
        if key in date_2:
            if date_1[key] == date_2[key]:
                result[f'{key} 0'] = date_1[key]
            else:
                if type(date_1[key]) == dict and type(date_2[key]) == dict:
                    result[f'{key} 0'] = difference(date_1[key], date_2[key])
                    value_1 = to_plain(date_1[key])
                    value_2 = to_plain(date_2[key])
                    if parent:
                        key = parent + '.' + key
                    result_plain += difference(value_1, value_2, parent=key)
                else:
                    result[f'{key} 1'] = date_1[key]
                    result[f'{key} 2'] = date_2[key]
                    value_1 = to_plain(date_1[key])
                    value_2 = to_plain(date_2[key])
                    if parent:
                        key = parent + '.' + key
                    result_plain.append(f"Property '{key}' was updated. From {value_1} to {value_2}")
        else:
            result[f'{key} 1'] = date_1[key]
            if parent:
                key = parent + '.' + key
            result_plain.append(f"Property '{key}' was removed")
    for key in date_2:
        if key not in date_1:
            result[f'{key} 2'] = date_2[key]
            value = to_plain(date_2[key])
            if parent:
                key = parent + '.' + key
            result_plain.append(f"Property '{key}' was added with value: {value}")
    if plain:
        return result_plain
    return result

#         Property 'common.setting3' was updated. From true to null

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



def get_final(result, level=1):
    result_1 = sorted(result.items())
    final_str = '{\n'
    for key, value in result_1:
        key = replace_digit(key)
        if type(value) == dict:
            value = get_final(value, level + 1)
        for_replace = {'True': 'true', 'False': 'false', 'None': 'null'}
        for k, v in for_replace.items():
            value = str(value).replace(k, v)
        row = f'{"    " * level}{key}: {value}\n'
        final_str += row
    final_str += f'{"    " * (level - 1)}' + '}'
    return final_str


def replace_digit(key):
    if '1' in key[-1:]:
        return f'- {key.split()[0]}'
    elif '0' in key[-1:]:
        return f'0  {key.split()[0]}'
    elif '2' in key[-1:]:
        return f'+ {key.split()[0]}'
    return key


if __name__ == '__main__':
    date_1 = get_data("file_1.json")
    date_2 = get_data("file_2.json")
    result = (difference(date_1, date_2))
    print(result)
    with open('result2.txt', 'w') as f:
        final_str = get_final(result).replace('  +', '+').replace('  -', '-').replace('  0', '')
        f.write(final_str)
