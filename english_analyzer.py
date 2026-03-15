import re

def analyze_english(word):
    """
    Rule-based morphological analyzer for English
    Returns: (root, [features])
    """

    # 1
    irregular_nouns = {
        "men": "man",
        "women": "woman",
        "children": "child",
        "teeth": "tooth",
        "feet": "foot",
        "mice": "mouse",
        "geese": "goose",
        "oxen": "ox",
        "people": "person"
    }

    if word in irregular_nouns:
        return irregular_nouns[word], ["N", "PL"]



    # 2
    irregular_verbs_past = {
        "went": "go",
        "came": "come",
        "saw": "see",
        "ate": "eat",
        "ran": "run",
        "gave": "give",
        "took": "take",
        "wrote": "write",
        "drove": "drive",
        "bought": "buy",
        "thought": "think",
        "made": "make",
        "had": "have",
        "did": "do"
    }

    if word in irregular_verbs_past:
        return irregular_verbs_past[word], ["V", "PAST"]


    # 3
    if re.search(r"([bcdfghjklmnpqrstvwxyz])\1ing$", word):
        root = re.sub(r"([bcdfghjklmnpqrstvwxyz])\1ing$", r"\1", word)
        return root, ["V", "PROG"]


    # 4
    if re.search(r"[^e]ing$", word):
        root = re.sub(r"ing$", "", word)
        return root, ["V", "PROG"]

    if re.search(r"eing$", word):
        root = re.sub(r"ing$", "", word) + "e"
        return root, ["V", "PROG"]


    # 5
    if re.search(r"([bcdfghjklmnpqrstvwxyz])\1ed$", word):
        root = re.sub(r"([bcdfghjklmnpqrstvwxyz])\1ed$", r"\1", word)
        return root, ["V", "PAST"]


    # 6
    if re.search(r"ied$", word):
        root = re.sub(r"ied$", "y", word)
        return root, ["V", "PAST"]


    # 7
    if re.search(r"ed$", word):
        root = re.sub(r"ed$", "", word)
        return root, ["V", "PAST"]


    # 8
    if re.search(r"ies$", word):
        root = re.sub(r"ies$", "y", word)
        return root, ["V", "PRES"]


    # 9
    if re.search(r"(oes|ches|shes|sses|xes|zes)$", word):
        root = re.sub(r"es$", "", word)
        return root, ["V", "PRES"]


    # 10
    if re.search(r"s$", word):
        root = re.sub(r"s$", "", word)
        return root, ["V", "PRES"]


    # 11
    if re.search(r"ies$", word):
        root = re.sub(r"ies$", "y", word)
        return root, ["N", "PL"]


    # 12
    if re.search(r"(xes|ches|shes|sses|zes)$", word):
        root = re.sub(r"es$", "", word)
        return root, ["N", "PL"]


    # 13
    if re.search(r"ves$", word):
        root = re.sub(r"ves$", "f", word)
        return root, ["N", "PL"]


    # 14
    if re.search(r"s$", word):
        root = re.sub(r"s$", "", word)
        return root, ["N", "PL"]


    # 15
    if re.search(r"er$", word):
        root = re.sub(r"er$", "", word)
        return root, ["ADJ", "COMP"]


    # 16
    if re.search(r"est$", word):
        root = re.sub(r"est$", "", word)
        return root, ["ADJ", "SUPER"]


    return word, ["UNKNOWN"]

word = input().strip()

root, features = analyze_english(word)

print(root, *features)