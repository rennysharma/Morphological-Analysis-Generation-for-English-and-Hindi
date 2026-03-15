import re
import sys
from unicode_converter import unicode_converter

def analyze_hindi(word):
    """
    Rule-based morphological analyzer for Hindi
    Input: ISO 15919 transliterated Hindi word
    Returns: (root, [features])
    """

    # 1

    irregular_verbs = {
        "gayā": "jā",
        "gayī": "jā",
        "gaye": "jā",
        "kiyā": "kar",
        "kiyī": "kar",
        "kiye": "kar",
        "diyā": "de",
        "diye": "de",
        "liyā": "le",
        "liye": "le",
        "huā": "ho",
        "huī": "ho",
        "hue": "ho",
    }

    if word in irregular_verbs:
        return irregular_verbs[word], ["V", "PERF"]

    # 2

    if word == "hai":
        return "ho", ["V", "PRES", "SG"]

    if word == "hain":
        return "ho", ["V", "PRES", "PL"]

    # 3

    if word == "thā":
        return "ho", ["V", "PAST", "MASC"]

    if word == "thī":
        return "ho", ["V", "PAST", "FEM"]

    if word == "the":
        return "ho", ["V", "PAST", "PL"]

    # 4

    if re.search(r"rahā$", word):
        return re.sub(r"rahā$", "", word), ["V", "PROG", "MASC"]

    if re.search(r"rahī$", word):
        return re.sub(r"rahī$", "", word), ["V", "PROG", "FEM"]

    if re.search(r"rahe$", word):
        return re.sub(r"rahe$", "", word), ["V", "PROG", "PL"]

    # 5

    if re.search(r"tā$", word):
        return re.sub(r"tā$", "", word), ["V", "HAB", "MASC"]

    if re.search(r"tī$", word):
        return re.sub(r"tī$", "", word), ["V", "HAB", "FEM"]

    if re.search(r"te$", word):
        return re.sub(r"te$", "", word), ["V", "HAB", "PL"]

    # 6

    if re.search(r"yā$", word):
        return re.sub(r"yā$", "", word), ["V", "PERF", "MASC"]

    if re.search(r"yī$", word):
        return re.sub(r"yī$", "", word), ["V", "PERF", "FEM"]

    if re.search(r"ye$", word):
        return re.sub(r"ye$", "", word), ["V", "PERF", "PL"]

    # 7

    if re.search(r"egā$", word):
        return re.sub(r"egā$", "", word), ["V", "FUT", "MASC"]

    if re.search(r"egī$", word):
        return re.sub(r"egī$", "", word), ["V", "FUT", "FEM"]

    if re.search(r"eṁge$", word):
        return re.sub(r"eṁge$", "", word), ["V", "FUT", "PL"]

    # 8

    if re.search(r"nā$", word):
        return re.sub(r"nā$", "", word), ["V", "INF"]

    # 9

    if re.search(r"oṁ$", word):
        return re.sub(r"oṁ$", "ā", word), ["N", "MASC", "PL", "OBL"]

    if re.search(r"e$", word):
        possible = re.sub(r"e$", "ā", word)
        return possible, ["N", "MASC", "PL"]

    # 10

    if re.search(r"iyāṁ$", word):
        stem = re.sub(r"iyāṁ$", "", word)
        return stem + "ī", ["N", "FEM", "PL"]

    if re.search(r"eṁ$", word):
        return re.sub(r"eṁ$", "", word), ["N", "FEM", "PL"]

    # 11

    if re.search(r"ī$", word):
        return re.sub(r"ī$", "ā", word), ["ADJ", "FEM"]

    if re.search(r"e$", word):
        return re.sub(r"e$", "ā", word), ["ADJ", "PL"]

    if re.search(r"ā$", word):
        return word, ["ADJ", "MASC"]

    return word, ["UNKNOWN"]


if __name__ == "__main__":
    text = input().strip()
    iso_word = unicode_converter(text)
    print("Converted:", iso_word)

    root, features = analyze_hindi(iso_word)
    print(root, " ".join(features))