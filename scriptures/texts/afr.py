from __future__ import unicode_literals
from .base import Text


class Afrikaans(Text):
    """
    Afrikaans Bible translations (1933, 1953 and 1983)

    Info mostly taken from the "Afrikaanse Taal- en Stylgids" (Afrikaans language and style guide) of the
    "Nederduitse Gereformeerde Kerk in Suid-Afrika" (Dutch-German Reformed Church in South Africa) available at
    http://www.kaapkerkadmin.co.za/doks/17_Stylgids_14.pdf This style guide uses modern spellings with fewer diacritics,
    but I did make the regular expressions broad enough to recognise old (1953) spellings like "Matthéüs" and spellings
    that use only ASCII characters, like "Joel" instead of "Joël".

    TODO: check the number of verses in each chapter.
    They are not always the same as in English, especially in the Psalms, where we usually have one more verse.

    TODO: Many Afrikaans books start with "Die" (the) or have even longer titles, like "Aan die Romeine" (To the Romans)
    instead of "Romeine" (Romans). Which ones should we use?

    """
    books = {
        'gen': ('Genesis', 'Gen', 'G[eé]n(?:esis)?', [31, 25, 24, 26, 32, 22, 24, 22, 29, 32, 32, 20, 18, 24, 21, 16, 27, 33, 38, 18, 34, 24, 20, 67, 34, 35, 46, 22, 35, 43, 55, 32, 20, 31, 29, 43, 36, 30, 23, 23, 57, 38, 34, 34, 28, 34, 31, 22, 33, 26]),
        'eks': ('Eksodus', 'Eks', 'E(?:ks|x)(?:odus)?', [22, 25, 22, 31, 23, 30, 25, 32, 35, 29, 10, 51, 22, 31, 27, 36, 16, 27, 25, 26, 36, 31, 33, 18, 40, 37, 21, 43, 46, 38, 18, 35, 23, 35, 35, 38, 29, 31, 43, 38]),
        'lev': ('Levitikus', 'Lev', 'Lev(?:[ií]tikus)?', [17, 16, 17, 35, 19, 30, 38, 36, 24, 20, 47, 8, 59, 57, 33, 34, 16, 30, 37, 27, 24, 33, 44, 23, 55, 46, 34]),
        'num': ('Numeri', 'Num', 'N[uú]m(?:eri)?', [54, 34, 51, 49, 31, 27, 89, 26, 23, 36, 35, 16, 33, 45, 41, 50, 13, 32, 22, 29, 35, 41, 30, 25, 18, 65, 23, 31, 40, 16, 54, 42, 56, 29, 34, 13]),
        'deut': ('Deuteronomium', 'Deut', 'Deut(?:eron[oó]mium)?', [46, 37, 29, 49, 33, 25, 26, 20, 29, 22, 32, 32, 18, 29, 23, 22, 20, 22, 21, 20, 23, 30, 25, 22, 19, 19, 26, 68, 29, 20, 30, 52, 29, 12]),
        'jos': ('Josua', 'Jos', 'Jos(?:ua)?', [18, 24, 17, 24, 15, 27, 26, 35, 27, 43, 23, 24, 33, 15, 63, 10, 18, 28, 51, 9, 45, 34, 16, 33]),
        'rig': ('Rigters', 'Rig', 'Rig(?:t(?:ers)?)?', [36, 23, 31, 24, 31, 40, 25, 35, 57, 18, 40, 15, 25, 20, 20, 31, 13, 31, 30, 48, 25]),
        'rut': ('Rut', 'Rut', 'Rut', [22, 23, 18, 22]),
        '1sam': ('I Samuel', '1Sam', '(?:1|I)(?:\s)?Sam(?:uel)?', [28, 36, 21, 22, 12, 21, 17, 22, 27, 27, 15, 25, 23, 52, 35, 23, 58, 30, 24, 42, 15, 23, 29, 22, 44, 25, 12, 25, 11, 31, 13]),
        '2sam': ('II Samuel', '2Sam', '(?:2|II)(?:\s)?Sam(?:uel)?', [27, 32, 39, 12, 25, 23, 29, 18, 13, 19, 27, 31, 39, 33, 37, 23, 29, 33, 43, 26, 22, 51, 39, 25]),
        '1kon': ('I Konings', '1Kon', '(?:1|I)(?:\s)?Kon(?:ings)?', [53, 46, 28, 34, 18, 38, 51, 66, 28, 29, 43, 33, 34, 31, 34, 34, 24, 46, 21, 43, 29, 53]),
        '2kon': ('II Konings', '2Kon', '(?:2|II)(?:\s)?Kon(?:ings)?', [18, 25, 27, 44, 27, 33, 20, 29, 37, 36, 21, 21, 25, 29, 38, 20, 41, 37, 37, 21, 26, 20, 37, 20, 30]),
        '1kron': ('I Kronieke', '1Kron', '(?:1|I)(?:\s)?Kron(?:ieke)?', [54, 55, 24, 43, 26, 81, 40, 40, 44, 14, 47, 40, 14, 17, 29, 43, 27, 17, 19, 8, 30, 19, 32, 31, 31, 32, 34, 21, 30]),
        '2kron': ('II Kronieke', '2Kron', '(?:2|II)(?:\s)?Kron(?:ieke)?', [17, 18, 17, 22, 14, 42, 22, 18, 31, 19, 23, 16, 22, 15, 19, 14, 19, 34, 11, 37, 20, 12, 21, 27, 28, 23, 9, 27, 36, 27, 21, 33, 25, 33, 27, 23]),
        'esra': ('Esra', 'Esra', 'Esra', [11, 70, 13, 24, 17, 22, 28, 36, 15, 44]),
        'neh': ('Nehemia', 'Neh', 'Neh(?:em[ií]a)?', [11, 20, 32, 23, 19, 19, 73, 18, 38, 39, 36, 47, 31]),
        'est': ('Ester', 'Est', 'Est(?:er)?', [22, 23, 15, 17, 14, 14, 10, 17, 32, 3]),
        'job': ('Job', 'Job', 'Job', [22, 13, 26, 21, 27, 30, 21, 22, 35, 22, 20, 25, 28, 22, 35, 22, 16, 21, 29, 29, 34, 30, 17, 25, 6, 14, 23, 28, 25, 31, 40, 22, 33, 37, 16, 33, 24, 41, 30, 24, 34, 17]),
        'ps': ('Psalms', 'Ps', 'Ps(?:alm(?:s)?)?', [6, 12, 8, 8, 12, 10, 17, 9, 20, 18, 7, 8, 6, 7, 5, 11, 15, 50, 14, 9, 13, 31, 6, 10, 22, 12, 14, 9, 11, 12, 24, 11, 22, 22, 28, 12, 40, 22, 13, 17, 13, 11, 5, 26, 17, 11, 9, 14, 20, 23, 19, 9, 6, 7, 23, 13, 11, 11, 17, 12, 8, 12, 11, 10, 13, 20, 7, 35, 36, 5, 24, 20, 28, 23, 10, 12, 20, 72, 13, 19, 16, 8, 18, 12, 13, 17, 7, 18, 52, 17, 16, 15, 5, 23, 11, 13, 12, 9, 9, 5, 8, 28, 22, 35, 45, 48, 43, 13, 31, 7, 10, 10, 9, 8, 18, 19, 2, 29, 176, 7, 8, 9, 4, 8, 5, 6, 5, 6, 8, 8, 3, 18, 3, 3, 21, 26, 9, 8, 24, 13, 10, 7, 12, 15, 21, 10, 20, 14, 9, 6]),
        'spr': ('Spreuke van Salomo', 'Spr', 'Spr(?:euke(?: van Salomo)?)?', [33, 22, 35, 27, 23, 35, 27, 36, 18, 32, 31, 28, 25, 35, 33, 33, 28, 24, 29, 30, 31, 29, 35, 34, 28, 28, 27, 28, 27, 33, 31]),
        'pred': ('Prediker', 'Pred', 'Pred(?:iker)?', [18, 26, 22, 16, 20, 12, 29, 17, 18, 20, 10, 14]),
        'hoogl': ('Hooglied van Salomo', 'Hoogl', 'Hoogl(?:ied(?: van Salomo)?)?', [17, 17, 11, 16, 16, 13, 13, 14]),
        'jes': ('Jesaja', 'Jes', 'Jes(?:aja)?', [31, 22, 26, 6, 30, 13, 25, 22, 21, 34, 16, 6, 22, 32, 9, 14, 14, 7, 25, 6, 17, 25, 18, 23, 12, 21, 13, 29, 24, 33, 9, 20, 24, 17, 10, 22, 38, 22, 8, 31, 29, 25, 28, 28, 25, 13, 15, 22, 26, 11, 23, 15, 12, 17, 13, 12, 21, 14, 21, 22, 11, 12, 19, 12, 25, 24]),
        'jer': ('Jeremia', 'Jer', 'Jer(?:emia)?', [19, 37, 25, 31, 31, 30, 34, 22, 26, 25, 23, 17, 27, 22, 21, 21, 27, 23, 15, 18, 14, 30, 40, 10, 38, 24, 22, 17, 32, 24, 40, 44, 26, 22, 19, 32, 21, 28, 18, 16, 18, 22, 13, 30, 5, 28, 7, 47, 39, 46, 64, 34]),
        'klaagl': ('Klaagliedere', 'Klaagl', 'Klaagl(?:iedere(?: van Jeremia)?)?', [22, 22, 66, 22, 22]),
        'eseg': ('Esegiël', 'Eseg', 'Es[eé]g(?:i[ëe]l)?', [28, 10, 27, 17, 17, 14, 27, 18, 11, 22, 25, 28, 23, 23, 8, 63, 24, 32, 14, 49, 32, 31, 49, 27, 17, 21, 36, 26, 21, 26, 18, 32, 33, 31, 15, 38, 28, 23, 29, 49, 26, 20, 27, 31, 25, 24, 23, 35]),
        'dan': ('Daniël', 'Dan', 'Dan(?:i[eë]l)?', [21, 49, 30, 37, 31, 28, 28, 27, 27, 21, 45, 13]),
        'hos': ('Hosea', 'Hos', 'Hos(?:[eé]a)?', [11, 23, 5, 19, 15, 11, 16, 14, 17, 15, 12, 14, 16, 9]),
        'joël': ('Joël', 'Joël', 'Jo[ëe]l', [20, 32, 21]),  # TODO: Is it OK to use non-ASCII characters in the dictionary key?
        'am': ('Amos', 'Amos', 'Amos', [15, 16, 15, 13, 27, 14, 17, 14, 15]),
        'ob': ('Obadja', 'Obad', 'Obad(?:ja)?', [21]),
        'jona': ('Jona', 'Jona', 'Jon(?:a)?', [17, 10, 10, 11]),
        'miga': ('Miga', 'Miga', 'Mig(?:a)?', [16, 13, 12, 13, 15, 16, 20]),
        'nah': ('Nahum', 'Nah', 'Nah(?:um)?', [15, 13, 19]),
        'hab': ('Habakuk', 'Hab', 'H[aá]b(?:akuk)?', [17, 20, 19]),
        'sef': ('Sefanja', 'Sef', 'Sef(?:[aá]nja)?', [18, 15, 20]),
        'hag': ('Haggai', 'Hag', 'Hag(?:g(?:ai)?)?', [15, 23]),
        'sag': ('Sagaria', 'Sag', 'Sag(?:ar[ií]a)?', [21, 13, 10, 14, 11, 15, 14, 23, 17, 12, 17, 14, 9, 21]),
        'mal': ('Maleagi', 'Mal', 'Mal(?:e[aá]gi)?', [14, 17, 18, 6]),
        'matt': ('Mattheus', 'Matt', 'Matth?(?:[eé][uü]s)?', [25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36, 39, 28, 27, 35, 30, 34, 46, 46, 39, 51, 46, 75, 66, 20]),
        'mark': ('Markus', 'Mark', 'Mark(?:us)?', [45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72, 47, 20]),
        'luk': ('Lukas', 'Luk', 'Luk(?:as)?', [80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35, 32, 31, 37, 43, 48, 47, 38, 71, 56, 53]),
        'joh': ('Johannes', 'Joh', '(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I))Joh(?:annes)?', [51, 25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31, 27, 33, 26, 40, 42, 31, 25]),
        'hand': ('Handelinge van die Apostels', 'Hand', 'Hand(?:elinge(?: van die Apostels)?)?', [26, 47, 26, 37, 42, 15, 60, 40, 43, 48, 30, 25, 52, 28, 41, 40, 34, 28, 41, 38, 40, 30, 35, 27, 27, 32, 44, 31]),
        'rom': ('Romeine', 'Rom', 'Rom(?:eine)?', [32, 29, 31, 25, 21, 23, 25, 39, 33, 21, 36, 21, 14, 23, 33, 27]),
        '1kor': ('I Korintiërs', '1Kor', '(?:1|I)(?:\s)?Kor(?:inth?i[eë]rs)?', [31, 16, 23, 21, 13, 20, 40, 13, 27, 33, 34, 31, 13, 40, 58, 24]),
        '2kor': ('II Korintiërs', '2Kor', '(?:2|II)(?:\s)?Kor(?:inth?i[eë]rs)?', [24, 17, 18, 18, 21, 18, 16, 24, 15, 18, 33, 21, 14]),
        'gal': ('Galasiërs', 'Gal', 'Gal(?:[aá]si[eë]rs)?', [24, 21, 29, 31, 26, 18]),
        'ef': ('Efesiërs', 'Ef', 'Ef(?:[eé]si[eë]rs)?', [23, 22, 21, 32, 33, 24]),
        'fil': ('Filippense', 'Fil', 'Fil(?:ippense)?', [30, 30, 21, 23]),
        'kol': ('Kolossense', 'Kol', 'Kol(?:ossense)?', [29, 23, 25, 18]),
        '1tess': ('I Tessalonisense', '1Tess', '(?:1|I)(?:\s)?Tess(?:alonisense)?', [10, 20, 13, 18, 28]),
        '2tess': ('II Tessalonisense', '2Tess', '(?:2|II)(?:\s)?Tess(?:alonisense)?', [12, 17, 18]),
        '1tim': ('I Timoteus', '1Tim', '(?:1|I)(?:\s)?Tim(?:[oó]th?e[uü]s)?', [20, 15, 16, 16, 25, 21]),
        '2tim': ('II Timoteus', '2Tim', '(?:2|II)(?:\s)?Tim(?:[oó]th?e[uü]s)?', [18, 26, 17, 22]),
        'tit': ('Titus', 'Titus', 'Tit(?:us)?', [16, 15, 15]),
        'filem': ('Filemon', 'Filem', 'Fil[eé](?:m(?:on)?)?', [25]),
        'heb': ('Hebreërs', 'Heb', 'Heb(?:re[ëe]rs)?', [14, 18, 19, 16, 14, 20, 28, 13, 28, 39, 40, 29, 25]),
        'jak': ('Jakobus', 'Jak', 'Jak(?:obus)?', [27, 26, 18, 17, 20]),
        '1pet': ('I Petrus', '1Pet', '(?:1|I)(?:\s)?Pet(?:rus)?', [25, 25, 22, 19, 14]),
        '2pet': ('II Petrus', '2Pet', '(?:2|II)(?:\s)?Pet(?:rus)?', [21, 22, 18]),
        '1joh': ('I Johannes', '1Joh', '(?:(?:1|I)(?:\s)?)Joh(?:annes)?', [10, 29, 24, 21, 21]),
        '2joh': ('II Johannes', '2Joh', '(?:(?:2|II)(?:\s)?)Joh(?:annes)?', [13]),
        '3joh': ('III Johannes', '3Joh', '(?:(?:3|III)(?:\s)?)Joh(?:annes)?', [14]),
        'jud': ('Judas', 'Jud', 'Jud(?:as)?', [25]),
        'op': ('Openbaring van Johannes', 'Op', 'Op(?:en(?:b(?:aring(?: van Johannes)?)?)?)?', [20, 29, 22, 11, 14, 17, 17, 13, 21, 11, 19, 17, 18, 20, 8, 21, 18, 24, 21, 15, 27, 21]),
    }
