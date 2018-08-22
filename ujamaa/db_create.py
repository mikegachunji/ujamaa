from ujamaa import create_app
from ujamaa_models import db
from ujamaa_models.models import User, Post, University, Program, Course, CourseOutline, Exam, Notes

app = create_app()
app.app_context().push()
 
 
# drop all of the existing database tables

db.drop_all()
 
# create the database and the database table
db.create_all()


# insert user data
university1 = University(title='Moi University')
university2 = University(title='Jomo Kenyatta University of Science and Technology')
university3 = University(title='Strathmore University')
university4 = University(title='Kenyatta University')
university5 = University(title='University Of Nairobi')

db.session.add(university1)
db.session.add(university2)
db.session.add(university3)
db.session.add(university4)
db.session.add(university5)


program1 = Program(title='Information Technology')
program2 = Program(title='Business Management')
program3 = Program(title='Economics')
db.session.add(program1)
db.session.add(program2)
db.session.add(program3)


course1 = Course(title='Introduction To Computer Systems',year=1, program_id=1)
course2 = Course(title='Introduction To Programming', year=1, program_id=1)
course3 = Course(title='Discrete Mathematics', year=1, program_id=1)
course4 = Course(title='Probability And Statistics', year=1, program_id=1)
course5 = Course(title='Operating Systems', year=2, program_id=1)
course6 = Course(title='Computer Architecture', year=2, program_id=1)
course7 = Course(title='Computer Networks', year=2, program_id=1)
course8 = Course(title='Software Engineering', year=2, program_id=1)
course9 = Course(title='Analysis And Design Of Algorithms', year=3, program_id=1)
course10 = Course(title='Foundations Of Human Computer Interaction', year=3, program_id=1)
course11 = Course(title='Management Information Systems', year=3, program_id=1)
course12 = Course(title='Distributed Systems', year=3, program_id=1)
course13 = Course(title='Computer Network Security', year=4, program_id=1)
course14 = Course(title='Icts And Society', year=4, program_id=1)
course15 = Course(title='Ict Project Management', year=4, program_id=1)
course16 = Course(title='Computer Graphics', year=4, program_id=1)

course17 = Course(title='Communication Skills', year=1, program_id=2)
course18 = Course(title='Introduction To Business', year=1, program_id=2)
course19 = Course(title='Introduction To Micro-economics', year=1 , program_id=2)
course20 = Course(title='Introduction To Macro-economics', year=1 , program_id=2)
course21 = Course(title='Introduction To Management Accounting', year=2 , program_id=2)
course22 = Course(title='Micro-economic Theory', year=2, program_id=2)
course23 = Course(title='Organizational Theory', year=2, program_id=2)
course24= Course(title='Introduction To Risk And Insurance', year=2, program_id=2)
course25 = Course(title='Organizational Behaviour', year=3, program_id=2)
course26 = Course(title='Monetary Theory And Practice', year=3, program_id=2)
course27= Course(title='Financial Institutions And Markets', year=3, program_id=2)
course28 = Course(title='Business Law I', year=3, program_id=2)
course29 = Course(title='Principles Of Auditing', year=4, program_id=2)
course30= Course(title='Tax Laws And Practice', year=4, program_id=2)
course31= Course(title='Strategic Management', year=4, program_id=2)
course32 = Course(title='International Finance', year=4, program_id=2)

course33 = Course(title='Communication Skills', year=1, program_id=3)
course34= Course(title='Introduction To Microeconomics', year=1, program_id=3)
course35= Course(title='Introduction To Macroeconomics', year=1, program_id=3)
course36 = Course(title='Economic Statistics I', year=1, program_id=3)
course37= Course(title='Introduction To Financial Accounting', year=2, program_id=3)
course38 = Course(title='Introduction To Management Accounting', year=2, program_id=3)
course39= Course(title='Mathematics For Economists I', year=2, program_id=3)
course40= Course(title='Introduction To Real Analysis & Topology', year=2, program_id=3)
course41 = Course(title='International Economics', year=3, program_id=3)
course42 = Course(title='Economic History', year=3, program_id=3)
course43 = Course(title='Development Economics', year=3, program_id=3)
course44 = Course(title='Intermediate Microeconomics', year=3, program_id=3)
course45 = Course(title='Public Economics', year=4, program_id=3)
course46 = Course(title='Environmental Economics', year=4, program_id=3)
course47= Course(title='Transport Economics', year=4, program_id=3)
course48 = Course(title='Economics Of Industry', year=4, program_id=3)

db.session.add(course1)
db.session.add(course2)
db.session.add(course3)
db.session.add(course4)
db.session.add(course5)
db.session.add(course6)
db.session.add(course7)
db.session.add(course8)
db.session.add(course9)
db.session.add(course10)
db.session.add(course11)
db.session.add(course12)
db.session.add(course13)
db.session.add(course14)
db.session.add(course15)
db.session.add(course16)
db.session.add(course17)
db.session.add(course18)
db.session.add(course19)
db.session.add(course20)
db.session.add(course21)
db.session.add(course22)
db.session.add(course23)
db.session.add(course24)
db.session.add(course25)
db.session.add(course26)
db.session.add(course27)
db.session.add(course28)
db.session.add(course29)
db.session.add(course30)
db.session.add(course31)
db.session.add(course32)
db.session.add(course33)
db.session.add(course34)
db.session.add(course35)
db.session.add(course36)
db.session.add(course37)
db.session.add(course38)
db.session.add(course39)
db.session.add(course40)
db.session.add(course41)
db.session.add(course42)
db.session.add(course43)
db.session.add(course44)
db.session.add(course45)
db.session.add(course46)
db.session.add(course47)
db.session.add(course48)

db.session.commit()