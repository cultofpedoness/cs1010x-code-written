#
# CS1010S --- Programming Methodology
#
# Mission 8 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ippt import *
import csv

##########
# Task 1 #
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

def read_data(filename):
    rows = read_csv(filename)
    rep_title = map(lambda x: int(x),rows[0][1:])
    age_title = ()
    data = ()
    for row in rows[1:]:
        age_title += (int(row[0]),)
        data += (map(lambda x: int(x),row[1:]),)
    return create_table(data, age_title, rep_title)

pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

# print("## Q1 ##")
# Sit-up score of a 24-year-old who did 10 sit-ups.
print(access_cell(situp_table, 24, 10))    # 0

# Push-up score of a 18-year-old who did 30 push-ups.
print(access_cell(pushup_table, 18, 30))   # 16

# Run score of a 30-year old-who ran 12 minutes (720 seconds)
print(access_cell(run_table, 30, 720))     # 36

# Since our run.csv file does not have data for 725 seconds, we should
# get None if we try to access that cell.
print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 #
##########

def pushup_score(pushup_table, age, pushup):
    if pushup == 0:
        return 0
    elif pushup>60:
        pushup = 60
    return access_cell(pushup_table, age, pushup)

def situp_score(situp_table, age, situp):
    if situp == 0:
        return 0
    elif situp > 60:
        situp = 60
    return access_cell(situp_table, age, situp)

def run_score(run_table, age, run):
    if run >1100:
        return 0
    elif run <510:
        run = 510
    if run%10:
        run = run - run%10 + 10
    return access_cell(run_table, age, run)

print("## Q2 ##")
print(pushup_score(pushup_table, 18, 61))   # 25
print(pushup_score(pushup_table, 18, 70))   # 25
print(situp_score(situp_table, 24, 0))      # 0

print(run_score(run_table, 30, 720))        # 36
print(run_score(run_table, 30, 725))        # 35
print(run_score(run_table, 30, 735))        # 35
print(run_score(run_table, 30, 500))        # 50
print(run_score(run_table, 30, 1300))       # 0


##########
# Task 3 #
##########

def ippt_award(score):
    if score<51:
        return "F"
    elif score<61:
        return "P"
    elif score<75:
        return "P$"
    elif score<85:
        return "S"
    else:
        return "G"

print("## Q3 ##")
print(ippt_award(50))     # F
print(ippt_award(51))     # P
print(ippt_award(61))     # P$
print(ippt_award(75))     # S
print(ippt_award(85))     # G


##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    pushup_table = get_pushup_table(ippt_table)
    situp_table = get_situp_table(ippt_table)
    run_table = get_run_table(ippt_table)
    p_score = pushup_score(pushup_table, age, pushup)
    s_score = situp_score(situp_table, age, situp)
    r_score = run_score(run_table, age, run)
    ippt_score = p_score+s_score+r_score
    return (ippt_score, ippt_award(ippt_score))
    

print("## Q4 ##")
print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########
def make_training_program(rate_pushup, rate_situp, rate_run):
    def training_program(ippt_table, age, pushup, situp, run, days):
        pushup += days//rate_pushup
        situp += days//rate_situp
        run -= days//rate_run
        return (pushup, situp, run, ippt_results(ippt_table, age, pushup, \
                                                 situp, run))
    return training_program

print("## Q5 ##")
tp = make_training_program(7, 3, 10)
print(tp(ippt_table, 25, 30, 25, 820, 30))        # (34, 35, 817, (61, 'P$'))


##########
# Bonus  #
##########

def make_tp_bonus(rate_pushup, rate_situp, rate_run):
    def tp_bonus(ippt_table, age, pushup, situp, run, days):
        if days == 0:
            return (pushup, situp, run, ippt_results(ippt_table, age, pushup,situp, run))
        elif days - rate_pushup < 0:
            if days - rate_situp <0:
                if days - rate_run <0:
                   return (pushup, situp, run, ippt_results(ippt_table, age, pushup,situp, run))
                else:
                    return tp_bonus(ippt_table, age, pushup, situp, run-1, days-rate_run)
            else:
                if days - rate_run <0:
                    return tp_bonus(ippt_table, age, pushup, situp+1, run, days-rate_situp)
                else:
                    return max(tp_bonus(ippt_table, age, pushup, situp+1, run, days-rate_situp), \
                               tp_bonus(ippt_table, age, pushup, situp, run-1, days-rate_run),\
                               key = lambda x: x[3][0])
        else:
            if days - rate_situp <0:
                if days - rate_run <0:
                    return tp_bonus(ippt_table, age, pushup+1,situp, run, days-rate_pushup)
                else:
                    return max(tp_bonus(ippt_table, age, pushup+1, situp, run, days-rate_pushup), \
                               tp_bonus(ippt_table, age, pushup, situp, run-1, days-rate_run),\
                               key = lambda x: x[3][0])
            else:
                if days - rate_run <0:
                    return max(tp_bonus(ippt_table, age, pushup+1, situp, run, days-rate_pushup), \
                               tp_bonus(ippt_table, age, pushup, situp+1, run, days-rate_situp),\
                               key = lambda x: x[3][0])
                else:
                    return max(tp_bonus(ippt_table, age, pushup+1, situp, run, days-rate_pushup),\
                               tp_bonus(ippt_table, age, pushup, situp+1, run, days-rate_situp),\
                               tp_bonus(ippt_table, age, pushup, situp, run-1, days-rate_run),\
                               key = lambda x: x[3][0])
    return tp_bonus

tp_bonus = make_tp_bonus(7, 3, 10)

# Note: Depending on your implementation, you might get a different number of
# sit-up, push-up, and 2.4km run timing. However, the IPPT score and grade
# should be the same as the sample output.

print(tp_bonus(ippt_table, 25, 20, 30, 800, 30))      # (20, 40, 800, (58, 'P'))
print(tp_bonus(ippt_table, 25, 20, 30, 800, 2))       # (20, 30, 800, (52, 'P'))
