users = [
	{"id": 0, "name": "Hero"},
	{"id": 1, "name": "Dunn"},
	{"id": 2, "name": "Sue"},
	{"id": 3, "name": "Chi"},
	{"id": 4, "name": "Thor"},
	{"id": 5, "name": "Clive"},
	{"id": 6, "name": "Hicks"},
	{"id": 7, "name": "Devin"},
	{"id": 8, "name": "Kate"},
	{"id": 9, "name": "Klein"},
]

print("Current Users", users)

# (0, 1) indicates that the data 
# scientist with id 0 (Hero) and
# the data scientist with id 1 
# (Dunn) are friends.
friendships = [
	(0, 1),
	(0, 2),
	(1, 2), 
	(1, 3), 
	(2, 3), 
	(3, 4),
	(4, 5), 
	(5, 6), 
	(5, 7), 
	(6, 8), 
	(7, 8), 
	(8, 9)
]

# dd a list of friends to each user.
for user in users:
	user["friends"] = []

# Then we populate the lists
# using the friendships data
for i, j in friendships:
	users[i]["friends"].append(users[j])
	users[j]["friends"].append(users[i])

# find the total number of connections, 
# by summing up the lengths of all the
# friends lists
def number_of_friends(user):
	""" How many friends does a user have """
	return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)
print("Total connections:", total_connections)

number_of_users = len(users)
print("Total Users:", number_of_users)

avg_connections = total_connections / number_of_users
print("Average Connections per User:", avg_connections)

# It’s also easy to find the most connected people—they’re the people who have the largest number of friends
# Since there aren’t very many users, we can sort them from “most friends” to “least friends”
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
# each pair is (user_id, num_friends)
# sorted(num_friends_by_id, key=lambda(user_id, num_friends): num_friends, reverse=True)


""" “Data Scientists You May Know” suggester. """

# Your first instinct is to suggest that a user might know the friends of friends. These are easy to compute: for each of a user’s friends, iterate over that person’s friends, and collect all the results:
def friends_of_friend_ids_bad(user):
	# "foaf" is short for "friend of a friend"
	return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"]]

print("People user Hero may know:", [friend["id"] for friend in users[0]["friends"]])
print("People user Dunn may know:", [friend["id"] for friend in users[1]["friends"]])
print("People user Sue may know:", [friend["id"] for friend in users[2]["friends"]])


# Knowing that people are friends-of-friends in multiple ways seems like interesting information, so maybe instead we should produce a count of mutual friends. And we definitely should use a helper function to exclude people already known to the user:
from collections import Counter

def not_the_same(user, other_user):
	""" two users are not the same if they have different ids """
	return user["id"] != other_user["id"]

def not_friends(user, other_user):
	""" other_user is not a friend if hes not in user["friends"]; that is, if hes not_the_same as all the people in user["friends"] """
	return all(not_the_same(friend, other_user) for friend in user["friends"])

def friends_of_friend_ids(user):
	return Counter(foaf["id"] for friend in user["friends"] for foaf in friend["friends"] if not_the_same(user, foaf) and not_friends(user, foaf))

print("People User Chi may know:", friends_of_friend_ids(users[3]))
# This correctly tells Chi ( id 3) that she has two mutual friends with Hero ( id 0) but only one mutual friend with Clive ( id 5)



""" As a data scientist, you know that you also might enjoy meeting users with similar interests. (This is a good example of the “substantive expertise” aspect of data sci‐ ence.) After asking around, you manage to get your hands on this data, as a list of pairs (user_id, interest) : """

interests = [
	(0, "Hadoop"),
	(0, "Big Data"), 
	(0, "HBase"), 
	(0, "Java"),
	(0, "Spark"), 
	(0, "Storm"), 
	(0, "Cassandra"),
	(1, "NoSQL"),
	(1, "MongoDB"),
	(1, "Cassandra"),
	(1, "HBase"),
	(1, "Postgres"), 
	(2, "Python"), 
	(2, "scikit-learn"), 
	(2, "scipy"),
	(2, "numpy"), 
	(2, "statsmodels"), 
	(2, "pandas"), 
	(3, "R"), 
	(3, "Python"),
	(3, "statistics"),
	(3, "regression"), 
	(3, "probability"),
	(4, "machine learning"), 
	(4, "regression"), 
	(4, "decision trees"),
	(4, "libsvm"), 
	(5, "Python"), 
	(5, "R"), 
	(5, "Java"), 
	(5, "C++"),
	(5, "Haskell"), 
	(5, "programming languages"), 
	(6, "statistics"),
	(6, "probability"), 
	(6, "mathematics"), 
	(6, "theory"),
	(7, "machine learning"), 
	(7, "scikit-learn"), 
	(7, "Mahout"),
	(7, "neural networks"), 
	(8, "neural networks"), 
	(8, "deep learning"),
	(8, "Big Data"), 
	(8, "artificial intelligence"), 
	(9, "Hadoop"),
	(9, "Java"), 
	(9, "MapReduce"), 
	(9, "Big Data")
]

# For example, Thor ( id 4) has no friends in common with Devin ( id 7), but they share an interest in machine learning.
# It’s easy to build a function that finds users with a certain interest:
def data_scientists_who_like(target_interest):
	return [user_id for user_id, user_interest in interests if user_interest == target_interest]
# print("People User Chi has interests with:", data_scientists_who_like(users[3]))

""" This works, but it has to examine the whole list of interests for every search. If we
have a lot of users and interests (or if we just want to do a lot of searches), we’re prob‐
ably better off building an index from interests to users """
from collections import defaultdict

# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
	user_ids_by_interest[interest].append(user_id)

""" And another from users to interests: """

# keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
	interests_by_user_id[user_id].append(interest)

""" 
Now it’s easy to find who has the most interests in common with a given user:
	• Iterate over the user’s interests.
	• For each interest, iterate over the other users with that interest.
	• Keep count of how many times we see each other user. 
"""

def most_common_interests_with(user):
	return Counter(interested_user_id for interest in interests_by_user_id["id"] for interested_user_id in user_ids_by_interest[interest] if interested_user_id != user['id'])

print("People User Chi has interests with:", most_common_interests_with(users[3]))








































