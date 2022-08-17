import re
import hashlib


def str_to_hash(my_string, my_key='data', hash_size=30):
    h = hashlib.md5(my_key.encode('utf-8'))
    h.update(my_string.encode('utf-8'))
    return h.hexdigest()[:hash_size]


def homoglyph_regex(pattern):
    text = pattern.get('regex', [])
    if text:
        for index, part_pattern in enumerate(text):
            pattern['regex'][index] = change_dash(part_pattern)

    split_dict = pattern.get('split_regex', {})
    if split_dict and isinstance(split_dict, dict):
        for split_keys, split_group in split_dict.items():
            if isinstance(split_group, dict):
                for key, value in split_group.items():
                    pattern['split_regex'][split_keys][key] = change_dash(value)

    return pattern


def change_dash(part_pattern):

    check_alpha = r'\w-\w'
    alpha_pattern = re.finditer(check_alpha, part_pattern)
    alpha_hash = {}
    for obj in alpha_pattern:
        alpha_hash[obj.group()] = str_to_hash(obj.group(), "", 4)
        part_pattern = part_pattern.replace(obj.group(),str_to_hash(obj.group(), "", 4))

    check_slash = r'\\[-—–]'
    slash_pattern = re.finditer(check_slash, part_pattern)
    for obj in slash_pattern:
        part_pattern = part_pattern.replace(obj.group(), "-")

    check_brac = r'\\\[|\\]'
    brac_pattern = re.finditer(check_brac, part_pattern)
    for obj in brac_pattern:
        alpha_hash[obj.group()] = str_to_hash(obj.group(), "", 4)
        part_pattern = part_pattern.replace(obj.group(), str_to_hash(obj.group(), "", 4))

    re_dash = r'[-—–]'
    dash_index = [dash.start() for dash in re.finditer(re_dash, part_pattern)]

    if dash_index:
        split_string = []
        for _dash, num_dash in enumerate(dash_index):
            if _dash == 0:
                split_string.append(part_pattern[0:num_dash])
            else:
                split_string.append(part_pattern[dash_index[_dash-1]+1:num_dash])

        split_string.append(part_pattern[dash_index[-1]+1:])

        for _dash, num_dash in enumerate(dash_index):
            checker = False
            for char in part_pattern[num_dash:]:
                if char == "]":
                    checker = True
                    break

                elif char == "[":
                    checker = False
                    break

            if checker:
                split_string[_dash] = split_string[_dash] + "˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—"

            else:
                split_string[_dash] = split_string[_dash] + "[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—]"

        part_pattern = "".join(split_string)

    for key, value in alpha_hash.items():
        part_pattern = part_pattern.replace(value, key)

    return part_pattern


def homoglyph_resolver(uid_regex):
    if uid_regex:
        check_alpha = r'[a-z]-[a-z]'
        alpha_pattern = re.finditer(check_alpha, uid_regex)
        alpha_hash = {}
        for obj in alpha_pattern:
            alpha_hash[obj.group()] = str_to_hash(obj.group(), "", 4)
            uid_regex = uid_regex.replace(obj.group(), str_to_hash(obj.group(), "", 4))

        uid_regex = re.sub(r'[-–—]', '[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—]', uid_regex)

        for key, value in alpha_hash.items():
            uid_regex = uid_regex.replace(value, key)

    return uid_regex
