#
# CS1010X --- Programming Methodology
#
# Sidequest 12.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json

# Reading json file
def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google ;)

    For example, cs1010x-fbdata.json contains:

    {
       "members": {
          "data": [
             {
                "name": "Aadit Kamat",
                "id": "1003982836283025"
             },
             {
                "name": "Rakshit Gogia",
                "id": "10204299775189027"
             },
             ...
          ]
       },
       "description": "This is the official FB Group for ...",
       "name": "CS1010X",
       "feed": {
          "data": [
             {
                "message": "Might be useful for the business analytics ...",
                "from": {
                   "name": "Ben Leong",
                   "id": "10152805891837166"
                },
                "name": "Machine Learning with Python - BDU"
                "id": "409054432560329_1002582839874149",
                "likes": {
                   "data": [
                      {
                         "id": "10208170707289199",
                         "name": "Lim Kian Hwee"
                      },
                      {
                         "id": "10204292869386114",
                         "name": "Siidheesh Theivasigamani"
                      },
                      ...
                   ]
                },
                ...
             },
             ...
          ]
       },
       "id": "409054432560329"
    }

    """
    datafile = open(filename, 'r',  encoding='utf-8')
    return json.loads(datafile.read())

# CS1010X Facebook Group Data as a dictionary object
fb_data = read_json('cs1010x-fbdata.json')

##########
# Task a #
##########

def count_comments(data):
    count = 0
    for item in data["feed"]["data"]:
        if "comments" in item:
            count += len(item["comments"]["data"])
    return count

print("Number of Comments in CS1010X: ", count_comments(fb_data))

##########
# Task b #
##########

def count_likes(data):
    count = 0
    for item in data["feed"]["data"]:
        if "likes" in item:
            count += len(item["likes"]["data"])
        if "comments" in item:
            for comment in item["comments"]["data"]:
                count += comment["like_count"]
    return count

print("Number of Likes in CS1010X: ", count_likes(fb_data))

##########
# Task c #
##########

def create_member_dict(data):
    result = {}
    for person in data["members"]["data"]:
        result[person["id"]]= {}
        for key, value in person.items():
            if key == "id":
                pass
            else:
                result[person["id"]][key] = value
    return result

member_dict = create_member_dict(fb_data)
print(member_dict["10205702832196255"])

# Q: Why did we choose the id of the member data object to be the key?
# A: Because the id is an unique identifier and allows us to call for a
# specific person's details using the ID from the resulting member dict.

# Q: It is inappropriate to use the name as the key. What will happen if we use the name as the key of member_dict?
# A: This is because there may be multiple people with the same name, such as
# Ivan Tan from our current class. Thus the identifier will not be unique.

##########
# Task d #
##########

def posts_freq(data):
    result = {}
    for post in data["feed"]["data"]:
        if post["from"]["id"] not in result:
            result[post["from"]["id"]] = 1
        else:
            result[post["from"]["id"]] += 1
    return result
        

print("Posts Frequency: ", posts_freq(fb_data))

##########
# Task e #
##########

def comments_freq(data):
    result = {}
    for post in data["feed"]["data"]:
        if "comments" in post:
            for comment in post["comments"]["data"]:
                if comment["from"]["id"] not in result:
                    result[comment["from"]["id"]] = 1
                else:
                    result[comment["from"]["id"]] += 1

    return result

print("Comments Frequency: ", comments_freq(fb_data))

##########
# Task f #
##########

def likes_freq(data):
    result = {}
    for post in data["feed"]["data"]:
        if "likes" in post:
            for like in post["likes"]["data"]:
                if like["id"] not in result:
                    result[like["id"]] = 1
                else:
                    result[like["id"]] += 1
    return result

print("Likes Frequency: ", likes_freq(fb_data))

##########
# Task g #
##########

def popularity_score(data):
    result = {}
    for post in data["feed"]["data"]:
        if "likes" in post:
            if post["from"]["id"] not in result:
                result[post["from"]["id"]] = len(post["likes"]["data"])
            else:
                result[post["from"]["id"]] += len(post["likes"]["data"])
        if "comments" in post:
            for comment in post["comments"]["data"]:
                if comment["like_count"] >0:
                    if comment["from"]["id"] not in result:
                        result[comment["from"]["id"]] = comment["like_count"]
                    else:
                        result[comment["from"]["id"]] += comment["like_count"]

    return result

print("Popularity Score: ", popularity_score(fb_data))

##########
# Task h #
##########

def member_stats(data):
    member_dict = create_member_dict(data)
    posts_dict = posts_freq(data)
    comments_dict = comments_freq(data)
    likes_dict = likes_freq(data)
    for key, value in member_dict.items():
        if key in posts_dict:
            member_dict[key]["posts_count"] = posts_dict[key]
        else:
            member_dict[key]["posts_count"] = 0
        if key in comments_dict:
            member_dict[key]["comments_count"] = comments_dict[key]
        else:
            member_dict[key]["comments_count"] = 0
        if key in likes_dict:
            member_dict[key]["likes_count"] = likes_dict[key]
        else:
            member_dict[key]["likes_count"] = 0

    return member_dict

stats = member_stats(fb_data)
print(stats["10152805891837166"])

##########
# Task i #
##########

def activity_score(data):
    stats_dict = member_stats(data)
    score_dict = {}
    for key, stat in stats_dict.items():
        score_dict[key] = stat["posts_count"]*3 + stat["comments_count"]*2 + stat["likes_count"]
    return score_dict

scores = activity_score(fb_data)
print(scores["10153020766393769"]) # => 30
print(scores["857756387629369"]) # => 8


##########
# Task j #
##########

def active_members_of_type(data, k, type_fn):
    member_list = create_member_dict(data)
    use_list = type_fn(data)
    result = []
    for key, value in member_list.items():
        if key not in use_list:
            pass
        elif use_list[key]>=k:
            result.append([value["name"], use_list[key]])
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return result

print(active_members_of_type(fb_data, 2, posts_freq))

print(active_members_of_type(fb_data, 20, comments_freq))

print(active_members_of_type(fb_data, 40, likes_freq))

print(active_members_of_type(fb_data, 20, popularity_score))

print(active_members_of_type(fb_data, 80, activity_score))




########### DO NOT REMOVE THE TEST BELOW ###########

def gradeit():
    print("\n*** Facebook Stalker Autograding ***")
    print('==================')
    answers = json.loads(open('grading.json', 'r',  encoding='utf-8').read())
    total, correct = 0, 0
    def pass_or_fail(code, answer):
        nonlocal total
        total += 1
        if code == answer:
            nonlocal correct
            correct += 1
            return 'Passed!'
        else:
            return 'Failed.'
            
    print('Testing count_comments... ', pass_or_fail(count_comments(fb_data), answers['count_comments']))
    print('Testing count_likes... ', pass_or_fail(count_likes(fb_data), answers['count_likes']))
    print('Testing create_member_dict... ', pass_or_fail(create_member_dict(fb_data), answers['create_member_dict']))
    print('Testing posts_freq... ', pass_or_fail(posts_freq(fb_data), answers['posts_freq']))
    print('Testing comments_freq... ', pass_or_fail(comments_freq(fb_data), answers['comments_freq']))
    print('Testing likes_freq... ', pass_or_fail(likes_freq(fb_data), answers['likes_freq']))
    print('Testing popularity_score... ', pass_or_fail(popularity_score(fb_data), answers['popularity_score']))
    print('Testing member_stats... ', pass_or_fail(member_stats(fb_data), answers['member_stats']))
    print('Testing activity_score... ', pass_or_fail(activity_score(fb_data), answers['activity_score']))
    print('Testing members with >= 1 posts... ', pass_or_fail(active_members_of_type(fb_data, 1, posts_freq), answers['active_posters']))
    print('Testing members with >= 4 comments... ', pass_or_fail(active_members_of_type(fb_data, 4, comments_freq), answers['active_commenters']))
    print('Testing members with >= 4 likes... ', pass_or_fail(active_members_of_type(fb_data, 4, likes_freq), answers['active_likers']))
    print('Testing members who have >= 3 likes... ', pass_or_fail(active_members_of_type(fb_data, 3, popularity_score), answers['popular']))
    print('Testing members with an activity score of >= 10... ', pass_or_fail(active_members_of_type(fb_data, 10, activity_score), answers['overall_active']))
    print('==================')
    print('Grades: ' + str(correct) + '/' + str(total) + '\n')

gradeit()
