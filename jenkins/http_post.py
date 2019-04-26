import urllib
import urllib2

post_data = urllib.urlencode({})
response = urllib2.urlopen('url', post_data)
print(response.read())
print(response.getheaders())
