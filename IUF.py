import json

#Load the json file
def followers_list():
    with open ('assets/followers.json') as json_file:
        data=json.load(json_file)

    # create an empty array to hold the values
    followers_values = []

    # iterate through the relationships_followers list
    for relationship in data['relationships_followers']:
        # iterate through the string_list_data list
        for string_data in relationship['string_list_data']:
            # append the value to the values array
            followers_values.append(string_data['value'])

    # print the values array
    print(followers_values)
    print(len(followers_values))


def following_list():
    with open ('assets/following.json') as json_file:
        data=json.load(json_file)

    # create an empty array to hold the values
    following_values = []

    # iterate through the relationships_followers list
    for relationship in data['relationships_following']:
        # iterate through the string_list_data list
        for string_data in relationship['string_list_data']:
            # append the value to the values array
             following_values.append(string_data['value'])

    # print the values array
    print( following_values)
    print(len(following_values))

followers_list()
