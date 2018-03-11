import unittest

from ..texts.afr import Afrikaans

a = Afrikaans()


def f(txt):
    """
    accept a string containing a scripture reference, normalize it, and then
    return the reformatted string
    """
    re_match = a.scripture_re.match(txt)
    if re_match is None:
        raise ValueError("{} does not match the scripture regex.".format(txt))

    re_match_groups = re_match.groups()
    return a.reference_to_string(*a.normalize_reference(*re_match_groups))


class TestDeuterocanonBookNames(unittest.TestCase):
    def setUp(self):
        pass

    # Old Testament

    def test_genesis(self):
        self.assertEqual(f('génesis 1:1'), 'Genesis 1:1')
        self.assertEqual(f('genesis 1:1'), 'Genesis 1:1')
        self.assertEqual(f('gén 1:1'), 'Genesis 1:1')
        self.assertEqual(f('gen 1:1'), 'Genesis 1:1')

    def test_exodus(self):
        self.assertEqual(f('eksodus 1:1'), 'Eksodus 1:1')
        self.assertEqual(f('eks 1:1'), 'Eksodus 1:1')

    def test_leviticus(self):
        self.assertEqual(f('levitikus 1:1'), 'Levitikus 1:1')
        self.assertEqual(f('lev 1:1'), 'Levitikus 1:1')

    def test_numbers(self):
        self.assertEqual(f('numeri 1:1'), 'Numeri 1:1')
        self.assertEqual(f('num 1:1'), 'Numeri 1:1')

    def test_deuteronomy(self):
        self.assertEqual(f('deuteronomium 1:1'), 'Deuteronomium 1:1')
        self.assertEqual(f('deut 1:1'), 'Deuteronomium 1:1')

    def test_joshua(self):
        self.assertEqual(f('josua 1:1'), 'Josua 1:1')
        self.assertEqual(f('jos 1:1'), 'Josua 1:1')

    def test_judges(self):
        self.assertEqual(f('rigters 1:1'), 'Rigters 1:1')
        self.assertEqual(f('rig 1:1'), 'Rigters 1:1')

    def test_ruth(self):
        self.assertEqual(f('rut 1:1'), 'Rut 1:1')

    def test_i_samuel(self):
        self.assertEqual(f('I samuel 1:1'), 'I Samuel 1:1')
        self.assertEqual(f('1 samuel 1:1'), 'I Samuel 1:1')
        self.assertEqual(f('I sam 1:1'), 'I Samuel 1:1')
        self.assertEqual(f('1 sam 1:1'), 'I Samuel 1:1')
        self.assertEqual(f('1sam 1:1'), 'I Samuel 1:1')

    def test_ii_samuel(self):
        self.assertEqual(f('II samuel 1:1'), 'II Samuel 1:1')
        self.assertEqual(f('2 samuel 1:1'), 'II Samuel 1:1')
        self.assertEqual(f('II sam 1:1'), 'II Samuel 1:1')
        self.assertEqual(f('2 sam 1:1'), 'II Samuel 1:1')
        self.assertEqual(f('2sam 1:1'), 'II Samuel 1:1')

    def test_i_konings(self):
        self.assertEqual(f('I konings 1:1'), 'I Konings 1:1')
        self.assertEqual(f('1 konings 1:1'), 'I Konings 1:1')
        self.assertEqual(f('I kon 1:1'), 'I Konings 1:1')
        self.assertEqual(f('1 kon 1:1'), 'I Konings 1:1')
        self.assertEqual(f('1kon 1:1'), 'I Konings 1:1')

    def test_ii_konings(self):
        self.assertEqual(f('II konings 1:1'), 'II Konings 1:1')
        self.assertEqual(f('2 konings 1:1'), 'II Konings 1:1')
        self.assertEqual(f('II kon 1:1'), 'II Konings 1:1')
        self.assertEqual(f('2 kon 1:1'), 'II Konings 1:1')
        self.assertEqual(f('2kon 1:1'), 'II Konings 1:1')

    def test_i_kronieke(self):
        self.assertEqual(f('I kronieke 1:1'), 'I Kronieke 1:1')
        self.assertEqual(f('1 kronieke 1:1'), 'I Kronieke 1:1')

        self.assertEqual(f('I kron 1:1'), 'I Kronieke 1:1')
        self.assertEqual(f('1 kron 1:1'), 'I Kronieke 1:1')

    def test_ii_kronieke(self):
        self.assertEqual(f('II kronieke 1:1'), 'II Kronieke 1:1')
        self.assertEqual(f('2 kronieke 1:1'), 'II Kronieke 1:1')

        self.assertEqual(f('II kron 1:1'), 'II Kronieke 1:1')
        self.assertEqual(f('2 kron 1:1'), 'II Kronieke 1:1')

    def test_ezra(self):
        self.assertEqual(f('esra 1:1'), 'Esra 1:1')

    def test_nehemiah(self):
        self.assertEqual(f('nehemia 1:1'), 'Nehemia 1:1')
        self.assertEqual(f('neh 1:1'), 'Nehemia 1:1')

    def test_esther(self):
        self.assertEqual(f('ester 1:1'), 'Ester 1:1')
        self.assertEqual(f('est 1:1'), 'Ester 1:1')

    def test_job(self):
        self.assertEqual(f('job 1:1'), 'Job 1:1')

    def test_psalms(self):
        self.assertEqual(f('psalms 1:1'), 'Psalms 1:1')
        self.assertEqual(f('psalm 1:1'), 'Psalms 1:1')
        self.assertEqual(f('ps 1:1'), 'Psalms 1:1')

    def test_proverbs(self):
        self.assertEqual(f('spreuke 1:1'), 'Spreuke van Salomo 1:1')
        self.assertEqual(f('spr 1:1'), 'Spreuke van Salomo 1:1')

    def test_ecclesiastes(self):
        self.assertEqual(f('prediker 1:1'), 'Prediker 1:1')
        self.assertEqual(f('pred 1:1'), 'Prediker 1:1')

    def test_song_of_solomon(self):
        self.assertEqual(f('hooglied 1:1'), 'Hooglied van Salomo 1:1')
        self.assertEqual(f('hoogl 1:1'), 'Hooglied van Salomo 1:1')

    def test_isaiah(self):
        self.assertEqual(f('jesaja 1:1'), 'Jesaja 1:1')
        self.assertEqual(f('jes 1:1'), 'Jesaja 1:1')

    def test_jeremiah(self):
        self.assertEqual(f('jeremia 1:1'), 'Jeremia 1:1')
        self.assertEqual(f('jer 1:1'), 'Jeremia 1:1')

    def test_lamentations(self):
        self.assertEqual(f('klaagliedere 1:1'), 'Klaagliedere 1:1')
        self.assertEqual(f('klaagl 1:1'), 'Klaagliedere 1:1')

    def test_ezekiel(self):
        self.assertEqual(f('esegiël 1:1'), 'Esegiël 1:1')
        self.assertEqual(f('eseg 1:1'), 'Esegiël 1:1')

    def test_daniel(self):
        self.assertEqual(f('daniel 1:1'), 'Daniël 1:1')
        self.assertEqual(f('dan 1:1'), 'Daniël 1:1')

    def test_hosea(self):
        self.assertEqual(f('hosea 1:1'), 'Hosea 1:1')
        self.assertEqual(f('hos 1:1'), 'Hosea 1:1')

    def test_joel(self):
        self.assertEqual(f('joel 1:1'), 'Joël 1:1')

    def test_amos(self):
        self.assertEqual(f('amos 1:1'), 'Amos 1:1')

    def test_obadiah(self):
        self.assertEqual(f('obadja 1:1'), 'Obadja 1')
        self.assertEqual(f('obad 1:1'), 'Obadja 1')

    def test_jonah(self):
        self.assertEqual(f('jona 1:1'), 'Jona 1:1')
        self.assertEqual(f('jon 1:1'), 'Jona 1:1')

    def test_micah(self):
        self.assertEqual(f('miga 1:1'), 'Miga 1:1')

    def test_nahum(self):
        self.assertEqual(f('nahum 1:1'), 'Nahum 1:1')
        self.assertEqual(f('nah 1:1'), 'Nahum 1:1')

    def test_habakkuk(self):
        self.assertEqual(f('habakuk 1:1'), 'Habakuk 1:1')
        self.assertEqual(f('hab 1:1'), 'Habakuk 1:1')

    def test_zephaniah(self):
        self.assertEqual(f('sefanja 1:1'), 'Sefanja 1:1')
        self.assertEqual(f('sef 1:1'), 'Sefanja 1:1')

    def test_haggai(self):
        self.assertEqual(f('haggai 1:1'), 'Haggai 1:1')
        self.assertEqual(f('hag 1:1'), 'Haggai 1:1')

    def test_sagaria(self):
        self.assertEqual(f('sagaria 1:1'), 'Sagaria 1:1')
        self.assertEqual(f('sag 1:1'), 'Sagaria 1:1')

    def test_maleagi(self):
        self.assertEqual(f('maleagi 1:1'), 'Maleagi 1:1')
        self.assertEqual(f('mal 1:1'), 'Maleagi 1:1')

    # /Old Testament

    # New Testament

    def test_mattheus(self):
        self.assertEqual(f('mattheus 1:1'), 'Mattheus 1:1')
        self.assertEqual(f('matt 1:1'), 'Mattheus 1:1')

    def test_mark(self):
        self.assertEqual(f('markus 1:1'), 'Markus 1:1')
        self.assertEqual(f('mark 1:1'), 'Markus 1:1')

    def test_luke(self):
        self.assertEqual(f('lukas 1:1'), 'Lukas 1:1')
        self.assertEqual(f('luk 1:1'), 'Lukas 1:1')

    def test_johannes(self):
        self.assertEqual(f('johannes 1:1'), 'Johannes 1:1')
        self.assertEqual(f('joh 1:1'), 'Johannes 1:1')

    def test_acts(self):
        self.assertEqual(f('handelinge 1:1'), 'Handelinge van die Apostels 1:1')
        self.assertEqual(f('hand 1:1'), 'Handelinge van die Apostels 1:1')

    def test_romeine(self):
        self.assertEqual(f('romeine 1:1'), 'Romeine 1:1')
        self.assertEqual(f('rom 1:1'), 'Romeine 1:1')

    def test_i_korinthiers(self):
        self.assertEqual(f('I korinthiërs 1:1'), 'I Korintiërs 1:1')
        self.assertEqual(f('I korintiërs 1:1'), 'I Korintiërs 1:1')
        self.assertEqual(f('1 korinthiërs 1:1'), 'I Korintiërs 1:1')
        self.assertEqual(f('1 korintiërs 1:1'), 'I Korintiërs 1:1')
        self.assertEqual(f('1 korinthiers 1:1'), 'I Korintiërs 1:1')
        self.assertEqual(f('1 korintiers 1:1'), 'I Korintiërs 1:1')

        self.assertEqual(f('Ikor 1:1'), 'I Korintiërs 1:1')
        self.assertEqual(f('1kor 1:1'), 'I Korintiërs 1:1')

    def test_ii_korinthiers(self):
        self.assertEqual(f('II korinthiërs 1:1'), 'II Korintiërs 1:1')
        self.assertEqual(f('II korintiërs 1:1'), 'II Korintiërs 1:1')
        self.assertEqual(f('2 korinthiërs 1:1'), 'II Korintiërs 1:1')
        self.assertEqual(f('2 korintiërs 1:1'), 'II Korintiërs 1:1')
        self.assertEqual(f('2 korinthiers 1:1'), 'II Korintiërs 1:1')
        self.assertEqual(f('2 korintiers 1:1'), 'II Korintiërs 1:1')

        self.assertEqual(f('IIkor 1:1'), 'II Korintiërs 1:1')
        self.assertEqual(f('2kor 1:1'), 'II Korintiërs 1:1')

    def test_galasiers(self):
        self.assertEqual(f('galasiërs 1:1'), 'Galasiërs 1:1')
        self.assertEqual(f('gal 1:1'), 'Galasiërs 1:1')

    def test_efesiers(self):
        self.assertEqual(f('efesiërs 1:1'), 'Efesiërs 1:1')
        self.assertEqual(f('ef 1:1'), 'Efesiërs 1:1')

    def test_filippense(self):
        self.assertEqual(f('filippense 1:1'), 'Filippense 1:1')
        self.assertEqual(f('fil 1:1'), 'Filippense 1:1')

    def test_kolossense(self):
        self.assertEqual(f('kolossense 1:1'), 'Kolossense 1:1')
        self.assertEqual(f('kol 1:1'), 'Kolossense 1:1')

    def test_i_tessalonisense(self):
        self.assertEqual(f('I tessalonisense 1:1'), 'I Tessalonisense 1:1')
        self.assertEqual(f('I tess 1:1'), 'I Tessalonisense 1:1')
        self.assertEqual(f('1 tessalonisense 1:1'), 'I Tessalonisense 1:1')
        self.assertEqual(f('1 tess 1:1'), 'I Tessalonisense 1:1')

        self.assertEqual(f('Itessalonisense 1:1'), 'I Tessalonisense 1:1')
        self.assertEqual(f('Itess 1:1'), 'I Tessalonisense 1:1')
        self.assertEqual(f('1tessalonisense 1:1'), 'I Tessalonisense 1:1')
        self.assertEqual(f('1tess 1:1'), 'I Tessalonisense 1:1')

    def test_ii_tessalonisense(self):
        self.assertEqual(f('II tessalonisense 1:1'), 'II Tessalonisense 1:1')
        self.assertEqual(f('II tess 1:1'), 'II Tessalonisense 1:1')
        self.assertEqual(f('2 tessalonisense 1:1'), 'II Tessalonisense 1:1')
        self.assertEqual(f('2 tess 1:1'), 'II Tessalonisense 1:1')

        self.assertEqual(f('IItessalonisense 1:1'), 'II Tessalonisense 1:1')
        self.assertEqual(f('IItess 1:1'), 'II Tessalonisense 1:1')
        self.assertEqual(f('2tessalonisense 1:1'), 'II Tessalonisense 1:1')
        self.assertEqual(f('2tess 1:1'), 'II Tessalonisense 1:1')

    def test_i_timotheus(self):
        self.assertEqual(f('I timotheüs 1:1'), 'I Timoteus 1:1')
        self.assertEqual(f('I tim 1:1'), 'I Timoteus 1:1')
        self.assertEqual(f('1 timotheüs 1:1'), 'I Timoteus 1:1')
        self.assertEqual(f('1 tim 1:1'), 'I Timoteus 1:1')

        self.assertEqual(f('Itimotheüs 1:1'), 'I Timoteus 1:1')
        self.assertEqual(f('Itim 1:1'), 'I Timoteus 1:1')
        self.assertEqual(f('1timotheüs 1:1'), 'I Timoteus 1:1')
        self.assertEqual(f('1tim 1:1'), 'I Timoteus 1:1')

    def test_ii_timotheus(self):
        self.assertEqual(f('II timotheüs 1:1'), 'II Timoteus 1:1')
        self.assertEqual(f('II tim 1:1'), 'II Timoteus 1:1')
        self.assertEqual(f('2 timotheüs 1:1'), 'II Timoteus 1:1')
        self.assertEqual(f('2 tim 1:1'), 'II Timoteus 1:1')

        self.assertEqual(f('IItimotheüs 1:1'), 'II Timoteus 1:1')
        self.assertEqual(f('IItim 1:1'), 'II Timoteus 1:1')
        self.assertEqual(f('2timotheüs 1:1'), 'II Timoteus 1:1')
        self.assertEqual(f('2tim 1:1'), 'II Timoteus 1:1')

    def test_titus(self):
        self.assertEqual(f('titus 1:1'), 'Titus 1:1')
        self.assertEqual(f('tit 1:1'), 'Titus 1:1')

    def test_filemon(self):
        self.assertEqual(f('filemon 1:1'), 'Filemon 1')
        self.assertEqual(f('filem 1:1'), 'Filemon 1')
        self.assertEqual(f('file 1:1'), 'Filemon 1')

    def test_hebreers(self):
        self.assertEqual(f('hebreërs 1:1'), 'Hebreërs 1:1')
        self.assertEqual(f('heb 1:1'), 'Hebreërs 1:1')

    def test_jakobus(self):
        self.assertEqual(f('jakobus 1:1'), 'Jakobus 1:1')
        self.assertEqual(f('jak 1:1'), 'Jakobus 1:1')

    def test_i_petrus(self):
        self.assertEqual(f('I petrus 1:1'), 'I Petrus 1:1')
        self.assertEqual(f('I pet 1:1'), 'I Petrus 1:1')
        self.assertEqual(f('1 petrus 1:1'), 'I Petrus 1:1')
        self.assertEqual(f('1 pet 1:1'), 'I Petrus 1:1')

        self.assertEqual(f('Ipetrus 1:1'), 'I Petrus 1:1')
        self.assertEqual(f('Ipet 1:1'), 'I Petrus 1:1')
        self.assertEqual(f('1petrus 1:1'), 'I Petrus 1:1')
        self.assertEqual(f('1pet 1:1'), 'I Petrus 1:1')

    def test_ii_petrus(self):
        self.assertEqual(f('II petrus 1:1'), 'II Petrus 1:1')
        self.assertEqual(f('II pet 1:1'), 'II Petrus 1:1')
        self.assertEqual(f('2 petrus 1:1'), 'II Petrus 1:1')
        self.assertEqual(f('2 pet 1:1'), 'II Petrus 1:1')

        self.assertEqual(f('IIpetrus 1:1'), 'II Petrus 1:1')
        self.assertEqual(f('IIpet 1:1'), 'II Petrus 1:1')
        self.assertEqual(f('2petrus 1:1'), 'II Petrus 1:1')
        self.assertEqual(f('2pet 1:1'), 'II Petrus 1:1')

    def test_i_johannes(self):
        self.assertEqual(f('I johannes 1:1'), 'I Johannes 1:1')
        self.assertEqual(f('1 johannes 1:1'), 'I Johannes 1:1')

        self.assertEqual(f('Ijoh 1:1'), 'I Johannes 1:1')
        self.assertEqual(f('1joh 1:1'), 'I Johannes 1:1')

    def test_ii_Johannes(self):
        self.assertEqual(f('II johannes 1:1'), 'II Johannes 1')
        self.assertEqual(f('2 johannes 1:1'), 'II Johannes 1')

        self.assertEqual(f('IIjoh 1:1'), 'II Johannes 1')
        self.assertEqual(f('2joh 1:1'), 'II Johannes 1')

    def test_iii_johannes(self):
        self.assertEqual(f('III johannes 1:1'), 'III Johannes 1')
        self.assertEqual(f('3 johannes 1:1'), 'III Johannes 1')

        self.assertEqual(f('IIIjoh 1:1'), 'III Johannes 1')
        self.assertEqual(f('3joh 1:1'), 'III Johannes 1')

    def test_jude(self):
        self.assertEqual(f('judas 1:1'), 'Judas 1')
        self.assertEqual(f('jud 1:1'), 'Judas 1')

    def test_openbaring(self):
        self.assertEqual(f('openbaring 1:1'), 'Openbaring van Johannes 1:1')
        self.assertEqual(f('openbaring van johannes 1:1'), 'Openbaring van Johannes 1:1')
        self.assertEqual(f('op 1:1'), 'Openbaring van Johannes 1:1')
        self.assertEqual(f('open 1:1'), 'Openbaring van Johannes 1:1')
        self.assertEqual(f('openb 1:1'), 'Openbaring van Johannes 1:1')

    # /New Testament
