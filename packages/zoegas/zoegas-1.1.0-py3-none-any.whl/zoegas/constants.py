"""
Constants to read dictionary entries
"""

import os
from collections import defaultdict
from zoegas import PACKDIR

# USER_PATH = os.path.expanduser('~')
# CORPUS_PATH = os.path.join(USER_PATH, "cltk_data", "old_norse", "dictionary", "old_norse_dictionary_zoega")

# dictionary_name = os.path.join(CORPUS_PATH, "dictionary.xml")
dictionary_name = os.path.join(PACKDIR, "dictionary.xml")

postags = defaultdict(str)
postags.update({
    "a.": "lkensf",
    "acc.": "o",
    "adv.": "a",
    "card. numb.": "ta",
    "compar.": "m",
    "conj.": "c",
    "dat.": "þ",
    "def. art.": "gken",
    "dem. pron.": "demonstrative pronoun",
    "f.": "nven",
    "for.": "e",
    "fem.": "v",
    "gen.": "e",
    "imperat.": "sb",
    "impers.": "impersonal",
    "indecl.": "indeclinable",
    "indef. pron.": "fo",
    "infin.": "sn",
    "int. pron.": "fs",
    "interj.": "interjection",
    "m.": "nken",
    "masc.": "k",
    "n.": "nhen",
    "neut.": "h",
    "nom.": "n",
    "ord. numb.": "to",
    "pers. pron.": "fp",
    "pl.": "f",
    "poss. pron.": "fe",
    "pp.": "sþ",
    "pr. p.": "se",
    "prep.": "a[oþe}",
    "pron.": "f",
    "refl.": "reflexive",
    "refl. pron.": "fb",
    "rel. pron.": "ft",
    "sing.": "e",
    "superl.": "e",
    "v.": "s",
    "v. refl.": "s[nbfvse]m",
})

pos_verbose = defaultdict(str)
pos_verbose.update({
    "a.": "adjective",
    "acc.": "accusative",
    "adv.": "adverb",
    "card. numb.": "cardinal number",
    "compar.": "comparative",
    "conj.": "conjunction",
    "dat.": "dative",
    "def. art.": "definite article",
    "dem. pron.": "demonstrative pronoun",
    "f.": "feminine noun",
    "for.": "e",
    "fem.": "feminine",
    "gen.": "genitive",
    "imperat.": "imperative",
    "impers.": "impersonal",
    "indecl.": "indeclinable",
    "indef. pron.": "indefinite pronoun",
    "infin.": "infinitive",
    "int. pron.": "interrogative pronoun",
    "interj.": "interjection",
    "m.": "masculine noun",
    "masc.": "masculine",
    "n.": "neuter noun",
    "neut.": "neuter",
    "nom.": "nominative",
    "ord. numb.": "ordinal number",
    "pers. pron.": "personnal pronoun",
    "pl.": "plural",
    "poss. pron.": "possessive pronoun",
    "pp.": "past participle",
    "pr. p.": "present participle",
    "prep.": "preposition",
    "pron.": "pronoun",
    "refl.": "reflexive",
    "refl. pron.": "reflexive pronoun",
    "rel. pron.": "relative pronoun",
    "sing.": "singular",
    "superl.": "superlative",
    "v.": "verb",
    "v. refl.": "verb reflexive",
})

abbreviations = {
    "a.": "adjective",
    "absol.": "absolute, absolutely",
    "acc.": "accusative",
    "adv.": "adverb",
    "card. numb.": "cardinal number",
    "Cf.": "confer",
    "cf.": "confer",
    "compar.": "comparative",
    "compds.": "compounds",
    "conj.": "conjunction",
    "dat.": "dative",
    "def. art.": "definite article",
    "dem. pron.": "demonstrative pronoun",
    "e-a": "einhverja",
    "e-m": "einhverjum",
    "e-n": "einhvern",
    "e-rra": "einhverra",
    "e-rri": "einhverri",
    "e-s": "einhvers",
    "e-t": "eitthvert",
    "e-u": "einhverju",
    "esp.": "especially",
    "f.": "feminine noun",
    "for.": "foreign",
    "fem.": "feminine",
    "freq.": "frequent, frequently",
    "gen.": "genitive",
    "i. e.": "id est",
    "imperat.": "imperative",
    "impers.": "impersonal",
    "indecl.": "indeclinable",
    "indef. pron.": "indefinite pronoun",
    "infin.": "infinitive",
    "int. pron.": "interrogative pronoun",
    "interj.": "interjection",
    "m.": "masculine noun",
    "masc.": "masculine",
    "n.": "neuter noun",
    "neut.": "neuter",
    "nom.": "nominative",
    "ord. numb.": "ordinal number",
    "pers. pron.": "personal pronoun",
    "pl.": "plural",
    "poet.": "poetically",
    "poss. pron.": "possessive pronoun",
    "pp.": "past participle",
    "pr. p.": "present participle",
    "prep.": "preposition",
    "pron.": "pronoun",
    "recipr.": "reciprocally",
    "refl.": "reflexive",
    "refl. pron.": "reflexive pronoun",
    "rel. pron.": "relative pronoun",
    "sing.": "singular",
    "superl.": "superlative",
    "v.": "verb",
    "v. refl.": "reflexive verb",
    "viz.": "namely"
}

oums = ["ǫ", "ö", "ø"]

heads = [
    "a", "á", "æ", "b", "d",
    "e", "f", "g", "h", "i",
    "í", "j", "k", "l", "m",
    "n", "o", "œ", "ó", oums[0],
    "p", "r", "s", "t", "þ",
    "u", "ú", "v", "y", "ý"
]

real_heads = [
    "a", "á", "æ", "b", "d",
    "e", "f", "g", "h", "i",
    "í", "j", "k", "l", "m",
    "n", "o", "œ", "ó", "ö", "ø",
    "p", "r", "s", "t", "þ",
    "u", "ú", "v", "y", "ý"
]

# head_dict_paths = [os.path.join(CORPUS_PATH, "entries", filename)
#                    for filename in os.listdir(os.path.join(CORPUS_PATH, "entries"))]
# head_filenames = [filename
#                   for filename in os.listdir(os.path.join(CORPUS_PATH, "entries"))]
# dheads = {head_filenames[i]: heads[i] for i in range(len(heads))}

if os.path.exists(os.path.join(PACKDIR, "entries")):
    head_dict_paths = [os.path.join(PACKDIR, "entries", filename)
                       for filename in os.listdir(os.path.join(PACKDIR, "entries"))]
if os.path.exists(os.path.join(PACKDIR, "entries")):
    head_filenames = [filename for filename in
                      os.listdir(os.path.join(PACKDIR, "entries"))]
    dheads = {head_filenames[i]: heads[i] for i in range(len(heads))}
