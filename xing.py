from rauth import OAuth1Service
import json
import requests
import urllib3

xing = OAuth1Service(
    name='xing',
    consumer_key='5eaa67ac6ad0b6594a09',
    consumer_secret='8e77ff505bb0cb90977b183411baa5f3c35b9620',
    request_token_url='https://api.xing.com/v1/request_token',
    access_token_url='https://api.xing.com/v1/access_token',
    authorize_url='https://api.xing.com/v1/authorize',
    base_url='https://api.xing.com/v1/'
    )

request_token, request_token_secret = xing.get_request_token(
        params={'oauth_callback':'nil'})

authorize_url = xing.get_authorize_url(request_token)

print 'Visit this URL in your browser: ' + authorize_url
pin = input('Enter PIN from the oauth_verifier field '
	'(last 4 digits in the redirect URL): ')
session = xing.get_auth_session(request_token,
                                   request_token_secret,
                                   method='POST',
                                   data={'oauth_verifier': pin})

keywords = raw_input("Enter comma separated keywords"
					" to search for - ")
count = raw_input("No of search results desired - ")

response = session.get('/v1/users/find',
                params={'keywords': keywords,'format':'json',
                'limit':count, 'user_fields':'page_name, haves'},
                header_auth=True)
profile_data = response.json()

# Print the data obtained in the get request.
for i in range(0,int(count)):
    print(i+1)
    print 'Name :', profile_data['users']['items'][i]['user']['page_name']
    print 'Skills :', profile_data['users']['items'][i]['user']['haves']
    print('\n')
