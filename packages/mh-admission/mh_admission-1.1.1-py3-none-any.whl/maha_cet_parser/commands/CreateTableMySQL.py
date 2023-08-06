import calendar
import logging
import os
import tempfile
import time

from sqlalchemy import MetaData, Integer, Table, Column, String, ForeignKey, Float, Enum, TEXT
from sqlalchemy import create_engine

from maha_cet_parser.admission_enums import SeatType, Gender, STATE_LEVEL
from .Commands import Command


def get_metadata():
    metadata = MetaData()

    universityTable = Table('university', metadata,
                            Column('id', Integer, primary_key=True, autoincrement=True),
                            Column('code', String(length=400), unique=True),
                            Column('name', TEXT, nullable=False),
                            Column('city', String(length=400)),
                            )

    collageTable = Table('collage', metadata,
                         Column('id', Integer, primary_key=True, autoincrement=True),
                         Column('code', String(length=400), unique=True),
                         Column('name', String(length=400)),
                         Column('home_university', Integer, ForeignKey("university.id"), default='NULL'),
                         Column('city', String(length=400)),
                         # Enum
                         #Column('status', String(400), nullable=True),
                         )

    # admissionTable = Table('admission', metadata,
    #                        Column('id', Integer, primary_key=True, autoincrement=True ),
    #
    #                        Column('admissionCutoff', Integer, nullable=False),
    #                        )

    branchTable = Table('branch', metadata,
                        Column('id', Integer, primary_key=True, autoincrement=True),
                        Column('collage_code', Integer, ForeignKey("collage.id"), default='NULL'),
                        Column('code', String(length=400), nullable=False, unique=True),
                        # Column('admission_details', Integer, ForeignKey("admission.id")),
                        Column('name', String(length=400)),
                        # add status enum
                        Column('status', String(400), nullable=True),
                        )

    # availableseatsTable = Table ( 'availableseats', metadata,
    #                               # seat_cap
    #                               # choice_code
    #                               # branch_code
    #                               # category
    #                               # enum (G+L)
    #                               # SI
    #                               # MS seath
    #                               # minority_seats
    #                               # All India
    #                               # Institue Seats
    #                               # level (state_level)
    #                               # TFWS choice code
    #                               # TFWS seats)

    admissioncutoffTable = Table('admissioncutoff', metadata,
                                 Column('id', Integer, primary_key=True, autoincrement=True),
                                 Column('seat_type', Enum(SeatType)),
                                 Column('rank', Float, nullable=False, default='NULL'),
                                 Column('merit_score', Float, nullable=False, default='NULL'),
                                 Column('branch_code', Integer, ForeignKey("branch.id"), default='NULL'),
                                 Column('admission_year', String(16), nullable=False, default='NULL'),
                                 # Enum
                                 Column('level', String(400), nullable=False, default=STATE_LEVEL),
                                 Column('stage', String(400), nullable=False, default='NULL'),
                                 Column('round', String(400), nullable=False, default='NULL')
                                 )

    studentTable = Table('student', metadata,
                         Column('id', Integer, primary_key=True),
                         Column('rank', Integer, nullable=False),
                         Column('mhcet_score', Float, nullable=False),
                         Column('mhcet_application_id', String(20), nullable=False, unique=True),
                         Column('candidate_name', String(40), nullable=False),
                         # enum
                         Column('gender', Enum(Gender)),
                         Column('candidate_category', String(40), nullable=False),
                         Column('seat_type', Enum(SeatType))
                         )
    return metadata


class CreateTableMySQL(Command):
    def __init__(self, args):
        '''Intialize the object by using the arguments from argparse'''
        Command.__init__(self, args)
        self.load_arg_or_default(args, 'db_dialect')
        self.load_arg_or_default(args, 'db_driver')
        self.load_arg_or_default(args, 'db_username')
        self.load_arg_or_default(args, 'db_password')
        self.load_arg_or_default(args, 'db_hostname')
        self.load_arg_or_default(args, 'db_port')
        self.load_arg_or_default(args, 'db_name')

        self.ts = calendar.timegm(time.gmtime())

        # Logger
        self.logger = logging.getLogger(__name__)
        self.logsDir = os.path.join(tempfile.gettempdir(), 'maha_cet_admission', 'logs')
        if not os.path.exists(self.logsDir):
            os.makedirs(self.logsDir)

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    @staticmethod
    def add_args(subparsers):
        # Top-level parser for this command
        parser = subparsers.add_parser("eng",help='Argument for Engineering admission')
        subparsers2 = parser.add_subparsers(help='Argument for Engineering admission')

        # Create Data base schema
        populatedb_parser = subparsers2.add_parser("create_tables")
        populatedb_parser.add_argument("-d", "--db_dialect", help="Database dialect Name",
                                       env_var="DATABASE_DIALECT_NAME", default="mysql")
        populatedb_parser.add_argument("-dd", "--db_driver", help="Database driver", env_var="DATABASE_DRIVER_NAME",
                                       default="pymysql")
        populatedb_parser.add_argument("-u", "--db_username", help="Database user name", env_var="DATABASE_USER_NAME",
                                       default="root")
        populatedb_parser.add_argument("-p", "--db_password", help="Database user password",
                                       env_var="DATABASE_USER_PASSWORD", default="root")
        populatedb_parser.add_argument("-host", "--db_hostname", help="Database host name", env_var="DATABASE_HOSTNAME",
                                       default="localhost")
        populatedb_parser.add_argument("-dp", "--db_port", help="Database port", env_var="DATABASE_PORT",
                                       default="3306")
        populatedb_parser.add_argument("-n", "--db_name", help="Database connection name", env_var="DB_SID_NAME",
                                       default="admissiondb")

        populatedb_parser.set_defaults(func=CreateTableMySQL.create_db_tables)

    # @staticmethod
    # def add_common_args(parser, arglist=None, required_override=True):
    #     """Parse the common command line arguments """
    #     pass

    def get_engine_url(self):
        engine_url = self.db_dialect + "+" + self.db_driver + "://" + \
                     self.db_username + ":" + self.db_password + "@" + \
                     self.db_hostname + ":" + self.db_port + "/" + \
                     self.db_name

        self.logger.info("Database Engine url is")
        self.logger.info(engine_url)
        return engine_url

    def get_engine(self):
        engine_url = self.get_engine_url()
        engine = create_engine(engine_url)

        return engine

    def run_create_db_tables(self):
        logfileName = "create_db_tables_" + str(self.ts) + ".log"
        log_file_name = os.path.join(self.logsDir, logfileName)
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                            level=logging.INFO,
                            handlers=[
                                logging.FileHandler(log_file_name, mode='w', encoding=None, delay=False),
                                logging.StreamHandler()
                            ])

        logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG )
        try:

            engine = self.get_engine()
            metadata = get_metadata()

            metadata.create_all(engine)

            self.logger.info(tempfile.gettempdir())
            self.logger.info("Succesfully created database following tables")
            self.logger.info(engine.table_names())
        except Exception:
            self.logger.exception("Fatal error in main loop"+ Exception.message)
        finally:
            self.logger.info("Details Logs available at " + log_file_name)

    @staticmethod
    def create_db_tables(args):
        utils = CreateTableMySQL(args)
        utils.run_create_db_tables()
