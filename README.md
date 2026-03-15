# Computational Linguistics Assignment 2
### Morphological Analysis & Generation for English and Hindi

A rule-based morphological analyzer and generator for English and Hindi (Devanagari), with a Devanagari-to-ISO 15919 transliteration module.

---

## Project Structure

```
.
├── english_analyser.py      # Morphological analyzer for English
├── english_generator.py     # Morphological generator for English
├── unicode_converter.py     # Devanagari → ISO 15919 transliteration
├── indian_analyser.py       # Morphological analyzer for Hindi
└── indian_generator.py      # Morphological generator for Hindi
```

---

## Getting Started

### Prerequisites

- Python 3.x

### Running

Each module can be imported and used independently. Example:

```python
from english_analyser import analyse
from english_generator import generate

analyse("running")    # → run V PROG
generate("run", "V PROG")  # → running
```

---

## English Rules

### Analyser (`english_analyser.py`)

| # | Rule | Example |
|---|------|---------|
| 1 | Irregular noun plurals | men → man N PL |
| 2 | Irregular verb past tense | went → go V PAST |
| 3 | Progressive -ing (consonant doubling) | running → run V PROG |
| 4 | Progressive -ing (silent-e deletion) | making → make V PROG |
| 5 | Past -ed (consonant doubling) | stopped → stop V PAST |
| 6 | Past -ied (consonant+y → i) | studied → study V PAST |
| 7 | Regular past -ed | walked → walk V PAST |
| 8 | 3SG present -ies (y alternation) | studies → study V PRES |
| 9 | 3SG present -es (sibilants) | watches → watch V PRES |
| 10 | 3SG present -s | runs → run V PRES |
| 11 | Noun plural -ies (y alternation) | babies → baby N PL |
| 12 | Noun plural -es (sibilants) | boxes → box N PL |
| 13 | Noun plural -ves (f→v alternation) | knives → knife N PL |
| 14 | Regular noun plural -s | dogs → dog N PL |
| 15 | Adjective comparative -er | taller → tall ADJ COMP |
| 16 | Adjective superlative -est | tallest → tall ADJ SUPER |

### Generator (`english_generator.py`)

Mirrors the analyser rules in reverse — takes a lemma + morphological tag and produces the surface form. Additionally handles:

- y → ier / iest for comparatives/superlatives (happy → happier, happiest)

---

## Hindi Rules

### Transliteration (`unicode_converter.py`)

Converts Devanagari to **ISO 15919** before morphological processing, turning complex Unicode sequences into a simple left-to-right string that suffix rules can match directly.

Key mappings:

| Category | Example | ISO Output |
|---|---|---|
| Independent vowels | अ, आ, इ, ई | a, ā, i, ī |
| Aspirated consonants | ख, घ, झ | kh, gh, jh |
| Retroflex consonants | ट, ड, ण | ṭ, ḍ, ṇ |
| Nukta letters | ज़, फ़, ड़ | za, fa, ṛa |
| Mātrās (vowel diacritics) | ा, ि, ी | ā, i, ī |
| Virama (halanta) | ् | removes inherent -a |
| Anusvāra / Candrabindu | ं, ँ | ṁ, m̐ |
| Visarga | ः | ḥ |

### Analyser (`indian_analyser.py`)

| # | Rule | Example |
|---|------|---------|
| 1 | Irregular perfective | गया → जा V PERF |
| 2 | Present copula | है → हो V PRES SG |
| 3 | Past copula | था/थी/थे → हो V PAST |
| 4 | Progressive aspect (-rahā) | कर रहा → कर V PROG MASC |
| 5 | Habitual aspect (-tā) | करता → कर V HAB MASC |
| 6 | Regular perfective (-yā) | किया → कर V PERF MASC |
| 7 | Future tense (-egā) | करेगा → कर V FUT MASC |
| 8 | Infinitive (-nā) | करना → कर V INF |
| 9 | Masculine ā-noun plural & oblique | लड़के → लड़का N PL |
| 10 | Feminine plural formation | लड़कियाँ → लड़की N PL |
| 11 | Adjective agreement (ā-ending) | अच्छी → अच्छा ADJ FEM |

### Generator (`indian_generator.py`)

Mirrors the analyser — takes a lemma + tag and produces the inflected form.

---

## Known Limitations & Error Analysis

### English

**Analyser errors** stem from rule ordering — verb -s rules fire before noun -s rules, so `dogs`, `boxes`, and `babies` are incorrectly tagged as verbs. The -er/-est rules also overgenerate: words like `water` and `sister` are wrongly analysed as comparatives since they happen to end in -er.

| Input | Output | Expected |
|---|---|---|
| happiest | happi ADJ SUPER | happy ADJ SUPER |
| making | mak V PROG | make V PROG |
| dogs | dog V PRES | dog N PL |

**Generator errors** are fewer; main failure is progressive formation for `cry` (outputs `cry` instead of `crying`).

### Hindi

The core limitation is the **absence of a lexicon** — the system only inspects suffixes and cannot distinguish inflectional suffixes from identical stem-final sequences.

| Input | Output | Expected | Cause |
|---|---|---|---|
| पानी | pānā ADJ FEM | (water, noun) | stem-final -ī confused with inflectional -ī |
| सोना | so V INF | (gold, noun) | -nā matched as infinitive |
| राजा | rājā ADJ MASC | (king, noun) | -ā matched as adjective ending |

**Transliteration errors:** nukta letters (ज़, फ़) emit the base consonant (ja, pha) instead of the correct nukta form (za, fa).

---

## Course
Computational Linguistics — Assignment 2
