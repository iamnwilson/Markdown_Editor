def heading(head, size=0):
    if size <= 1 or None:
        return '# ' + head
    elif size >= 6:
        return '###### ' + head
    else:
        return '#' * size + ' ' + head
