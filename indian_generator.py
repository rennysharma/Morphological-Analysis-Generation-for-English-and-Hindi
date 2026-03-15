import re
import sys
from unicode_converter import unicode_converter

def generate_hindi(root, features):
    """
    Rule-based morphological generator for Hindi (ISO 15919)
    Returns: surface form
    """

    # 1

    if root == "ho" and "PRES" in features:
        if "PL" in features:
            return "hain"
        return "hai"

    # 2

    if root == "ho" and "PAST" in features:
        if "FEM" in features:
            return "thī"
        if "PL" in features:
            return "the"
        return "thā"

    # 3

    irregular_perf = {
        "jā": {"MASC": "gayā", "FEM": "gayī", "PL": "gaye"},
        "kar": {"MASC": "kiyā", "FEM": "kiyī", "PL": "kiye"},
        "de": {"MASC": "diyā", "PL": "diye"},
        "le": {"MASC": "liyā", "PL": "liye"},
        "ho": {"MASC": "huā", "FEM": "huī", "PL": "hue"},
    }

    if "V" in features and "PERF" in features:
        if root in irregular_perf:
            if "FEM" in features:
                return irregular_perf[root].get("FEM")
            if "PL" in features:
                return irregular_perf[root].get("PL")
            return irregular_perf[root].get("MASC")

    # 4

    if "V" in features and "PROG" in features:
        if "FEM" in features:
            return root + " rahī"
        if "PL" in features:
            return root + " rahe"
        return root + " rahā"

    # 5

    if "V" in features and "HAB" in features:
        if "FEM" in features:
            return root + "tī"
        if "PL" in features:
            return root + "te"
        return root + "tā"

    # 6
    if "V" in features and "PERF" in features:
        if "FEM" in features:
            return root + "yī"
        if "PL" in features:
            return root + "ye"
        return root + "yā"

    # 7

    if "V" in features and "FUT" in features:
        if "FEM" in features:
            return root + "egī"
        if "PL" in features:
            return root + "eṁge"
        return root + "egā"

    # 8

    if "V" in features and "INF" in features:
        return root + "nā"

    # 9

    if "N" in features and root.endswith("ā"):
        stem = root[:-1]

        if "OBL" in features and "PL" in features:
            return stem + "oṁ"

        if "PL" in features:
            return stem + "e"

        return root

    # 10

    if "N" in features and root.endswith("ī"):
        stem = root[:-1]
        if "PL" in features:
            return stem + "iyāṁ"
        return root

    # 11

    if "N" in features and "PL" in features:
        if not root.endswith(("ā", "ī")):
            return root + "eṁ"

    # 12

    if "ADJ" in features and root.endswith("ā"):
        stem = root[:-1]

        if "FEM" in features:
            return stem + "ī"

        if "PL" in features:
            return stem + "e"

        return root

    return root


if __name__ == "__main__":
    print("Input format: <Devanagari root> <POS> <FEATURE1> <FEATURE2> ...")
    print("Example: खा V PROG MASC")
    print()

    data = input().strip().split()

    devanagari_root = data[0]
    features = [f.upper() for f in data[1:]]

    root = unicode_converter(devanagari_root)
    print("Converted root:", root)

    result = generate_hindi(root, features)
    print("Output:", result)