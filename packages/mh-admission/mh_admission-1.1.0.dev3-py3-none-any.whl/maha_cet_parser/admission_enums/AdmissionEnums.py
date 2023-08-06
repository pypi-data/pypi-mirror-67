from enum import unique, Enum, auto

HOME_UNIVERSITY_SEATS_ALLOTTED_TO_HOME_UNIVERSITY_CANDIDATES = "Home University Seats Allotted to Home University " \
                                                               "Candidates"
HOME_UNIVERSITY_SEATS_ALLOTTED_TO_OTHER_THAN_HOME_UNIVERSITY_CANDIDATES = "Home University Seats Allotted to Other " \
                                                                          "Than Home University Candidates"
OTHER_THAN_HOME_UNIVERSITY_SEATS_ALLOTTED_TO_HOME_UNIVERSITY_CANDIDATES = "Other Than Home University Seats Allotted " \
                                                                          "to Home University Candidates"
OTHER_THAN_HOME_UNIVERSITY_SEATS_ALLOTTED_TO_OTHER_THAN_HOME_UNIVERSITY_CANDIDATES = "Other Than Home University " \
                                                                                     "Seats Allotted to Other Than " \
                                                                                     "Home University Candidates"

STATE_LEVEL = "State Level"


# Legends for SeatType : H-Home University, O-Other than Home University,S-State Level, G-General, L-Ladies, AI-All India
# Legends:Start Character G-General, L-Ladies, End Character H-Home University, O-Other than Home University, S-State Level
# Maharashtra State Seats - Cut Off Indicates State General Merit No. ; Figures in bracket Indicates MHT-CET PCM Percentile
# F:Only For Female, K:Konkan Seats, HU:Home University, OHU:Other than Home University, PWD:Persons with Disabilities seats
# carved out from HU/SL, DEF:Defence seats carved out from OHU/SL
# Economically Weaker Section (EWS) Seats
@unique
class SeatType(Enum):
    DEFSEBCS = 'DEFSEBCS'
    PWDVJH = 'PWDVJH'
    GSEBCS = 'GSEBCS'
    ORPHAN = 'ORPHAN'
    LSEBCO = 'LSEBCO'
    PWDNT2H = 'PWDNT2H'
    LVJO = 'LVJO'
    PWDSCS = 'PWDSCS'
    LOPENS = 'LOPENS'
    GOPENO = 'GOPENO'
    PWDNT3H = 'PWDNT3H'
    GSCS = 'GSCS'
    LNT3O = 'LNT3O'
    PWDOPEN = 'PWDOPEN'
    PWDSTH = 'PWDSTH'
    GNT1H = 'GNT1H'
    DEFSCS = 'DEFSCS'
    DEFVJS = 'DEFVJS'
    GVJH = 'GVJH'
    GSTS = 'GSTS'
    TFWS = 'TFWS'
    LNT1S = 'LNT1S'
    GSCO = 'GSCO'
    LVJS = 'LVJS'
    PWDSCH = 'PWDSCH'
    GNT3S = 'GNT3S'
    LOBCH = 'LOBCH'
    LSTS = 'LSTS'
    LOBCS = 'LOBCS'
    GNT1O = 'GNT1O'
    GVJS = 'GVJS'
    GSCH = 'GSCH'
    PWDSEBC = 'PWDSEBC'
    PWDOPENS = 'PWDOPENS'
    GNT1S = 'GNT1S'
    GOBCH = 'GOBCH'
    GSTH = 'GSTH'
    LOPENO = 'LOPENO'
    PWDOPENH = 'PWDOPENH'
    LOBCO = 'LOBCO'
    PWDNT2S = 'PWDNT2S'
    LSEBCH = 'LSEBCH'
    GNT2S = 'GNT2S'
    LNT2O = 'LNT2O'
    PWDOBCH = 'PWDOBCH'
    GOBCO = 'GOBCO'
    PWDSEBCH = 'PWDSEBCH'
    LSEBCS = 'LSEBCS'
    LSCH = 'LSCH'
    GSTO = 'GSTO'
    LSCO = 'LSCO'
    LNT3H = 'LNT3H'
    GOPENH = 'GOPENH'
    GOPENS = 'GOPENS'
    DEFOBCS = 'DEFOBCS'
    LNT2H = 'LNT2H'
    DEFNT1S = 'DEFNT1S'
    EWS = 'EWS'
    DEFSTS = 'DEFSTS'
    GSEBCO = 'GSEBCO'
    PWDOBCS = 'PWDOBCS'
    GNT2H = 'GNT2H'
    PWDVJS = 'PWDVJS'
    LSTO = 'LSTO'
    LNT1H = 'LNT1H'
    LNT3S = 'LNT3S'
    LSTH = 'LSTH'
    GVJO = 'GVJO'
    PWDSEBCS = 'PWDSEBCS'
    LNT1O = 'LNT1O'
    PWDSTS = 'PWDSTS'
    GSEBCH = 'GSEBCH'
    DEFNT2S = 'DEFNT2S'
    MI = 'MI'
    LOPENH = 'LOPENH'
    PWDNT3S = 'PWDNT3S'
    GOBCS = 'GOBCS'
    LSCS = 'LSCS'
    GNT2O = 'GNT2O'
    PWDNT1H = 'PWDNT1H'
    LVJH = 'LVJH'
    LNT2S = 'LNT2S'
    GNT3O = 'GNT3O'
    DEFOPENS = 'DEFOPENS'
    GNT3H = 'GNT3H'
    DEFNT3S = 'DEFNT3S'
    PWDNT1S = 'PWDNT1S'
    PWDC = 'PWDC'
    PWD2 = 'PWD2'
    PWD1 = 'PWD1'
    PWD3 = 'PWD3'
    DEFS = 'DEFS'


@unique
class Gender(Enum):
    MALE = auto()
    FEMALE = auto()
    INTERSEX = auto()


@unique
class CapRound(Enum):
    CAP_ROUND_1 = auto()
    CAP_ROUND_2 = auto()
    CAP_ROUND_3 = auto()


# import re
# a = "55138A"
# result = re.sub('[^0-9]','', a)
# print(result)
#
# s = "510023(21.32)"
#
# print(re.search(r'\(([^\)]+)\)',s).group(1))
#
# print(re.search(r'(?<!\()\b\w+\b(?![\)])',s).group(0))
#
# print(re.search(r'(?<!\()\b\w+\b(?![\)])', s))

