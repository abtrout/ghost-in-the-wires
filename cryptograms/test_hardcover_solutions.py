"""Solutions to the original hardcover edition, published in 2011."""

import base64

from .substitution import *


def test_chapter_01():
    """Rough Start"""
    input_str = "Yjcv ku vjg pcog qh vjg uauvgo wugf da jco qrgtcvqtu vq ocmg htgg rjqpg ecnnu?"
    output = "what is the name of the system used by ham operators to make free phone calls?"
    assert caesar_shift(input_str, 24) == output
    # ANSWER: auto patch


def test_chapter_02():
    """Just Visiting"""
    input_str = "Wbth lal voe htat oy voe wxbirtn vfzbqt wagye C poh aeovsn vojgav?"
    output = "what was the name of the central office where i was almost caught?"
    assert vignere_decrypt("autopatch", input_str) == output
    # ANSWER: sunset gower


def test_chapter_03():
    """Original Sin"""
    input_str = "Nyrk grjjnfiu uzu Z xzmv kf jvk lg re rttflek fe Kyv Rib?"
    output = "what password did i give to set up an account on the ark?"
    assert caesar_shift(input_str, 9) == output
    # ANSWER: jelly


def test_chapter_04():
    """Escape Artist"""
    input_str = "Flle ujw esc wexp mo xsp kjr hsm hiwwcm, \"Wplpll stq lec qma e wzerg mzkk!\"?"
    output = "what was the name of the man who yelled, \"search his car for a logic bomb!\"?"
    assert vignere_decrypt("jelly", input_str) == output
    # ANSWER: steve cooley


def test_chapter_05():
    """All Your Phone Lines Belong to Me"""
    input_str = "Bmfy ytbs ini N mnij tzy ns zsynq ymj Ozajsnqj Htzwy qtxy ozwnxinhynts tajw rj?"
    output = "what town did i hide out in until the juvenile court lost jurisdiction over me?"
    assert caesar_shift(input_str, 21) == output
    # ANSWER: oroville


def test_chapter_06():
    """Will Hack for Love"""
    input_str = "Kyoo olxi rzr Niyovo Cohjpcx ojy dn T apopsy?"
    output = "what game did sandra lambert ask if i played?"
    assert vignere_decrypt("oroville", input_str) == output
    # ANSWER: hearts


def test_chapter_07():
    """Hitched in Haste"""
    input_str = "Kvoh wg hvs boas ct hvs Doqwtwq Pszz sadzcmss kvc fsor hvs wbhsfboz asac opcih am voqywbu oqhwjwhwsg cjsf hvs voa forwc?"
    output = "what is the name of the pacific bell employee who read the internal memo about my hacking activities over the ham radio?"
    assert caesar_shift(input_str, 12) == output
    # ANSWER: bill cook


def test_chapter_08():
    """Lex Luthor"""
    input_str = "Iwh xwqv wpvpj fwr Vfvyj qks wf nzc ncgsoo esg psd gwc ntoqujvr ejs rypz nzfs?"
    output = "how much money did lenny owe me for losing the bet for cracking the door code?"
    assert vignere_decrypt("billcook", input_str) == output
    # ANSWER: $150


def test_chapter_09():
    """The Kevin Mitnick Discount Plan"""
    input_str = "Hsle td esp epcx qzc dzqehlcp mfcypo zy esp nsta esle Yzglepw dpye xp?"
    output = "what is the term for software burned on the chip that novatel sent me?"
    assert caesar_shift(input_str, 15) == output
    # ANSWER: firmware


def test_chapter_10():
    """Mystery Hacker"""
    input_str = "Bprf cup esanqneu xmm gtknv amme U biiwy krxheu Iwqt Taied?"
    output = "what guy answered the phone when i first called eric heinz?"
    assert vignere_decrypt("firmware", input_str) == output
    # ANSWER: henry spiegel


def test_chapter_11():
    """Foul Play"""
    input_str = "Lwpi idlc sxs bn upiwtg axkt xc lwtc X bdkts xc lxiw wxb?"
    output = "what town did my father live in when i moved in with him?"
    assert caesar_shift(input_str, 11) == output
    # ANSWER: calabasas


def test_chapter_12():
    """You Can Never Hide"""
    input_str = "Yhlt xak tzg iytfrfad RanBfld squtpm uhst uquwd ce mswf tz wjrwtsr a wioe lhsv Ecid mwnlkoyee bmt oquwdo't ledn mp acomt?"
    output = "what was the internal pacbell system that could be used to wiretap a line that eric mentioned but wouldn't tell me about?"
    assert vignere_decrypt("calabasas", input_str) == output
    # ANSWER: switched access service (SAS)


def test_chapter_13():
    """The Wiretapper"""
    input_str = "Zkdw lv wkh qdph ri wkh SL ilup wkdw zdv zluhwdsshg eb Sdflif Ehoo?"
    output = "what is the name of the pi firm that was wiretapped by pacifc bell?"
    assert caesar_shift(input_str, 23) == output
    # ANSWER: teltec


def test_chapter_14():
    """You Tap Me, I Tap You"""
    input_str = "Plpki ytw eai rtc aaspx M llogw qj wef ms rh xq?"
    output = "where was the pay phone i asked my dad to go to?"
    assert vignere_decrypt("teltec", input_str) == output
    # ANSWER: village market, across the street


def test_chapter_15():
    """How the Fuck Did You Get That?\""""
    input_str = "Ituot oaybmzk ymwqe ftq pqhuoq ftmf Xqiue geqp fa buow gb mzk dmpua euszmxe zqmd Qduo?"
    output = "which company makes the device that lewis used to pick up any radio signals near eric?"
    assert caesar_shift(input_str, 14) == output
    # ANSWER: optoelectronics


def test_chapter_16():
    """Crashing Eric's Private Party"""
    input_str = "Kwth qzrva rbq lcq rxw Svtg vxcz zm vzs lbfieerl nsem rmh dg ac oef'l cwamu?"
    output = "what month and day did eric tell me the wiretaps were put on my dad's lines?"
    assert vignere_decrypt("optoelectronics", input_str) == output
    # ANSWER: january 27


def test_chapter_17():
    """Pulling Back the Curtain"""
    input_str = "Epib qa bpm vium wn bpm ixizbumvb kwuxtmf epmzm Q bziksml lwev Mzqk Pmqvh?"
    output = "what is the name of the apartment complex where i tracked down eric heinz?"
    assert caesar_shift(input_str, 18) == output
    # ANSWER: oakwood apartments


def test_chapter_18():
    """Traffic Analysis"""
    input_str = "Khkp wg wve kyfcqmm yb hvh TBS oeidr trwh Yhb MmCiwus wko ogvwgxar hr?"
    output = "what is the acronym of the fbi squad that ken mcguire was assigned to?"
    assert vignere_decrypt("oakwood", input_str) == output
    # ANSWER: wcc3


def test_chapter_19():
    """Revelations"""
    input_str = "Rcvo dn ivhz ja ocz omvinvxodji oj adiy v kzmnji'n njxdvg nzxpmdot iphwzm pndib oczdm ivhz viy yvoz ja wdmoc?"
    output = "what is name of the transaction to find a person's social security number using their name and date of birth?"
    assert caesar_shift(input_str, 5) == output
    # ANSWER: alphadent


def test_chapter_20():
    """Reverse Sting"""
    input_str = "Wspa wdw gae ypte rj gae dilan lbnsp loeui V tndllrhh gae awvnh \"HZO, hzl jaq M uxla nvu?\""
    output = "what was the name of the steak house where i answered the phone \"dmv, how can i help you?\""
    assert vignere_decrypt("alphadent", input_str) == output
    # ANSWER: bob burns


def test_chapter_21():
    """Cat and Mouse"""
    input_str = "4A 75 6E 67 20 6A 6E 66 20 62 68 65 20 61 76 70 78 61 6E 7A 72 20 74 76 69 72 61 20 67 62 20 47 72 65 65 6C 20 55 6E 65 71 6C 3F"
    output = "what was our nickname given to terry hardy?"
    res = bytearray.fromhex(input_str.replace(" ", "")).decode()
    assert caesar_shift(res, 13) == output
    # ANSWER: klingon


def test_chapter_22():
    """Detective Work"""
    input_str = "Gsig cof dsm fkqeoe vnss jo farj tbb epr Csyvd Nnxub mzlr ut grp lne?"
    output = "what was the secret name we used for the wells fargo code of the day?"
    assert vignere_decrypt("klingon", input_str) == output
    # ANSWER: kat


def test_chapter_23():
    """Raided"""
    input_str = "Fqjc nunlcaxwrl mnerln mrm cqn OKR rwcnwcrxwjuuh kanjt fqnw cqnh bnjalqnm vh jyjacvnwc rw Ljujkjbjb?"
    output = "what electronic device did the fbi intentionally break when they searched my apartment in calabasas?"
    assert caesar_shift(input_str, 17) == output
    # ANSWER: boombox


def test_chapter_24():
    """Vanishing Act"""
    input_str = "Xvof jg qis bmns lg hvq thlss ktffb J cifsok EAJ uojbthwsbhlsg?"
    output = "what is the name of the store where i outran dmv investigators?"
    assert vignere_decrypt("boombox", input_str) == output
    # ANSWER: kinko's


def test_chapter_25():
    """Harry Houdini"""
    input_str = "Cngz zuct ngy znk grsg sgzkx lux znk xkgr Kxoi Ckoyy?"
    output = "what town has the alma mater for the real eric weiss?"
    assert caesar_shift(input_str, 20) == output
    # ANSWER: ellensburg


def test_chapter_26():
    """Private Investigator"""
    input_str = "Aslx jst nyk rlxi bx ns wgzzcmgw UP jnsh hlrjf nyk TT seq s cojorpdw pssx gxmyeie ao bzy glc?"
    output = "what was the name of my favorite tv show where the pi had a business card printer in his car?"
    assert vignere_decrypt("ellensburg", input_str) == output
    # ANSWER: the rockford files


def test_chapter_27():
    """Here Comes the Sun"""
    input_str = "85 102 121 114 32 103 113 32 114 102 99 32 108 121 107 99 32 109 100 32 114 102 99 32 122 109 109 105 113 114 109 112 99 32 71 32 100 112 99 111 115 99 108 114 99 98 32 103 108 32 66 99 108 116 99 112 63"
    output = "what is the name of the bookstore i frequented in denver?"
    res = "".join(map(lambda x: chr(int(x)), input_str.split()))
    assert caesar_shift(res, 2) == output
    # ANSWER: the tattered cover


def test_chapter_28():
    """Trophy Hunter"""
    input_str = "Phtm zvvvkci sw mhx Fmtvr VOX Ycmrt Emki vqimgv vowx hzh L cgf Ecbst ysi?"
    output = "what version of the micro tac ultra lite source code did i ask alisa for?"
    assert vignere_decrypt("tatteredcover", input_str) == output
    # ANSWER: doc2


def test_chapter_29():
    """Departure"""
    input_str = "126 147 172 163 040 166 172 162 040 154 170 040 157 172 162 162 166 156 161 143 040 145 156 161 040 163 147 144 040 115 156 165 144 153 153 040 163 144 161 154 150 155 172 153 040 162 144 161 165 144 161 040 150 155 040 122 172 155 040 111 156 162 144 077"
    output = "what was my password for the novell terminal server in san jose?"
    res = "".join(map(lambda x: chr(int(x, 8)), input_str.split()))
    assert caesar_shift(res, 1) == output
    # ANSWER: snowbird


def test_chapter_30():
    """Blindsided"""
    input_str = "Ouop lqeg gs zkds ulv V deds zq lus DS urqstsn't wwiaps?"
    output = "what kind of lock did i pick in the hr manager's office?"
    assert vignere_decrypt("snowbird", input_str) == output
    # ANSWER: wafer


def test_chapter_31():
    """Eyes in the Sky"""
    input_str = "Alex B25 rixasvo hmh M ywi xs gsrrigx xs xli HQZ qemrjveqi?"
    output = "what x25 network did i use to connect to the dmv mainframe?"
    assert caesar_shift(input_str, 22)
    # ANSWER: gte telenet


def test_chapter_32():
    """Sleepless in Seattle"""
    input_str = "Caem alw Ymek Xptq'd tnwlchvw xz lrv lkkzxv?"
    output = "what was lile elam's password to her server?"
    assert vignere_decrypt("gtetelenet", input_str) == output
    # ANSWER: m00n$@earth


def test_chapter_33():
    """Hacking the Samurai"""
    input_str = "Ozg ojglw lzw hshwj gf AH Khggxafy lzsl BKR skcwv ew stgml?"
    output = "who wrote the paper on ip spoofing that jsz asked me about?"
    assert caesar_shift(input_str, 8) == output
    # ANSWER: robert morris


def test_chapter_34():
    """Hiding in the Bible Belt"""
    input_str = "Nvbx nte hyv bqgs pj gaabv jmjmwdi whd hyv UVT'g Giuxdoc Gctcwd Hvyqbuvz hycoij?"
    output = "what was the type of phone service for the mdc's federal public defender phones?"
    assert vignere_decrypt("robertmorris", input_str) == output
    # ANSWER: direct connect


def test_chapter_35():
    """Game Over"""
    input_str = "2B 2T W 2X 2Z 36 36 2P 36 2V 3C W 3A 32 39 38 2Z W 3D 33 31 38 2V 36 3D W 2R 2Z W 3E 3C 2V 2X 2Z 2Y W 3E 39 W 2R 32 2V 3E W 2V 3A 2V 3C 3E 37 2Z 38 3E W 2X 39 37 3A 36 2Z 2S 1R"
    output = "my cellular phone signals we traced to what apartment complex?"
    # Base36 decode the input string.
    res = "".join(map(lambda x: chr(int(x, 36)), input_str.split()))
    assert caesar_shift(res, 20) == output
    # ANSWER: players club


def test_chapter_36():
    """An FBI Valentine"""
    input_str = "Lsar JSA cryoi ergiu lq wipz tnrs dq dccfunaqi zf oj uqpctkiel dpzpgp I jstcgo cu dy hgq?"
    output = "what fbi agent tried to look into my briefcase in my apartment before i locked it on him?"
    assert vignere_decrypt("playersclub", input_str) == output
    # ANSWER: daniel glasgow


def test_chapter_37():
    """Winning the Scapegoat Sweepstakes"""
    input_str = "V2hhdCBGQkkgYWdlbnQgYXNrZWQgU3VuIE1pY3Jvc3lzdGVtcyB0byBjbGFpbSB0aGV5IGxvc3QgODAgbWlsbGlvbiBkb2xsYXJzPw=="
    output = "What FBI agent asked Sun Microsystems to claim they lost 80 million dollars?"
    assert base64.b64decode(input_str).decode("ascii") == output
    # ANSWER: kathleen carson


def test_chapter_38():
    """Aftermath: A Reversal of Fortune"""
    input_str = "100-1111-10-0 011-000-1-111 00-0100 1101-10-1110-000-101-11-0-1 0111-110-00-1001-1-101 111-0-11-0101-010-1-101 111-10-0100 11-00-11"
    output = "what does my favorite bumper sticker say imi"
    res = " ".join([
        morse_decode(word.replace("-", " ").replace("0", "-").replace("1", "."))
        for word in input_str.split()
    ])
    assert res == output
    # ANSWER: free kevin?
