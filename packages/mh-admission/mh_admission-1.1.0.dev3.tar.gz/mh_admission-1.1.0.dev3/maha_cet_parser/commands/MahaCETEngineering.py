import calendar
import logging
import os
import re
import tempfile
import time
from pathlib import Path

from xlrd import open_workbook

import maha_cet_parser.db.db as dbutils
from maha_cet_parser.db.db import Branch, Collage, University, Admissioncutoff

from maha_cet_parser.admission_enums.AdmissionEnums import STATE_LEVEL
from maha_cet_parser.admission_enums.AdmissionEnums import HOME_UNIVERSITY_SEATS_ALLOTTED_TO_HOME_UNIVERSITY_CANDIDATES
from maha_cet_parser.admission_enums.AdmissionEnums import \
    HOME_UNIVERSITY_SEATS_ALLOTTED_TO_OTHER_THAN_HOME_UNIVERSITY_CANDIDATES
from maha_cet_parser.admission_enums.AdmissionEnums import \
    OTHER_THAN_HOME_UNIVERSITY_SEATS_ALLOTTED_TO_HOME_UNIVERSITY_CANDIDATES
from maha_cet_parser.admission_enums.AdmissionEnums import \
    OTHER_THAN_HOME_UNIVERSITY_SEATS_ALLOTTED_TO_OTHER_THAN_HOME_UNIVERSITY_CANDIDATES
from maha_cet_parser.admission_enums.AdmissionEnums import SeatType

from .Commands import Command

m_footer_starting = 'Legends:'


def has_header(sheet=None):
    rowlist = sheet.row_values(0)
    hasheader = False
    if 'Government of Maharashtra' in rowlist:
        hasheader = True
    return hasheader


def is_header_started(row=None):
    is_header = False
    if 'Government of Maharashtra' in row:
        is_header = True
    return is_header


def get_branch_status(sheet=None, branch=None, rowindex=None):
    rowlist = sheet.row_values(rowindex + 1)
    rowlist = list(filter(None, rowlist))
    branch_status = None
    if (rowlist[0].startswith('Status:')) and (not rowlist[1].startswith('Home University :')):
        if 'Home University :' in rowlist[1]:
            branch_status = rowlist[1][0:rowlist[1].find('Home University :')]
        else:
            branch_status = rowlist[1]

    return branch_status


class MahaCETEngineering(Command):
    def __init__(self, args):
        '''Intialize the object by using the arguments from argparse'''
        Command.__init__(self, args)
        self.load_arg_or_default(args, 'resource_location')
        self.load_arg_or_default(args, 'enggineering')
        self.load_arg_or_default(args, 'engg_be')
        self.load_arg_or_default(args, 'engg_me')
        self.load_arg_or_default(args, 'engg_both')
        self.load_arg_or_default(args, 'do_insert')

        self.load_arg_or_default(args, 'db_dialect')
        self.load_arg_or_default(args, 'db_driver')
        self.load_arg_or_default(args, 'db_username')
        self.load_arg_or_default(args, 'db_password')
        self.load_arg_or_default(args, 'db_hostname')
        self.load_arg_or_default(args, 'db_port')
        self.load_arg_or_default(args, 'db_name')

        self.universitynametoobj = {}
        self.collage = set()
        self.collagenameToObj = {}
        self.universityToCollage = {}
        self.collagetouniversity = {}
        self.branchCodeToBranch = {}
        self.collageCodeToCollage = {}
        self.admission_cut_off_list = []

        self.ts = calendar.timegm(time.gmtime())
        self.cap_round = None
        self.admission_year = None
        self.collage_row_no = 4

        self.seat_type_enum_list = list(map(lambda c: c.value, SeatType))
        self.seat_type_enum_set = set(self.seat_type_enum_list)
        # Logger
        self.logger = logging.getLogger(__name__)
        self.logsDir = os.path.join(tempfile.gettempdir(), 'maha_cet_admission', 'logs')
        if not os.path.exists(self.logsDir):
            os.makedirs(self.logsDir)

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    @staticmethod
    def add_args(subparsers):
        parser = subparsers.add_parser("populate_db", help='Argument to populate database with engineering admission '
                                                           'data')

        resource_default_path = os.path.abspath(
            os.path.join(os.path.dirname(Path(os.path.abspath(__file__)).parent),
                         "resources"))

        parser.add_argument("-r", "--resource_location", help="Excel file location for Admission data",
                            env_var="RESOURCE_ROOT_LOCATION", default=resource_default_path)

        parser.add_argument("-d", "--db_dialect", help="Database dialect Name",
                            env_var="DATABASE_DIALECT_NAME", default="mysql")
        parser.add_argument("-dd", "--db_driver", help="Database driver", env_var="DATABASE_DRIVER_NAME",
                            default="pymysql")
        parser.add_argument("-u", "--db_username", help="Database user name", env_var="DATABASE_USER_NAME",
                            default="root")
        parser.add_argument("-p", "--db_password", help="Database user password",
                            env_var="DATABASE_USER_PASSWORD", default="root")
        parser.add_argument("-host", "--db_hostname", help="Database host name", env_var="DATABASE_HOSTNAME",
                            default="localhost")
        parser.add_argument("-dp", "--db_port", help="Database port", env_var="DATABASE_PORT",
                            default="3306")
        parser.add_argument("-n", "--db_name", help="Database connection name", env_var="DB_SID_NAME",
                            default="admissiondb")

        parser.add_argument("-engg", "--enggineering", action='store_true',
                            help="Flag to populate engineering admission data available ")

        parser.add_argument("-be", "--engg_be", action='store_true',
                            help="Flag to populate engineering admission data For Bachelor Of Engineering ")

        # parser.add_argument("-me", "--engg_me", action='store_true',
        #                     help="Flag to populate engineering admission data for Master Of Engineering, "
        #                          "Note: Not enable now")
        #
        # parser.add_argument("-b", "--engg_both", action='store_true',
        #                     help="Flag to populate engineering admission data Bachelor and Master of Engineering, "
        #                          "Note: Not enable now ")

        parser.add_argument("-i", "--do_insert", action='store_true',
                            help="Flag not to populate engineering admission")

        parser.set_defaults(func=MahaCETEngineering.populate_db)

    def dump_objects(self, objects=None):
        for object in objects:
            self.logger.info(object)

    @staticmethod
    def add_common_args(parser, arglist=None, required_override=True):
        """Parse the common command line arguments """
        pass

    def get_engine_url(self):
        engine_url = self.db_dialect + "+" + self.db_driver + "://" + \
                     self.db_username + ":" + self.db_password + "@" + \
                     self.db_hostname + ":" + self.db_port + "/" + \
                     self.db_name

        self.logger.info("Database Engine url is")
        self.logger.info(engine_url)
        return engine_url

    def get_university(self, sheet=None):
        l_university = None

        if has_header(sheet):
            universityrow = sheet.row_values(6)

            for universityname in universityrow:
                if 'Home University : ' in universityname:
                    name = universityname.replace('Home University : ', "").replace("Un-Aided ", "")
                    keys = list(self.universitynametoobj.keys())
                    if name in keys:
                        l_university = self.universitynametoobj[name]
                    else:
                        l_university = University()
                        l_university.name = name
                        self.universitynametoobj[name] = l_university
        return l_university

    def get_collage(self, sheet=None):
        collage = Collage()
        if has_header(sheet):
            rowlist = sheet.row_values(self.collage_row_no)
            splitted = rowlist[0].split()

            collageCode_l = splitted[0]

            keys = list(self.collageCodeToCollage.keys())
            if collageCode_l in keys:
                collage = self.collageCodeToCollage[collageCode_l]
                if collage.university is None:
                    university = self.get_university(sheet=sheet)
                    collage.university = university
            else:
                collage.code = collageCode_l
                collage.city = splitted[len(splitted) - 1].replace('.', '')
                namestring = ''
                for row in rowlist:
                    namestring = namestring + ' ' + str(row)
                    namestring = namestring.strip()
                namestring = namestring.strip()
                namestring = namestring.replace(collageCode_l + ' - ', "")
                collage.name = namestring
                self.collageCodeToCollage[collage.code] = collage
                university = self.get_university(sheet=sheet)

                self.logger.info("Processing for University :- " + str(university))
                if not (namestring in self.collagetouniversity.keys()):
                    self.collagetouniversity[collage.name] = university

                collage.university = self.collagetouniversity[collage.name]

        return collage

    def is_footer_started(self, row=None):
        is_footer = False
        if row[0].startswith(m_footer_starting):
            is_footer = True
        return is_footer

    def is_row_for_collage(self, sheet=None, collage=None, rowindex=None):
        is_collage = False
        rowlist = sheet.row_values(rowindex)
        if rowlist[0].startswith(collage.code):
            is_collage = True
        return is_collage

    def is_row_for_branch(self, sheet=None, branch=None, rowindex=None):
        is_branch = False
        rowlist = sheet.row_values(rowindex)
        if rowlist[0].startswith(branch.code):
            is_branch = True
        return is_branch

    def is_row_for_stage(self, sheet=None, rowindex=None):
        is_stage = False
        rowlist = sheet.row_values(rowindex)
        if rowlist[0].startswith('Stage'):
            is_stage = True
        return is_stage

    def is_row_for_level(self, sheet=None, rowindex=None):
        is_level = False
        rowlist = sheet.row_values(rowindex)
        admission_level = rowlist[0]

        if admission_level == STATE_LEVEL:
            is_level = True
        elif admission_level == HOME_UNIVERSITY_SEATS_ALLOTTED_TO_HOME_UNIVERSITY_CANDIDATES:
            is_level = True
        elif admission_level == HOME_UNIVERSITY_SEATS_ALLOTTED_TO_OTHER_THAN_HOME_UNIVERSITY_CANDIDATES:
            is_level = True
        elif admission_level == OTHER_THAN_HOME_UNIVERSITY_SEATS_ALLOTTED_TO_HOME_UNIVERSITY_CANDIDATES:
            is_level = True
        elif admission_level == OTHER_THAN_HOME_UNIVERSITY_SEATS_ALLOTTED_TO_OTHER_THAN_HOME_UNIVERSITY_CANDIDATES:
            is_level = True
        else:
            pass

        return is_level

    def is_row_for_status(self, sheet=None, rowindex=None):
        is_status = False
        rowList = sheet.row_values(rowindex)
        status = rowList[0]
        if status == 'Status:':
            is_status = True
        return is_status

    def get_admission_level(self, sheet=None, rowindex=None):
        rowlist = sheet.row_values(rowindex)
        admission_level = rowlist[0]

        return admission_level

    def is_row_table_header(self, sheet=None, rowindex=None):
        is_table_header = False

        rowList = sheet.row_values(rowindex)
        if len(self.seat_type_enum_set.intersection(rowList)):
            is_table_header = True

        return is_table_header

    def is_row_table_rank(self, sheet=None, rowindex=None):
        is_rank = False
        rowList = sheet.row_values(rowindex)
        if rowList[0]:
            is_rank = True
        return is_rank

    def is_row_table_rank_and_merit_score(self, sheet=None, rowindex=None):
        is_rank_and_merit = False
        rowList = sheet.row_values(rowindex)
        for row in rowList:
            merit_score_group = re.search(r'\(([^\)]+)\)', str(row))
            rank_group = re.search(r'(?<!\()\b\w+\b(?![\)])', str(row))
            if (((merit_score_group is not None) and len(merit_score_group.group()) > 0) and (
                    (rank_group is not None) and len(rank_group.group(0)) > 0)):
                is_rank_and_merit = True
                break

        return is_rank_and_merit

    def get_rank_and_merit_score(self, sheet=None, rowindex=None ):
        rowList = sheet.row_values(rowindex)
        rank_list = [''] * len(rowList)
        merit_score_list = [''] * len(rowList)
        #for row in rowList:
        for index in range(len(rowList)):
            row = rowList[index]
            merit_score_group = re.search(r'\(([^\)]+)\)', str(row))
            rank_group = re.search(r'(?<!\()\b\w+\b(?![\)])', str(row))
            if (((merit_score_group is not None) and len(merit_score_group.group()) > 0) and (
                    (rank_group is not None) and len(rank_group.group(0)) > 0)):

                merit_score = merit_score_group.group(1)
                rank = rank_group.group(0)
                # self.logger.info("merit_score "+ str(merit_score))
                # self.logger.info("rank " + str(rank))
                rank_list.insert(index, rank)
                merit_score_list.insert(index, merit_score)
            else:
                rank_list.insert(index, row)
                #merit_score_list()

        return rank_list, merit_score_list

    def is_row_table_merit_score(self, sheet=None, rowindex=None):
        is_merit_score = False
        rowList = sheet.row_values(rowindex)
        if len(str(rowList[0])) == 0:
            is_merit_score = True
        return is_merit_score

    def get_table_header(self, sheet=None, rowindex=None):
        header_list = None
        if self.is_row_table_header(sheet=sheet, rowindex=rowindex):
            header_list = sheet.row_values(rowindex)
        return header_list

    def get_cut_off_object(self, sheet=None, rowindex=None):
        rowList = sheet.row_values(rowindex)
        header_list = None
        rank_list = None
        merit_score_list = None
        if self.is_row_table_header(sheet=sheet, rowindex=rowindex):
            header_list = rowList
        elif self.is_row_table_rank(sheet=sheet, rowindex=rowindex):
            rank_list = rowList
            if self.is_row_table_rank_and_merit_score(sheet=sheet, rowindex=rowindex):
                rank_list, merit_score_list = self.get_rank_and_merit_score(sheet=sheet, rowindex=rowindex)
        elif self.is_row_table_merit_score(sheet=sheet, rowindex=rowindex):
            merit_score_list = rowList
        return header_list, rank_list, merit_score_list

    def get_cut_off_details_for_current_branch(self, sheet=None, branch=None, rowindex=None):
        branch.status = get_branch_status(sheet=sheet, branch=branch, rowindex=rowindex)
        cutoff_table_header = []
        cutoff_table_rank = []
        cutoff_table_merit_score = []
        admission_level = None
        for index in range(rowindex, sheet.nrows):
            rowlist = sheet.row_values(index)
            if self.is_footer_started(row=rowlist):
                break
            elif self.is_row_for_collage(sheet=sheet, collage=branch.collage, rowindex=index):
                continue
            elif self.is_row_for_branch(sheet=sheet, branch=branch, rowindex=index):
                continue
            elif self.is_row_for_level(sheet=sheet, rowindex=index):
                admission_level = self.get_admission_level(sheet=sheet, rowindex=index)
                self.logger.info("Processing for admission level : " + admission_level)
                continue
            elif self.is_row_for_status(sheet=sheet, rowindex=index):
                continue
            elif self.is_row_for_stage(sheet=sheet, rowindex=index):
                continue
            else:
                header_list, rank_list, merit_score_list = self.get_cut_off_object(sheet=sheet, rowindex=index)
                if header_list is not None:
                    cutoff_table_header = header_list
                    cutoff_table_rank.clear()
                    cutoff_table_merit_score.clear()
                elif rank_list is not None:
                    if cutoff_table_rank is not None:
                        cutoff_table_merit_score.clear()
                    cutoff_table_rank = rank_list
                    if merit_score_list is not None:
                        cutoff_table_merit_score = merit_score_list
                elif merit_score_list is not None:
                    cutoff_table_merit_score = merit_score_list

                if (len(cutoff_table_header) > 0) and (len(cutoff_table_rank) > 0) and (
                        len(cutoff_table_merit_score) > 0):
                    for header_index in range(1, len(cutoff_table_header)):
                        if cutoff_table_rank[header_index]:
                            admission_cutoff = Admissioncutoff()
                            merit_rank = re.sub('[^0-9]', '', str(cutoff_table_rank[header_index]) )
                            admission_cutoff.rank = float(merit_rank)

                            admission_cutoff.merit_score = float(cutoff_table_merit_score[header_index].strip('()'))
                            admission_cutoff.stage = cutoff_table_rank[0]
                            admission_cutoff.admission_year = self.admission_year
                            admission_cutoff.branch = branch
                            admission_cutoff.seat_type = SeatType(cutoff_table_header[header_index])
                            admission_cutoff.level = admission_level
                            admission_cutoff.round = self.cap_round

                            self.admission_cut_off_list.append(admission_cutoff)

    def get_branches(self, sheet=None, collage=None):
        branchSet = set()
        if has_header(sheet):
            collagecode = collage.code
            for rowindex in range(sheet.nrows):
                rowlist = sheet.row_values(rowindex)
                for row in rowlist:
                    if collagecode in str(row):
                        if str(row).startswith(collagecode):
                            codestrings = str(row).split()
                            if len(collagecode) < len(codestrings[0]):
                                keys = list(self.branchCodeToBranch.keys())
                                branch = None
                                if codestrings[0] not in keys:
                                    branch = Branch()
                                    branch.code = codestrings[0]
                                    branch.name = str(row).replace(branch.code + ' - ', '')
                                    branch.collage = collage
                                    self.branchCodeToBranch[branch.code] = branch
                                    branchSet.add(branch)
                                else:
                                    branch = self.branchCodeToBranch[codestrings[0]]
                                    branchSet.add(branch)

                                self.logger.info("Processing for branch :- " + str(branch))
                                self.get_cut_off_details_for_current_branch(branch=branch, sheet=sheet,
                                                                            rowindex=rowindex)
        return branchSet

    def get_files_to_parse(self):
        l_filepathlist = []

        for root, dirs, files in os.walk(self.resource_location):
            if len(files) > 0:
                for l_file in files:
                    if l_file.endswith('.xlsx'):
                        l_filePath = os.path.join(root, l_file)
                        if os.path.isfile(l_filePath):
                            l_filepathlist.append(l_filePath)
        return l_filepathlist

    def update_admission_year(self, sheet=None):
        seperator = " "
        if has_header(sheet):
            rowlist = sheet.row_values(3)
            rowlist = list(filter(None, rowlist))
            regex_string = '(\d{4}\-\d{2})'
            # for year_string in rowlist:
            joined_string = seperator.join(rowlist)
            search_string = re.search(regex_string, joined_string)
            if search_string:
                self.admission_year = search_string.group(0)
                self.collage_row_no = 4
            else:
                rowlist = sheet.row_values(2)
                rowlist = list(filter(None, rowlist))
                joined_string = seperator.join(rowlist)
                search_string = re.search(regex_string, joined_string)
                if search_string:
                    self.admission_year = search_string.group(0)
                    self.collage_row_no = 3

    def get_cap_round_number(self, sheet=None):
        rowlist = sheet.row_values(2)
        rowlist = list(filter(None, rowlist))
        capround = None
        for capstring in rowlist:
            if 'CAP Round' in capstring:
                splitted = capstring.split()
                capround = splitted[2]
                if capround == '-':
                    capround = splitted[3]
                break
            else:
                capround = 'Additional Round for Government/Govt. Aided Institutes only'
        seperator = " "

        return capround

    def available_collage_status(self, status):
        for file in self.allroundcapexcel:
            l_wb = open_workbook(os.path.join(self.path, file))

            allsheets = l_wb.sheets()
            for sheet in allsheets:
                for rowindex in range(sheet.nrows):
                    rowlist = sheet.row_values(rowindex)
                    if 'Status' in str(rowlist[0]) and not 'Home University :' in str(rowlist[1]):
                        status.add(str(rowlist[1]))
        sorted(status)

    def get_cast_catagory(self, categorySet, admissionType):

        for file in self.allroundcapexcel:
            l_wb = open_workbook(os.path.join(self.path, file))

            allsheets = l_wb.sheets()
            for sheet in allsheets:
                for rowindex in range(sheet.nrows):
                    rowlist = sheet.row_values(rowindex)
                    if 'Stage' in str(rowlist[0]):
                        categoryList = sheet.row_values(rowindex - 1)
                        if not " " in str(categoryList[0]):
                            for category in categoryList:
                                if category:
                                    categorySet.add(category)
                        else:
                            admissionType.add(categoryList[0])
        sorted(categorySet)
        sorted(admissionType)

    def validate_collage(self):
        collage_list = list(self.collageCodeToCollage.values())
        for collage in collage_list:
            if collage.university is None:
                self.logger.info("University not found for "+str(collage))
                #raise ("University not found for ")
            else:
                self.logger.info("Collages with Valid University : " + str(collage))
                self.logger.info("University Name : " + str(collage.university.name))

    def run_populate_db(self):
        logfileName = "populate_db_tables_" + str(self.ts) + ".log"
        log_file_name = os.path.join(self.logsDir, logfileName)
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                            level=logging.INFO,
                            handlers=[
                                logging.FileHandler(log_file_name, mode='w', encoding=None, delay=False),
                                logging.StreamHandler()
                            ])
        try:
            allsheets = []
            workbooks = []
            masterBranches = []
            l_fileList = self.get_files_to_parse()
            for l_file in l_fileList:
                self.logger.info("\n")
                self.logger.info("Processing workbook : " + l_file)
                self.logger.info("\n")
                l_wb = open_workbook(l_file)
                allsheets = l_wb.sheets()
                count = 0
                self.update_admission_year(allsheets[0])
                collagenames = set()
                self.cap_round = self.get_cap_round_number(sheet=allsheets[0])
                for sheet in allsheets:
                    self.logger.info("Processing sheet No:- " + str(count + 1))
                    if has_header(sheet=sheet):
                        collage = self.get_collage(sheet=sheet)
                        collagenames.add(collage)

                    self.logger.info("Processing for Collage :- " + str(collage))
                    branchSet = self.get_branches(sheet=sheet, collage=collage)
                    masterBranches.extend(list(branchSet))
                    count += 1

            self.logger.info("------------------")
            self.logger.info("University info")
            self.dump_objects(objects=list(self.universitynametoobj.values()))
            self.logger.info("------------------")
            self.validate_collage()

            if self.do_insert:
                dbutils.buildInsert(self.admission_cut_off_list, db_url=self.get_engine_url())

        finally:
            self.logger.info("Details Logs available at "+ log_file_name)

    @staticmethod
    def populate_db(args):
        utils = MahaCETEngineering(args)
        utils.run_populate_db()
