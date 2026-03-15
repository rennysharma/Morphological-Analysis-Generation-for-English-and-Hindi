import re
import sys


def unicode_converter(text):
    """
    Converts Devanagari Unicode text into ISO 15919 transliteration
    """
    output = ""
    i = 0
    
    while i < len(text):
        ch = text[i]
        code = ord(ch)

        # VOWELS
        if code == 0x0905: output += "a"      # अ
        elif code == 0x0906: output += "ā"    # आ
        elif code == 0x0907: output += "i"    # इ
        elif code == 0x0908: output += "ī"    # ई
        elif code == 0x0909: output += "u"    # उ
        elif code == 0x090A: output += "ū"    # ऊ
        elif code == 0x090B: output += "r̥"    # ऋ
        elif code == 0x090F: output += "e"    # ए
        elif code == 0x0910: output += "ai"   # ऐ
        elif code == 0x0913: output += "o"    # ओ
        elif code == 0x0914: output += "au"   # औ

        # CONSONANTS
        elif code == 0x0915: output += "ka"   # क
        elif code == 0x0916: output += "kha"  # ख
        elif code == 0x0917: output += "ga"   # ग
        elif code == 0x0918: output += "gha"  # घ
        elif code == 0x0919: output += "ṅa"   # ङ
        elif code == 0x091A: output += "ca"   # च
        elif code == 0x091B: output += "cha"  # छ
        elif code == 0x091C: output += "ja"   # ज
        elif code == 0x091D: output += "jha"  # झ
        elif code == 0x091E: output += "ña"   # ञ
        elif code == 0x091F: output += "ṭa"   # ट
        elif code == 0x0920: output += "ṭha"  # ठ
        elif code == 0x0921: output += "ḍa"   # ड
        elif code == 0x0922: output += "ḍha"  # ढ
        elif code == 0x0923: output += "ṇa"   # ण
        elif code == 0x0924: output += "ta"   # त
        elif code == 0x0925: output += "tha"  # थ
        elif code == 0x0926: output += "da"   # द
        elif code == 0x0927: output += "dha"  # ध
        elif code == 0x0928: output += "na"   # न
        elif code == 0x092A: output += "pa"   # प
        elif code == 0x092B: output += "pha"  # फ
        elif code == 0x092C: output += "ba"   # ब
        elif code == 0x092D: output += "bha"  # भ
        elif code == 0x092E: output += "ma"   # म
        elif code == 0x092F: output += "ya"   # य
        elif code == 0x0930: output += "ra"   # र
        elif code == 0x0932: output += "la"   # ल
        elif code == 0x0935: output += "va"   # व
        elif code == 0x0936: output += "śa"   # श
        elif code == 0x0937: output += "ṣa"   # ष
        elif code == 0x0938: output += "sa"   # स
        elif code == 0x0939: output += "ha"   # ह

        # NUKTA LETTERS
        elif code == 0x095B: output += "za"   # ज़
        elif code == 0x095C: output += "ṛa"   # ड़
        elif code == 0x095D: output += "ṛha"  # ढ़
        elif code == 0x095E: output += "fa"   # फ़

        # MATRAS
        elif code == 0x093E: output = output[:-1] + "ā"   # ा
        elif code == 0x093F: output = output[:-1] + "i"    # ि
        elif code == 0x0940: output = output[:-1] + "ī"    # ी
        elif code == 0x0941: output = output[:-1] + "u"    # ु
        elif code == 0x0942: output = output[:-1] + "ū"    # ू
        elif code == 0x0943: output = output[:-1] + "ṛ"    # ृ
        elif code == 0x0947: output = output[:-1] + "e"    # े
        elif code == 0x0948: output = output[:-1] + "ai"   # ै
        elif code == 0x094B: output = output[:-1] + "o"    # ो
        elif code == 0x094C: output = output[:-1] + "au"   # ौ

        # VIRAMA
        elif code == 0x094D:                  # ्
            if output.endswith("a"):
                output = output[:-1]

        # SIGNS
        elif code == 0x0901: output += "m̐"   # ँ (candrabindu)
        elif code == 0x0902: output += "ṁ"   # ं (anusvāra)
        elif code == 0x0903: output += "ḥ"   # ः (visarga)
        elif code == 0x093C: pass             # ़ (nukta combining mark — skip)

        else:
            output += ch

        i += 1

    return output


if __name__ == "__main__":
    text = input("Enter Devanagari text: ")
    result = unicode_converter(text)
    print("ISO 15919 Output:", result)