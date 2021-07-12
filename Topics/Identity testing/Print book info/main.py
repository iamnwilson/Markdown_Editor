def print_book_info(title, author=None, year=None):
    #  Write your code here
    if title and author and year:
        print(f'"{title}" was written by {author} in {year}')
    elif author is None and year is None:
        print(f'"{title}"')
    elif year is None:
        print(f'"{title}" was written by {author}')
    elif author is None:
        print(f'"{title}" was written in {year}')

