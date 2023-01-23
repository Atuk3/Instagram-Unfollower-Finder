import json


# # connecting Flask from the __init__.py file to the main python file 
# from website import create_app
# app=create_app()

# if __name__=='__main__':
#     app.run(debug=True)

# create an empty array to hold the values
# followers_values = []
# following_values = []

# #Load the json file
# def followers_list():
#     with open ('assets/followers.json') as json_file:
#         data=json.load(json_file)

    
#     # iterate through the relationships_followers list
#     for relationship in data['relationships_followers']:
#         # iterate through the string_list_data list
#         for string_data in relationship['string_list_data']:
#             # append the value to the values array
#             followers_values.append(string_data['value'])

#     # print the values array
#     # print(followers_values)
#     # print(len(followers_values))


# def following_list():
#     with open ('assets/following.json') as json_file:
#         data=json.load(json_file)

   

#     # iterate through the relationships_followers list
#     for relationship in data['relationships_following']:
#         # iterate through the string_list_data list
#         for string_data in relationship['string_list_data']:
#             # append the value to the values array
#              following_values.append(string_data['value'])

#     print the values array
#     print( following_values)
#     print(len(following_values))



def compare_list():
    followers_list()
    following_list()
    not_in_followers = []
    for val in following_values:
        if val not in followers_values:
            not_in_followers.append(val)
    print("Following values which are not in followers_values:", not_in_followers)


compare_list()
