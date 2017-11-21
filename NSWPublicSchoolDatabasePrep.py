#########################################################################################################
#   Program Name : NSWPublicSchoolDatabasePrep.py                                                          #
#   Program Description:                                                                                #
#   This program prepares a SQLite table containing data about Public Schools in NSW.                      #
#                                                                                                       #
#
#########################################################################################################
import sqlite3
import sys

#######################################################################
### Create NSW_SCHOOL_DATA Table                                     ###
#######################################################################
conn = sqlite3.connect('NSW_SCHOOL_DATA.sqlite')
cur = conn.cursor()

cur.executescript('''	
DROP TABLE IF EXISTS NSW_SCHOOL_DATA;

CREATE TABLE NSW_SCHOOL_DATA (
	SCHOOL_CODE       number(4),
	AGEID             number(6),
	SCHOOL_NAME       varchar(100),
	STREET            varchar(100),
	SUBURB            varchar(100),
	POSTCODE          number(4),
	PHONE             number(10),
	SCHOOL_EMAIL      varchar(50),
	FAX               number(10),
	STUDENT_NUMBER    number(5),
	INDIGENOUS_PCT    number(5),
	LBOTE_PCT         number(5),
	ICSEA_VALUE       number(4),
	LEVEL_OF_SCHOOLING varchar(50),
	SELECTIVE_SCHOOL  varchar(20),
	OPPORTUNITY_CLASS varchar(2),
	SCHOOL_SPECIALITY_TYPE varchar(20),
	SCHOOL_SUBTYPE    varchar(20),
	PRESCHOOL_IND     varchar(2),
	DISTANCE_EDUCATION varchar(2),
	INTENSIVE_ENGLISH_CENTRE varchar(2),
	SCHOOL_GENDER      varchar(10),
	LATE_OPENING_SCHOOL varchar(2),
	DATE_1ST_TEACHER   date,
	LGA               varchar(50),
	ELECTORATE        varchar(20),
	FED_ELECTORATE    varchar(20),
	OPERATIONAL_DIRECTORATE varchar(20),
	PRINCIPAL_NETWORK varchar(10),
	FACS_DISTRICT     varchar(100),
	LOCAL_HEALTH_DISTRICT varchar(50),
	AECG_REGION       varchar(50),
	ASGS_REMOTENESS   varchar(50),
	LATITUDE          number(10),
	LONGITUDE         number(10),
	ASSETS_UNIT       varchar(50)   
);

''')
print("Table Created")

#PRAGMA table_info("NSW_SCHOOL_DATA)"
fname = 'NSWPublicSchoolData.txt'
fhand = open(fname)

#######################################################################
### Populate NSW_BIRTH_RATE Table                                   ###
#######################################################################
for line in fhand:
    fields = line.split('|')

    SCHOOL_CODE = fields[0].strip()
    AGEID = fields[1].strip()
    SCHOOL_NAME = fields[2].strip()
    STREET = fields[3].strip()
    SUBURB = fields[4].strip()
    POSTCODE = fields[5].strip()
    PHONE = fields[6].strip()
    SCHOOL_EMAIL = fields[7].strip()
    FAX = fields[8].strip()
    STUDENT_NUMBER = fields[9].strip()
    INDIGENOUS_PCT = fields[10].strip()
    LBOTE_PCT = fields[11].strip()
    ICSEA_VALUE = fields[12].strip()
    LEVEL_OF_SCHOOLING = fields[13].strip()
    SELECTIVE_SCHOOL = fields[14].strip()
    OPPORTUNITY_CLASS = fields[15].strip()
    SCHOOL_SPECIALITY_TYPE = fields[16].strip()
    SCHOOL_SUBTYPE = fields[17].strip()
    PRESCHOOL_IND = fields[18].strip()
    DISTANCE_EDUCATION = fields[19].strip()
    INTENSIVE_ENGLISH_CENTRE = fields[20].strip()
    SCHOOL_GENDER = fields[21].strip()
    LATE_OPENING_SCHOOL = fields[22].strip()
    DATE_1ST_TEACHER = fields[23].strip()
    LGA = fields[24].strip()
    ELECTORATE = fields[25].strip()
    FED_ELECTORATE = fields[26].strip()
    OPERATIONAL_DIRECTORATE = fields[27].strip()
    PRINCIPAL_NETWORK = fields[28].strip()
    FACS_DISTRICT = fields[29].strip()
    LOCAL_HEALTH_DISTRICT = fields[30].strip()
    AECG_REGION = fields[31].strip()
    ASGS_REMOTENESS = fields[32].strip()
    LATITUDE = fields[33].strip()
    LONGITUDE = fields[34].strip()
    ASSETS_UNIT = fields[35].strip()




    if SCHOOL_CODE == "School_code": continue

    cur.execute("INSERT INTO NSW_SCHOOL_DATA VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(SCHOOL_CODE, AGEID, SCHOOL_NAME,STREET,SUBURB,POSTCODE,PHONE,SCHOOL_EMAIL,FAX,STUDENT_NUMBER,INDIGENOUS_PCT,LBOTE_PCT,ICSEA_VALUE,LEVEL_OF_SCHOOLING,SELECTIVE_SCHOOL,OPPORTUNITY_CLASS,SCHOOL_SPECIALITY_TYPE,SCHOOL_SUBTYPE,PRESCHOOL_IND,DISTANCE_EDUCATION,INTENSIVE_ENGLISH_CENTRE,SCHOOL_GENDER,LATE_OPENING_SCHOOL,DATE_1ST_TEACHER,LGA,ELECTORATE,FED_ELECTORATE,OPERATIONAL_DIRECTORATE,PRINCIPAL_NETWORK,FACS_DISTRICT,LOCAL_HEALTH_DISTRICT,AECG_REGION,ASGS_REMOTENESS,LATITUDE,LONGITUDE,ASSETS_UNIT))

conn.commit()

print('Done')