# coding: utf-8
import logging

from sqlalchemy import Column, Enum, Float, ForeignKey, String
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
import sys

from maha_cet_parser.admission_enums import SeatType, STATE_LEVEL

Base = declarative_base()
metadata = Base.metadata


def buildInsert(objects=None, db_url=None):
    # an Engine, which the Session will use for connection
    # resources
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
    logger = logging.getLogger(__name__)
    try:
        some_engine = create_engine(db_url)

        # create a configured "Session" class
        Session = sessionmaker(bind=some_engine)

        # create a Session
        session = Session()
        session.add_all(objects)
        # work with sess
        # session.bulk_save_objects(objects)
        session.commit()
    except:
        logger.exception("Fatal error in main loop" + str(sys.exc_info()))
    finally:
        pass


class Student(Base):
    __tablename__ = 'student'

    id = Column(INTEGER(11), primary_key=True)
    rank = Column(INTEGER(11), nullable=False)
    mhcet_score = Column(Float, nullable=False)
    mhcet_application_id = Column(String(20), nullable=False, unique=True)
    candidate_name = Column(String(40), nullable=False)
    gender = Column(Enum('MALE', 'FEMALE', 'INTERSEX'))
    seat_type = Column(
        Enum('DEFSEBCS', 'PWDVJH', 'GSEBCS', 'ORPHAN', 'LSEBCO', 'PWDNT2H', 'LVJO', 'PWDSCS', 'LOPENS', 'GOPENO',
             'PWDNT3H', 'GSCS', 'LNT3O', 'PWDOPEN', 'PWDSTH', 'GNT1H', 'DEFSCS', 'DEFVJS', 'GVJH', 'GSTS', 'TFWS',
             'LNT1S', 'GSCO', 'LVJS', 'PWDSCH', 'GNT3S', 'LOBCH', 'LSTS', 'LOBCS', 'GNT1O', 'GVJS', 'GSCH', 'PWDSEBC',
             'PWDOPENS', 'GNT1S', 'GOBCH', 'GSTH', 'LOPENO', 'PWDOPENH', 'LOBCO', 'PWDNT2S', 'LSEBCH', 'GNT2S', 'LNT2O',
             'PWDOBCH', 'GOBCO', 'PWDSEBCH', 'LSEBCS', 'LSCH', 'GSTO', 'LSCO', 'LNT3H', 'GOPENH', 'GOPENS', 'DEFOBCS',
             'LNT2H', 'DEFNT1S', 'EWS', 'DEFSTS', 'GSEBCO', 'PWDOBCS', 'GNT2H', 'PWDVJS', 'LSTO', 'LNT1H', 'LNT3S',
             'LSTH', 'GVJO', 'PWDSEBCS', 'LNT1O', 'PWDSTS', 'GSEBCH', 'DEFNT2S', 'MI', 'LOPENH', 'PWDNT3S', 'GOBCS',
             'LSCS', 'GNT2O', 'PWDNT1H', 'LVJH', 'LNT2S', 'GNT3O', 'DEFOPENS', 'GNT3H', 'DEFNT3S', 'PWDNT1S'))


class University(Base):
    __tablename__ = 'university'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(400), unique=True)
    name = Column(String(100), nullable=False)
    city = Column(String(400))

    def __eq__(self, other):
        """Overrides the default implementation"""
        print("Coming here")
        if isinstance(other, Collage):
            return self.code == other.code
        return False

    # def __ne__(self, other):
    #     """Overrides the default implementation (unnecessary in Python 3)"""
    #     x = self.__eq__(other)
    #     if x is not NotImplemented:
    #         return not x
    #     return NotImplemented

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self):
        return self.__tablename__ + " : " + str(self.name)


class Collage(Base):
    __tablename__ = 'collage'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(400), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    # status = Column(String(400), nullable=True)
    home_university = Column(ForeignKey('university.id'), nullable=False, index=True)
    city = Column(String(40), nullable=False)

    university = relationship('University', cascade="save-update")

    def printName(self):
        print(self.__tablename__ + " : " + self.name)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Collage):
            return self.code == other.code
        return False

    # def __ne__(self, other):
    #     """Overrides the default implementation (unnecessary in Python 3)"""
    #     x = self.__eq__(other)
    #     if x is not NotImplemented:
    #         return not x
    #     return NotImplemented

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self):
        return self.__tablename__ + " : " + str(self.code) + ' - ' + str(self.name)


class Admission(Base):
    __tablename__ = 'admission'

    id = Column(INTEGER(11), primary_key=True)
    admission_year = Column(String(16), nullable=False)
    admissionCutoff = Column(INTEGER(11), nullable=False)


class Branch(Base):
    __tablename__ = 'branch'

    id = Column(INTEGER(11), primary_key=True)
    collage_code = Column(ForeignKey('collage.id'), nullable=False, index=True)
    code = Column(String(400), nullable=False, unique=True)
    # admission_details = Column(ForeignKey('admission.id'), index=True)
    status = Column(String(400), nullable=True)
    name = Column(String(400), nullable=False)
    # admission = relationship('Admission')
    collage = relationship('Collage', cascade="save-update")

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Branch):
            return self.code == other.code
        return False

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self):
        return self.__tablename__ + " : " + str(self.code) + ' - ' + str(self.name)


class Admissioncutoff(Base):
    __tablename__ = 'admissioncutoff'

    id = Column(INTEGER(11), primary_key=True)
    # seat_type = Column(
    #     Enum('DEFSEBCS', 'PWDVJH', 'GSEBCS', 'ORPHAN', 'LSEBCO', 'PWDNT2H', 'LVJO', 'PWDSCS', 'LOPENS', 'GOPENO',
    #          'PWDNT3H', 'GSCS', 'LNT3O', 'PWDOPEN', 'PWDSTH', 'GNT1H', 'DEFSCS', 'DEFVJS', 'GVJH', 'GSTS', 'TFWS',
    #          'LNT1S', 'GSCO', 'LVJS', 'PWDSCH', 'GNT3S', 'LOBCH', 'LSTS', 'LOBCS', 'GNT1O', 'GVJS', 'GSCH', 'PWDSEBC',
    #          'PWDOPENS', 'GNT1S', 'GOBCH', 'GSTH', 'LOPENO', 'PWDOPENH', 'LOBCO', 'PWDNT2S', 'LSEBCH', 'GNT2S', 'LNT2O',
    #          'PWDOBCH', 'GOBCO', 'PWDSEBCH', 'LSEBCS', 'LSCH', 'GSTO', 'LSCO', 'LNT3H', 'GOPENH', 'GOPENS', 'DEFOBCS',
    #          'LNT2H', 'DEFNT1S', 'EWS', 'DEFSTS', 'GSEBCO', 'PWDOBCS', 'GNT2H', 'PWDVJS', 'LSTO', 'LNT1H', 'LNT3S',
    #          'LSTH', 'GVJO', 'PWDSEBCS', 'LNT1O', 'PWDSTS', 'GSEBCH', 'DEFNT2S', 'MI', 'LOPENH', 'PWDNT3S', 'GOBCS',
    #          'LSCS', 'GNT2O', 'PWDNT1H', 'LVJH', 'LNT2S', 'GNT3O', 'DEFOPENS', 'GNT3H', 'DEFNT3S', 'PWDNT1S'))
    seat_type = Column(Enum(SeatType))
    rank = Column(Float, nullable=False)
    merit_score = Column(Float, nullable=False)
    branch_code = Column(ForeignKey('branch.id'), nullable=False, index=True)
    level = Column(String(400), nullable=False, default=STATE_LEVEL)
    stage = Column(String(400), nullable=False)
    round = Column(String(400), nullable=False)
    admission_year = Column(String(16), nullable=True)
    branch = relationship('Branch')

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Admissioncutoff):
            return self.admission_year == other.admission_year and self.branch.code == other.branch.code
        return False

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self):
        return self.__tablename__ + " : " + str(self.seat_type.name) + ' - ' + str(self.rank) + ' - ' + \
               str(self.merit_score) + ' - ' + str(self.branch_code) + ' - ' + str(self.level) + ' - ' + \
               str(self.stage) + ' - ' + str(self.round)
