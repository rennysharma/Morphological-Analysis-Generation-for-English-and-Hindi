import re


def generate_english(root, features):
    """
    Rule-based morphological generator for English
    Returns: surface form
    """

    # 1
    irregular_nouns = {
        "man": "men",
        "woman": "women",
        "child": "children",
        "tooth": "teeth",
        "foot": "feet",
        "mouse": "mice",
        "goose": "geese",
        "ox": "oxen",
        "person": "people"
    }

    if "N" in features and "PL" in features:
        if root in irregular_nouns:
            return irregular_nouns[root]


    # 2
    irregular_verbs_past = {
        "go": "went",
        "come": "came",
        "see": "saw",
        "eat": "ate",
        "run": "ran",
        "give": "gave",
        "take": "took",
        "write": "wrote",
        "drive": "drove",
        "buy": "bought",
        "think": "thought",
        "make": "made",
        "have": "had",
        "do": "did"
    }

    if "V" in features and "PAST" in features:
        if root in irregular_verbs_past:
            return irregular_verbs_past[root]


    # 3
    if "V" in features and "PROG" in features:
        if re.search(r"^[^aeiou]*[aeiou][bcdfghjklmnpqrstvwxyz]$", root):
            return root + root[-1] + "ing"


    # 4
    if "V" in features and "PROG" in features:
        if re.search(r"e$", root):
            return re.sub(r"e$", "", root) + "ing"


    # 5
    if "V" in features and "PAST" in features:
        if re.search(r"^[^aeiou]*[aeiou][bcdfghjklmnpqrstvwxyz]$", root):
            return root + root[-1] + "ed"


    # 6
    if "V" in features and "PAST" in features:
        if re.search(r"[^aeiou]y$", root):
            return re.sub(r"y$", "ied", root)


    # 7
    if "V" in features and "PAST" in features:
        return root + "ed"


    # 8
    if "V" in features and "PRES" in features:
        if re.search(r"[^aeiou]y$", root):
            return re.sub(r"y$", "ies", root)


    # 9
    if "V" in features and "PRES" in features:
        if re.search(r"(s|x|z|ch|sh)$", root):
            return root + "es"


    # 10
    if "V" in features and "PRES" in features:
        return root + "s"


    # 11
    if "N" in features and "PL" in features:
        if re.search(r"[^aeiou]y$", root):
            return re.sub(r"y$", "ies", root)


    # 12
    if "N" in features and "PL" in features:
        if re.search(r"(s|x|z|ch|sh)$", root):
            return root + "es"


    # 13
    if "N" in features and "PL" in features:
        if re.search(r"(f|fe)$", root):
            return re.sub(r"(f|fe)$", "ves", root)


    # 14
    if "N" in features and "PL" in features:
        return root + "s"


    # 15
    if "ADJ" in features and "COMP" in features:
        if re.search(r"[^aeiou]y$", root):
            return re.sub(r"y$", "ier", root)
        return root + "er"


    # 16
    if "ADJ" in features and "SUPER" in features:
        if re.search(r"[^aeiou]y$", root):
            return re.sub(r"y$", "iest", root)
        return root + "est"


    return root

print("Input format: root POS FEATURE")
print("POS: V (verb), N (noun), ADJ (adjective)")
print("Verb features: PROG, PAST, PRES")
print("Noun feature: PL")
print("Adjective features: COMP, SUPER")
print("Example: play V PROG")

data = input("Enter input: ").strip().split()


root = data[0].lower()
features = [f.upper() for f in data[1:]]

result = generate_english(root, features)
print(result)