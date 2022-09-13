import re
import hashlib


def str_to_hash(my_string, my_key="data", hash_size=30):
    h = hashlib.md5(my_key.encode("utf-8"))
    h.update(my_string.encode("utf-8"))
    return h.hexdigest()[:hash_size]


def homoglyph_regex(pattern):

    """
    Homoglyph executor for ADF Generator
    :param str pattern: list of regex pattern in single repo adf generator specific
    :return: list of regex pattern with replaced homoglyph patterns
    """
    text = pattern.get("regex", [])
    if text:
        for index, regex in enumerate(text):
            pattern["regex"][index] = change_dash(regex)

    split_dict = pattern.get("split_regex", {})
    if split_dict and isinstance(split_dict, dict):
        for split_keys, split_group in split_dict.items():
            if isinstance(split_group, dict):
                for key, value in split_group.items():
                    pattern["split_regex"][split_keys][key] = change_dash(value)

    return pattern


def change_dash(regex):
    """
    General function for replacing dash with list of all dash in regex pattern
    :param str regex: regex containing different types of homoglyph
    :return: regex replaced with list of homoglyphs
    """
    regex_dict = {}

    regex_slash = r"\\[-—–]"
    slash_pattern = re.finditer(regex_slash, regex)
    for obj in slash_pattern:
        regex = regex.replace(obj.group(), "-")

    regex_brac = r"\\\[|\\]"
    brac_pattern = re.finditer(regex_brac, regex)
    for obj in brac_pattern:
        regex_dict[obj.group()] = str_to_hash(obj.group(), "", 3)
        regex = regex.replace(
            obj.group(), str_to_hash(obj.group(), "", 3)
        )

    regex_range = r"\w-\w"
    range_pattern = re.finditer(regex_range, regex)
    range_dict = {}
    for obj in range_pattern:
        range_checker = False
        for char in regex[obj.span()[0]:]:
            if char == "]":
                range_checker = True
                break

            elif char == "[":
                range_checker = False
                range_dict[obj.group()] = str_to_hash(obj.group(), "1", 3)
                regex = regex[0:obj.span()[0]] + str_to_hash(obj.group(), "1", 3) + regex[obj.span()[1]:]
                break
        if range_checker:
            regex_dict[obj.group()] = str_to_hash(obj.group(), "", 3)
            regex = regex.replace(
                obj.group(), str_to_hash(obj.group(), "", 3)
            )

    for key, value in range_dict.items():
        regex = regex.replace(value, key)

    re_dash = r"[-—–]"
    dash_indexes = [dash.start() for dash in re.finditer(re_dash, regex)]

    if dash_indexes:
        split_regex = []
        for _dash, dash_index in enumerate(dash_indexes):
            if _dash == 0:
                split_regex.append(regex[0:dash_index])
            else:
                split_regex.append(regex[dash_indexes[_dash - 1] + 1 : dash_index])

        split_regex.append(regex[dash_indexes[-1] + 1 :])

        for _dash, dash_index in enumerate(dash_indexes):
            checker = False
            for char in regex[dash_index:]:
                if char == "]":
                    checker = True
                    break

                elif char == "[":
                    checker = False
                    break

            if checker:
                split_regex[_dash] = split_regex[_dash] + "˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—"

            else:
                split_regex[_dash] = split_regex[_dash] + "[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—]"

        regex = "".join(split_regex)

    for key, value in regex_dict.items():
        regex = regex.replace(value, key)

    return regex


def homoglyph_resolver(uid_regex):
    """
    Homoglyph function for resolver
    :param str uid_regex: uid regex construct from resolver
    :return: uid regex repalced with list of homoglyphs
    """
    if uid_regex:
        regex_range = r"[a-z]-[a-z]"
        range_pattern = re.finditer(regex_range, uid_regex)
        regex_dict = {}
        for obj in range_pattern:
            regex_dict[obj.group()] = str_to_hash(obj.group(), "", 4)
            uid_regex = uid_regex.replace(obj.group(), str_to_hash(obj.group(), "", 4))

        uid_regex = re.sub(r"[-–—]", "[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—]", uid_regex)
        uid_regex = uid_regex.replace("[˗۔‐‑‒–⁃−\\-➖Ⲻ﹘—]", "-", 1)

        for key, value in regex_dict.items():
            uid_regex = uid_regex.replace(value, key)

    return uid_regex
