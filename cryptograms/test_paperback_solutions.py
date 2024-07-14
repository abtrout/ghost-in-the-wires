"""Solutions to the paperback edition, published in 2012."""

import base64

from .substitution import *
from .transposition import *


def test_chapter_01():
    """Rough Start"""
    input_str = "Max vhlm hy max unl wkboxk ingva B nlxw mh ingva fr hpg mktglyxkl"
    output = "the cost of the bus driver punch i used to punch my own transfers"
    assert caesar_shift(input_str, 7) == output
    # ANSWER: The punch cost $15.


def test_chapter_02():
    """Just Visiting"""
    input_str = "Estd mzzv esle elfrse xp szh ez ncplep yph topyetetpd hspy T hld l acp-eppy"
    output = "this book that taught me how to create new identities when i was a pre-teen"
    # Note: 15 (dollars) was last chapter's ANSWER.
    assert caesar_shift(input_str, 15) == output
    # ANSWER: The book was The Paper Trip.


def test_chapter_03():
    """Original Sin"""
    input_str = "pbzfsobp dkfobtpkx lq pbkfi ppbkfpry aoxtolc iixz lq abpr bobt pbzfsba cl bmvq obail bpbeQ"
    output = "these older type of devices were used to call forward business lines to answering services"
    assert caesar_shift(input_str[::-1], 3) == output
    # ANSWER: The device is called a diverter.


def test_chapter_04():
    """Escape Artist"""
    input_str = "gsvmznvlugsvnzrmuiznvhrszxpvwzgfhxrmgsvzikzmvgwzbh"
    output = "thenameofthemainframesihackedatuscinthearpanetdays"
    assert atbash(input_str) == output
    # ANSWER: The mainframe was called COSMOS: Computer System for Mainframe Operations.


def test_chapter_05():
    """All Your Phone Lines Belong to Me"""
    input_str = "jbi ujt veo eco ntk iwa lhc eeo anu uir trs hae oni rfn irt toh imi ets shs !eu"
    output = "itookacourseinthissubjectwheniranfromthejuvenileauthorities!"
    assert columnar_decipher(input_str.split(), d_row=1, d_col=-1) == output
    # ANSWER: The course was on criminal justice.


def test_chapter_06():
    """Will Hack for Love"""
    input_str = "bmFtZXRoZWNvbXBhbnl3aGVyZWJvbm5pZXdhc2VtcGxveWVkd2hlbndlc3RhcnRlZGRhdGluZw=="
    output = "namethecompanywherebonniewasemployedwhenwestarteddating"
    assert base64.b64decode(input_str).decode("ascii") == output
    # ANSWER: The company was GTE: General Telephone and Electronics Corporation.


def test_chapter_07():
    """Hitched in Haste"""
    input_str = "multbqncannqenabrhfgacnqogehchetbkkebmsqgkncchebr"
    output = "numberofdoorcodesihadforpacificbellcentraloffices"
    # We'll Simply Substitute with a special alphabet.
    sub_alphas = invert_alphabet(mixed_alphabet("gte"))
    assert simple_substitute(input_str, sub_alphas) == output
    # ANSWER: He had door codes for 11 PacBell offices.


def test_chapter_08():
    """Lex Luthor"""
    input_str = "'siass nuhmil sowsra amnapi waagoc ifinti dscisf iiiesf ahgbao staetn itmlro"
    output = "isaidiwasn'tthisfamousmagicianwhilebeingasmartasstoprisonofficials"
    assert columnar_decipher(input_str.split(), d_row=-1, d_col=1) == output
    # ANSWER: The famous magician was David Copperfield.


def test_chapter_09():
    """The Kevin Mitnick Discount Plan"""
    input_str = "tvifafwawehes hsesoonvtlimaeloemtcagmen irnoerrldony"
    output = "thisversionofnovatelfirmwareallowedmetochangemyesn"
    assert rail_decipher(input_str.split()) == output
    # ANSWER: The firmware version was 1.05.


def test_chapter_10():
    """Mystery Hacker"""
    input_str = "gnkusr ooursnsisti ttnotoihiec rolwaintmlk ovtgp"
    output = "gotrootonunlvworkstationusingthissimpletrick"
    assert rail_decipher(input_str.split()) == output
    # ANSWER: The trick was spamming ^C to escape the boot sequence.


def test_chapter_11():
    """Foul Play"""
    input_str = "ow gw ty kc qb eb nm ht ud pc iy ty ik tu zo dp gl qt hd"
    output = "mybrotheradamlistenedtothistypeofmusic"
    assert playfair_decrypt("", input_str) == output
    # ANSWER: Adam listened to rap and hip-hop.


def test_chapter_12():
    """You Can Never Hide"""
    input_str = "idniidhsubrseognteiuignuhrzdalrd ietfetinmeablnigorcsnuatoieclei"
    output = "iidentifiedthisnumberasbelongingtoericusingunauthorizedcallerid"
    assert rail_decipher(input_str.split()) == output
    # ANSWER: The number was 310 837-5412.


def test_chapter_13():
    """The Wiretapper"""
    input_str = "qclgjq'acrjcrlmqnyrcpgursmzyddmbcnngrgmfupceylyk"
    output = "managerwhoitippedoffaboutwiretapsonteltec'slines"
    assert caesar_shift(input_str, 2)[::-1] == output
    # ANSWER: The manager was Mark Kasden.


def test_chapter_14():
    """You Tap Me, I Tap You"""
    input_str = "c2VuaWxzJ2RhZHltbm9zcGF0ZXJpd2VodHRjZW5ub2NlcmRuYXNlbGVnbmFzb2xvdHlsZm90ZGFob2h3dG5lZ2F5dGlydWNlc2xsZWJjYXBlaHQ="
    output = "thepacbellsecurityagentwhohadtoflytolosangelesandreconnectthewiretapsonmydad'slines"
    assert base64.b64decode(input_str).decode("ascii")[::-1] == output
    # ANSWER: The security agent was Darrel Santos.


def test_chapter_15():
    """\"How the Fuck Did You Get That?\""""
    input_str = "ud mn cf ub mw re lb is ba of gx ty qc qh il ea ym nx bz ub he cf th is"
    output = "thishackerweshowedoffsastowhileathamburgerhamlet"
    assert playfair_decrypt("", input_str[::-1]) == output
    # ANSWER: They showed SAS to Eric Heinz.


def test_chapter_16():
    """Crashing Eric's Private Party"""
    input_str = "7\\3|2\\9|3\\5|4/0/8/2|6\\7/0/4\\4\\5/6/6\\5/7/8/9|7\\8/7|9\\5/9\\2\\3\\5\\7/8|2/0/8|2/6|6|2|7\\7\\0\\4\\9|"
    output = "iaskedericforthekeytothisphonecompanyfacility"
    assert vignere_decrypt("heinz", telephone_decrypt(input_str)) == output
    # ANSWER: He asked Eric for the key to PacBell central offices.


def test_chapter_17():
    """Pulling Back the Curtain"""
    input_str = "100 0000 10 1 01 001 00 1000 1 010 11 000 0 0000 11 000 000111 00011 10000 11111 11110 11000 00111 10000 11111 10000 11111"
    output = "whatnumberisthis?3104776565"
    assert twisted_morse_decode(input_str) == output
    # ANSWER: That is the number for the LA FBI headquarters.


def test_chapter_18():
    """Traffic Analysis"""
    input_str = "6365696a647a727573697775716d6d6e736e69627a74736a6f796970646 9737967647163656c6f71776c66646d63656d78626c6879746d796f6d 71747765686a6a71656d756c70696b6a627965696a71"
    output = "iidentifiedthefbicellphonesthatwherecallingericbyhackingintothiscellularprovider"
    decoded = bytes.fromhex(input_str.replace(" ", "")).decode("ascii")
    assert vignere_decrypt("lafbi", decoded)[::-1] == output
    # ANSWER: He hacked into PacTel.


def test_chapter_19():
    """Revelations"""
    input_str = "hranmoafignwoeoeiettwsoeheneteelaefnbaethscvrdniyajspwrl"
    output = "therealnameofanfbiagentwhosecoveridentitywasjosephwernle"
    # Divide the input string into two rows.
    half = len(input_str) // 2
    rows = [input_str[:half], input_str[half:]]
    assert columnar_decipher(rows, d_row=-1, d_col=1) == output
    # ANSWER: His name was Joseph Ways.


def test_chapter_20():
    """Reverse Sting"""
    input_str = "yo kb pn oc ox rh oq kb oh kp ge gs yt yt hg sa li mt ob sa po po mk pl md"
    output = "thecompanyteltechackedintotogetinformationonpeople"
    assert playfair_decrypt("fbi", input_str.replace(" ", "")) == output
    # ANSWER: TelTec hacked into TRW.


def test_chapter_21():
    """Cat and Mouse"""
    input_str = "77726e6b7668656a77676b6b276c6d6b6274616672656567776c6a7368697a70726f6d79656c"
    output = "darrellsanto'svoicemailpasswordwasthis"
    decoded = bytes.fromhex(input_str.replace(" ", "")).decode("ascii")
    assert vignere_decrypt("trw", decoded) == output
    # ANSWER: His voicemail password was 1313.


def test_chapter_22():
    """Detective Work"""
    input_str = "opoybdpmwoqbcpqcygagpcgxbpusapdluscplchxwoisgyeasdcpopdhadfyaethis"
    output = "thisdeviceiconnectedwithmyscannertoalertmewhenfbiwasnearmylocation"
    assert playfair_decrypt("", input_str)[::-1] == output
    # ANSWER: The device was a Digital Data Interpreter (DDI).


def test_chapter_23():
    """Raided"""
    input_str = "1001 0111 01 00 0 0 101 011 1111 1110 1011 1111 101 0110 1111 1101 110 010 100 0 0100 11 1011 1011 000 10 101 01"
    output = "myfavoritedonutsarethesekind"
    decoded = morse_decode(input_str.replace("1", ".").replace("0", "-"))
    assert autokey_decrypt("ddi", decoded) == output
    # ANSWER: His favorite donuts are FBI donuts.


def test_chapter_24():
    """Vanishing Act"""
    input_str = "anhgynnrtfafaqgmbhsuuzkzfbhbfk"
    output = "codeforawantedpersoninlasvegas"
    assert playfair_decrypt("fbidonuts", input_str)[::-1] == output
    # ANSWER: The code is 440.


def test_chapter_25():
    """Harry Houdini"""
    input_str = "nhyitekmnryoogmwefehocttntnoauttosumooalgei"
    output = "goutatthegymtheamountofmoneyilostonceworkin"
    # slight adjustment --^ theamountofmoneyilostonceworkingoutatthegym.
    assert every_nth(input_str, 3)[::-1] == output
    # ANSWER: He lost $11,000.


def test_chapter_26():
    """Private Investigator"""
    input_str = "11 0100 000 111 010 0 011 0010 000 010 11 10 1101 01 01 1 000 1 1111 01 0 011 1 010 1 1000 000 010 01 00 01 01 011 00 1101 0010 1 010 1 10 0 001101 110010 001101 110010 001101 100 0000 1 10 101 0 111 0 10 010 0101 0000 11 10 001 10 1 011 00 100 1 10 0 00 0 00 1 000"
    output = "ilookedforinfantothatwereborninadifferent?????whenresearchingnewmdentities"
    assert twisted_morse_decode(input_str) == output
    # ANSWER: He looked for infants born in a different state.


def test_chapter_27():
    """Here Comes the Sun"""
    input_str = "laeaslarhawpuiolshawzadxijxkjgvvbvaxavlowyuuhdsxausmrmbulbegukseq"
    output = "thehostnamewhichwasusedforthesecuritybugdatabaseatsunmicrosystems"
    assert autokey_decrypt("state", input_str) == output
    # ANSWER: The hostname was elmer.


def test_chapter_28():
    """Trophy Hunter"""
    input_str = "70776d61766374666f2770636d6167797a786977786f78656a7974696465737073786f65696f63726f64706a6f766b636165686573677069637a61786172"
    output = "asecurityflawinthisprogramallowedmetobreakintonovell'sfirewall"
    decoded = bytes.fromhex(input_str).decode("ascii")
    assert autokey_decrypt("elmer", decoded)[::-1] == output
    # ANSWER: The security flaw was in sendmail.


def test_chapter_29():
    """Departure"""
    input_str = "qnxpnebielnudqqpbibecua3m'llswhmmhrdzucclsfvqmdunepbkreezkarsnngpkgmscdnkr"
    output = "thenameoftheemployssthatsetmeupanabbountonnoveiiddscomdialupterminalserver"
    assert playfair_decrypt("sendmail", input_str)[::-1] == output
    # ANSWER: The employee was Shawn Nunley.


def test_chapter_30():
    """Blindsided"""
    input_str = "eyiyibemhemijixvpyiocjkxdwwxdazvtkaazrvl"
    output = "thereasoniwasfiredfromthelawfirmindenver"
    assert autokey_decrypt("nunley", input_str)[::-1] == output
    # ANSWER: He was fired for consulting on company time.


def test_chapter_31():
    """Eyes in the Sky"""
    input_str = "usygbjmqeauidgttlcflgqmfqhyhwurqmbxzoqmnpmjhlneqsctmglahp"
    output = "thispersonwastrickedintosendingmenumerousvmssecurityholes"
    assert autokey_decrypt("consulting", input_str)[::-1] == output
    # ANSWER: He tricked Neill Clift.


def test_chapter_32():
    """Sleepless in Seattle"""
    input_str = "tpdwxjw'viyegmzbecfvpcqtuwdinpfhzvvfadzbkfoevcnseozxffdlvrdo'jwsjkzllxwapfrvhuaqz"
    output = "icompromisedthisuser'spasswordthroughnetworkmonitoringtohackintoshimomura'sserver"
    assert autokey_decrypt("clift", input_str)[::-1] == output
    # ANSWER: He compromised david's password.


def test_chapter_33():
    """Hacking the Samurai"""
    input_str = "010 1 0001 101 0 111 000 100001 01 101 001 00 111 00 00 1111 000 01 111 1 10 000 0000 1001 000 11 0000 0 111 0 0 0101 010 110 111 111 0 1111 1 101 111 1101 110 01 00 010 111 000 0100 111 01 100 00"
    output = "iwaslookingforthesourcetothisphoneonshimomura?sserver"
    inverted = input_str.replace("1", "2").replace("0", "1").replace("2", "0")
    assert twisted_morse_decode(inverted)[::-1] == output
    # ANSWER: He was looking for the source to OKI.


def test_chapter_34():
    """Hiding in the Bible Belt"""
    input_str = "eqfeihchqqlndcinrarnfhqdvmlqnmcrlphaccqmaefkzhlslnstmqgmma"
    output = "thisemployeeatintermetricsuploadedthemotorolacompilerforme"
    assert bifid_decrypt("oki", input_str)[::-1] == output
    # ANSWER: The employee was Marty Stolz.


def test_chapter_35():
    """Game Over"""
    input_str = "ifdmnbbnqitnsobmmmtthdkhqbqzpo\"nduqz\"zhnemccxhyaninaxanf"
    output = "someoneloggedintomymartyaccountonthissystemfromthewell"
    assert bifid_decrypt("marty", input_str)[::-1] == output
    # ANSWER: The system was escape.com


def test_chapter_36():
    """An FBI Valentine"""
    input_str = "kgqmicewdnfmastcefkxlkqshgrfsspotxuesqvcohxttpcuvhnxawypuwzdt"
    output = "thefbifoundthisiteminmyskiiacketthatconfirmediwaskevinmitnick"
    assert bifid_decrypt("esc", input_str)[::-1] == output
    # ANSWER: They found a pay stub made out to Kevin Mitnick.


def test_chapter_37():
    """Winning the Scapegoat Sweepstakes"""
    input_str = "0\\6\\2/7\\4/2\\4\\8\\2|8|6|7\\0\\4\\3/2|8/7/3\\2/2/5|6/4|8\\7\\6\\6\\3\\2|3/3\\7/4|6/0/3|7/0\\6|8|9/4\\4/6/5/4|5|0\\8\\9\\7/4|4/4|8|5/3/3|4|8|4/0\\5|8/2/"
    output = "namethedocumcntaryfilmwhichcounteredthchrossinaccuraciesoftakedown"
    decoded = telephone_decrypt(input_str)
    assert bifid_decrypt("paystub", decoded)[::-1] == output
    # ANSWER: The documentary was Freedom Downtime.


def test_chapter_38():
    """Aftermath: A reversal of Fortune"""
    input_str = "001101 110010 001101 110010 001101 110010 001101 110010 111 00 011 00 10 110 0000 11 00 1001 110 0100 111 10 11 00 1101 1001 0100 10 100 11 01 101 0010 11 101 011 111 000 100 010 1001 001 1 101 01 010 1010 01 0 1110 10 0111 010 010"
    output = "???"  # TODO!
