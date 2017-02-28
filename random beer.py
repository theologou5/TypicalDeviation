import urllib2
import json
import requests

key = 'YOUR API KEY HERE'
sandbox = 'YOUR SANDBOX URL HERE'
recipient = 'YOUR EMAIL HERE'

response = urllib2.urlopen(' https://api.punkapi.com/v2/beers/random ')
html = response.read().strip()
request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key), data={
    'from': 'hello@example.com',
    'to': recipient,
    'subject': 'Random Beer',
    'text': html
})

print 'Status: {0}'.format(request.status_code)
print 'Body:   {0}'.format(request.text)
