# CS1010S --- Programming Methodology
#
# Mission 7 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import datetime
import csv

###############
# Pre-defined #
###############

def map(fn, seq):
    res = ()

    for ele in seq:
        res = res + (fn(ele), )
    return res

def filter(pred, seq):
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

###############
# Station ADT #
###############

def make_station(station_code, station_name):
    return (station_code, station_name)

def get_station_code(station):
    return station[0]

def get_station_name(station):
    return station[1]

test_station1 = make_station('CC2', 'Bras Basah')
test_station2 = make_station('CC3', 'Esplanade')
test_station3 = make_station('CC4', 'Promenade')


############
## Task 1 ##
############

def make_train(train_code):
    ''' Do NOT modify this function'''
    return (train_code,)



test_train = make_train('TRAIN 0-0')

#############
# Task 1a   #
#############

def get_train_code(train):
    return train[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1A
print("## Task 1a ##")
print(get_train_code(test_train))

# Expected Output #
# TRAIN 0-0

#############
# Task 1b   #
#############

def make_line(name, stations):
    return (name,) + stations

def get_line_name(line):
    return line[0]

def get_line_stations(line):
    return line[1:]

def get_station_by_name(line, station_name):
    result = filter(lambda station: True if get_station_name(station) == station_name else False,\
                    get_line_stations(line))
    if result == ():
        return None
    else:
        return result[0]

def get_station_by_code(line, station_code):
    result = filter(lambda station: True if get_station_code(station) == station_code else False,\
                    get_line_stations(line))
    if result == ():
        return None
    else:
        return result[0]

def get_station_position(line, station_code):
    if get_station_by_code(line, station_code) == None:
        return -1
    else:
        stations_by_code = map(get_station_code, get_line_stations(line))
        i = 0
        for stat in stations_by_code:
            if stat == station_code:
                break
            else:
                i += 1
        return i

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1B
print("## Task 1b ##")
test_line = make_line('Circle Line', (test_station1, test_station2, test_station3))
print(get_line_name(test_line))
print(get_line_stations(test_line))
print(get_station_by_name(test_line, 'Bras Basah'))
print(get_station_by_code(test_line, 'CC4'))

# Expected Output #
# Circle Line
# (('CC2', 'Bras Basah'), ('CC3', 'Esplanade'), ('CC4', 'Promenade'))
# ('CC2', 'Bras Basah')
# ('CC4', 'Promenade')

#############
# Task 1c   #
#############

def make_train_position(is_moving, from_station, to_station):
    ''' Do NOT modify this function'''
    return (is_moving, from_station, to_station)

def get_is_moving(train_position):
    return train_position[0]

def get_direction(line, train_position):
    start_pt = get_station_position(line, get_station_code(train_position[1]))
    end_pt = get_station_position(line, get_station_code(train_position[2]))
    if end_pt>start_pt:
        return 0
    else:
        return 1

def get_stopped_station(train_position):
    if not get_is_moving(train_position):
        return train_position[1]

def get_previous_station(train_position):
    if get_is_moving(train_position):
        return train_position[1]

def get_next_station(train_position):
    return train_position[2]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1C
print("## Task 1c ##")
test_train_position1 = make_train_position(False, test_station1, test_station2)
test_train_position2 = make_train_position(True, test_station3, test_station2)
test_train_position3 = make_train_position(True, test_station1, test_station3)
print(get_is_moving(test_train_position2))
print(get_direction(test_line, test_train_position1))
print(get_stopped_station(test_train_position1))
print(get_previous_station(test_train_position2))
print(get_next_station(test_train_position2))

# Expected Output #
# True
# 0
# ('CC2', 'Bras Basah')
# ('CC4', 'Promenade')
# ('CC3', 'Esplanade')

#############
# Task 1d   #
#############

def make_schedule_event(train, train_position, time):
    return (train, train_position, time)

def get_train(schedule_event):
    return schedule_event[0]

def get_train_position(schedule_event):
    return schedule_event[1]

def get_schedule_time(schedule_event):
    return schedule_event[2]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1D
print("## Task 1d ##")
test_bd_event1 = make_schedule_event(test_train, test_train_position2, datetime.datetime(2016, 1, 1, 9, 27))
test_bd_event2 = make_schedule_event(test_train, test_train_position1, datetime.datetime(2016, 1, 1, 2, 25))
test_bd_event3 = make_schedule_event(test_train, test_train_position3, datetime.datetime(2016, 1, 1, 9, 27))
print(get_train(test_bd_event1))
print(get_train_position(test_bd_event1))
print(get_schedule_time(test_bd_event1))

# Expected Output #
# ('TRAIN 0-0',)
# (True, ('CC4', 'Promenade'), ('CC3', 'Esplanade'))
# 2016-01-01 09:27:00


############
## Task 2 ##
############

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

#############
# Task 2a   #
#############

def parse_lines(data_file):
    rows = read_csv(data_file)[1:]
    lines = ()
    curr_line_name = rows[0][2]
    curr_line_stations = ()
    for row in rows:
        code, station_name, line_name = row
        if line_name == curr_line_name:
            curr_line_stations += (make_station(code, station_name),)
        else:
            lines += (make_line(curr_line_name, curr_line_stations),)
            curr_line_name = line_name
            curr_line_stations = (make_station(code, station_name),)
    # Addition #3
    return lines

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2A. THIS IS NOT OPTIONAL TESTING!
LINES = parse_lines('station_info.csv')
CCL = filter(lambda line: get_line_name(line) == 'Circle Line', LINES)[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2A
print("## Task 2a ##")
print(get_line_stations(CCL)[5:8])
print(LINES)

# Expected Output #
# (('CC6', 'Stadium'), ('CC7', 'Mountbatten'), ('CC8', 'Dakota'))

#############
# Task 2b   #
#############

def parse_events_in_line(data_file, line):
    rows = read_csv(data_file)[1:]
    events = ()
    for row in rows:
        train = make_train(row[0],)
        start_station = get_station_by_code(line, row[2])
        end_station = get_station_by_code(line, row[3])
        if row[1] == "True":
            is_moving = True
        else:
            is_moving = False
        train_position = make_train_position(is_moving, start_station, end_station)
        date, month, year = map(int, row[4].split("/"))
        hour, minute = map(int, row[5].split(":"))
        train_event = make_schedule_event(train, train_position, datetime.datetime(year, month, date, hour, minute))
        events += (train_event, )
    return events

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2B. THIS IS NOT OPTIONAL TESTING!
BD_EVENTS = parse_events_in_line('breakdown_events.csv', CCL)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2B
print("## Task 2b ##")
print(BD_EVENTS[9])

# Expected Output #
# (('TRAIN 1-11',), (False, ('CC23', 'one-north'), ('CC22', 'Buona Vista')), datetime.datetime(2017, 1, 6, 7, 9))

############
## Task 3 ##
############

#############
# Task 3a   #
#############

def is_valid_event_in_line(bd_event, line):
    schedule_time = get_schedule_time(bd_event)
    train_position = get_train_position(bd_event)
    if get_is_moving(train_position):
        start_station = get_previous_station(train_position)
        end_station = get_next_station(train_position)
    else:
        start_station = get_stopped_station(train_position)
        end_station = get_next_station(train_position)
    start_pt = get_station_position(line, get_station_code(start_station))
    end_pt = get_station_position(line, get_station_code(end_station))
    my_date = get_schedule_time(bd_event)
    start_time = datetime.time(7,0)
    end_time = datetime.time(23,0)
    if my_date.time()<start_time or my_date.time()>end_time:
        return False
    if abs(start_pt-end_pt)!= 1:
        return False
    return True
    

def get_valid_events_in_line(bd_events, line):
    ''' Do NOT modify this function'''
    return filter(lambda ev: is_valid_event_in_line(ev, line), bd_events)

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 3A. THIS IS NOT OPTIONAL TESTING!
##VALID_BD_EVENTS = get_valid_events_in_line(BD_EVENTS, CCL)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3A
##print("## Task 3a ##")
##print(is_valid_event_in_line(test_bd_event1, CCL))
##print(is_valid_event_in_line(test_bd_event2, CCL))
##print(is_valid_event_in_line(test_bd_event3, CCL))

# Expected Output #
# True
# False

#############
# Task 3b   #
#############

def get_location_id_in_line(bd_event, line):
    train_position = get_train_position(bd_event)
    if get_is_moving(train_position):
        start_pt = get_station_position(line, get_station_code(get_previous_station(train_position)))
        end_pt = get_station_position(line, get_station_code(get_next_station(train_position)))
        return (start_pt+end_pt)/2
    else:
        return get_station_position(line, get_station_code(get_stopped_station(train_position)))
    

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3B
##print("## Task 3b ##")
##test_loc_id1 = get_location_id_in_line(test_bd_event1, CCL)
##test_loc_id2 = get_location_id_in_line(test_bd_event2, CCL)
##print(test_loc_id1)
##print(test_loc_id2)

# Expected Output #
# 2.5
# 1

############
## Task 4 ##
############

# UNCOMMENT the following to read the entire train schedule
##FULL_SCHEDULE = parse_events_in_line('train_schedule.csv', CCL)    # this will take some time to run

#############
# Task 4a   #
#############

def get_schedules_at_time(train_schedule, time):
    return_schedules = ()
    for schedule in train_schedule:
        if get_schedule_time(schedule) == time:
            return_schedules += (schedule,)
    return return_schedules
        

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4A
##print("## Task 4a ##")
##test_datetime = datetime.datetime(2017, 1, 6, 6, 0)
##test_schedules_at_time = get_schedules_at_time(FULL_SCHEDULE[:5], test_datetime)
##print(test_schedules_at_time[1])

# Expected Output #
# (('TRAIN 1-0',), (False, ('CC29', 'HarbourFront'), ('CC28', 'Telok Blangah')), datetime.datetime(2017, 1, 6, 6, 0))

#############
# Task 4b   #
#############

def get_schedules_near_loc_id_in_line(train_schedule, line, loc_id):
    return_schedules = ()
    for schedule in train_schedule:
        if abs(get_location_id_in_line(schedule, line)-loc_id)<=0.5:
            return_schedules += (schedule,)
        else:
            pass
    return return_schedules

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4B
##print("## Task 4b ##")
##test_schedules_near_loc_id = get_schedules_near_loc_id_in_line(FULL_SCHEDULE[:10], CCL, test_loc_id1)
##print(test_schedules_near_loc_id[1])

# Expected Output #
# (('TRAIN 0-0',), (True, ('CC3', 'Esplanade'), ('CC4', 'Promenade')), datetime.datetime(2017, 1, 6, 6, 5))

#############
# Task 4c   #
#############

def get_rogue_schedules_in_line(train_schedule, line, time, loc_id):
    time_match = get_schedules_at_time(train_schedule, time)
    loc_match = get_schedules_near_loc_id_in_line(train_schedule, line, loc_id)
    return_schedules = ()
    for schedule in time_match:
        if schedule in loc_match:
            return_schedules += (schedule,)

    return return_schedules

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4C
print("## Task 4c ##")
##test_bd_event3 = VALID_BD_EVENTS[0]
##test_loc_id3 = get_location_id_in_line(test_bd_event3, CCL)
##test_datetime3 = get_schedule_time(test_bd_event3)
##test_rogue_schedules = get_rogue_schedules_in_line(FULL_SCHEDULE[1000:1100], CCL, test_datetime3, test_loc_id3)
##print(test_rogue_schedules[2])

# Expected Output #
# (('TRAIN 1-11',), (True, ('CC24', 'Kent Ridge'), ('CC23', 'one-north')), datetime.datetime(2017, 1, 6, 7, 9))

############
## Task 5 ##
############

###############
# Scorer ADT  #
###############

def make_scorer():
    return {}

def blame_train(scorer, train_code):
    scorer[train_code] = scorer.get(train_code, 0) + 1
    return scorer

def get_blame_scores(scorer):
    return tuple(scorer.items())

# Use this to keep track of each train's blame score.
SCORER = make_scorer()

#############
# Task 5a   #
#############

def calculate_blame_in_line(full_schedule, valid_bd_events, line, scorer):
    for schedule in valid_bd_events:
        rogue_schedules = get_rogue_schedules_in_line(full_schedule, line, get_schedule_time(schedule),\
                                                      get_location_id_in_line(schedule, line))
        rogue_schedules_codes = map(get_train_code,(map(get_train,rogue_schedules)))
        filtered_codes = []
        for code in rogue_schedules_codes:
            if code in filtered_codes:
                pass
            else:
                filtered_codes.append(code)
        for code in filtered_codes:
            blame_train(SCORER, code)

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 5A. THIS IS NOT OPTIONAL TESTING!
##calculate_blame_in_line(FULL_SCHEDULE, VALID_BD_EVENTS, CCL, SCORER)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5A
##print("## Task 5a ##")
##print(sorted(get_blame_scores(SCORER))[7])

# Expected Answer
# ('TRAIN 0-5', 2)

#############
# Task 5b   #
#############

def find_max_score(scorer):
    return max(map(lambda score_tuple: score_tuple[1], get_blame_scores(scorer)))

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5B
##print("## Task 5b ##")
##test_max_score = find_max_score(SCORER)
##print(test_max_score)

# Expected answer
# 180

#############
# Task 5c   #
#############

# UNCOMMENT THE CODE BELOW TO VIEW ALL BLAME SCORES. THIS IS NOT OPTIONAL TESTING!
##print("## Task 5c ##")
##train_scores = get_blame_scores(SCORER)
##print("############### Candidate rogue trains ###############")
##for score in train_scores:
##    print("%s: %d" % (score[0], score[1]))
print("######################################################")

''' Please type your answer into the Task 5c textbox on Coursemology '''

'''
Yes, the rogue train hypothesis holds. This is because there is a single train with a significantly
higher blame score than all of the other trains. That train has a blame score of 180, while the
remaining trains have a highest of 18, which is 90% lower. This shows that this train, Train 0-4,
is more than likely to have some relationship with the breakdowns, since so many breakdowns happened
in close proximity to it while it was traveling. As for the other trains, though they may be related
to the breakdowns as well, it is much more likely that they just happened to be nearby and definitely
would not have had as much impact as Train 0-4.
'''

#############
# Task 5d   #
#############

def find_rogue_train(scorer, max_score):
    for score_tuple in get_blame_scores(scorer):
        if score_tuple[1] == max_score:
            return score_tuple[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5D
##print("## Task 5d ##")
##print("Rogue Train is '%s'" % find_rogue_train(SCORER, test_max_score))

# Expected Answer
# Rogue Train is 'TRAIN 0-4'
