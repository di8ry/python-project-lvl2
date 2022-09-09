def formatter(result, format_):
    if not format_:
        format_ = 'stylish'
    if format_ == 'plain':
        return '\n'.join(sorted(result))
    elif format_ == 'stylish':
        final = get_tree(result).replace('  +', '+')
        final = final.replace('  -', '-').replace('  0', '')
        return final


def get_tree(result, level=1):
    result_1 = sorted(result.items())
    final_str = '{\n'
    for key, value in result_1:
        key = replace_digit(key)
        if type(value) == dict:
            value = get_tree(value, level + 1)
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
