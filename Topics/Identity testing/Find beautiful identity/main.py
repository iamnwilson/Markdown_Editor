def object_with_beautiful_identity():
    for i in range(10_000):
        # Change the next line
        a = "888"
        if str(id(i)).endswith(a):
            return i
    return None
