def formatting(format_name, diff):
    if not format_name:
        format_name = 'stylish'
    if format_name == 'plain':
        return
    elif format_name == 'stylish':
        final = get_tree(result).replace('  +', '+')
        final = final.replace('  -', '-').replace('  0', '')
    elif format_name == 'json':
        return
