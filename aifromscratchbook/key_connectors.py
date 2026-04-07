from collections import Counter

users = [
    {"id": 0, "name": "Bob"},
    {"id": 1, "name": "Sally"},
    {"id": 2, "name": "Jane"},
    {"id": 3, "name": "John"},
    {"id": 4, "name": "Julian"},
    {"id": 5, "name": "Sue"},
    {"id": 6, "name": "Lucas"},
    {"id": 7, "name": "Sam"},
    {"id": 8, "name": "Mary"},
    {"id": 9, "name": "Levi"},
]

friendship_pairs = [
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
    (8, 9),
]

# Init the dict with an empty list for each user id
friendships = {user["id"]: [] for user in users}

print(friendships)

for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of i
    friendships[j].append(i)  # Add i as a friend of j


def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)


total_connections = sum(number_of_friends(user) for user in users)
avg_connections = total_connections / len(users)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
# Sort the list by the number of friends largest to smallest
num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1], reverse=True
)


def foaf_ids_bad(user):
    """foaf is short for "friend of a friend" """
    return [
        foaf_id
        for friend_id in friendships[user["id"]]
        for foaf_id in friendships[friend_id]
    ]


def friends_of_friends(user):
    """For each of my friends, find their friends who aren't me and aren't my friends"""
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id and foaf_id not in friendships[user_id]
    )
