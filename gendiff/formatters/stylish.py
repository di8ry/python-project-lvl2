def build_ident(depth):
    return ' ' * 4 * depth


def render(diff, depth=0):
    node_type = diff['type']

    key = diff.get('key')
    value = diff.get('value')
    value_old = diff.get('value_old')
    value_new = diff.get('value_new')

    children = diff.get('children')

    ident = build_ident(depth)

    if node_type == 'root':
        lines = map(lambda child: render(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'

    if node_type == 'nested':
        lines = map(lambda child: render(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'  {key}: {result}'

    if node_type == 'added':
        return f'{ident}+ {key}: {value}'

    if node_type == 'deleted':
        return f'{ident}- {key}: {value}'

    if node_type == 'changed':
        return f'{ident}- {key}: {value_old}' \
               f'{ident}+ {key}: {value_new}'

    if node_type == 'unchanged':
        return f'{ident}  {key}: {value}'

    raise ValueError(f'Unknown node type: {node_type}')
