from rauth import OAuth1Service
import json
import requests
import urllib2

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
pin = input('Enter PIN from browser: ')
session = xing.get_auth_session(request_token,
                                   request_token_secret,
                                   method='POST',
                                   data={'oauth_verifier': pin})
r = session.get('/v1/users/find',
                params={'keywords': 'php,bangalore','format':'json','limit':'100','user_fields':'page_name'},
                header_auth=True)
response_json = r.json()
