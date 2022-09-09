from gendiff.formatters import stylish, json, plain


def formatting(format_name, diff):
    if format_name == 'plain':
        return plain.render(diff)
    elif format_name == 'stylish':
        return stylish.render(diff)
    elif format_name == 'json':
        return json.render(diff)

    raise ValueError(f'Unknown format: {format_name}')
