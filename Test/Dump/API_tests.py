# import requests 
# import googleapiclient.discovery


# api_service_name = "youtube"
# api_version = 'v3'

# DEVELOPER_KEY = ""

# # API_CLIENT 

# youtube = googleapiclient.discovery.build(
#     api_service_name, api_version, developerKey=DEVELOPER_KEY)

# # request variable is the only thing needed to be changed 


# request = youtube.search().list(
#     part="id,snippet",
#     type="video",
#     q="summer of 69",
#     videoDuration="any",
#     maxResults="1"
# )

# response = request.execute()

# print (response)


''' 
- take the vedio url out of the api request 
- take the vedio url and put it into a variable
- put it into the vlc and pafy lib 

'''


from youtubesearchpython import *

def Discord_MV_url():
    variable = input("Enter a search term: ")
    customsearch = CustomSearch(variable, VideoSortOrder.viewCount,limit=1)

    for i in range(1):
        return (customsearch.result()['result'][i]['link'])

print (Discord_MV_url()) 



