import string

states = ['Alabama', ' georgia!', 'georgia ', 'georgia', 'FlOalda', 'south caroain', 'West virginia?']


def clean_strings(strings, *funcs):
    results = []
    for s in strings:
        for f in funcs:
            s = f(s)
        results.append(s)
    return results


def strip(a):
    return str.strip(a)


def remove_special(a):
    return re.sub('[?!#*&$@]', '', a)


states = clean_strings(states, str.strip, lambda x: re.sub('[?!#*&$@]', '', x), str.title)
print(states)

