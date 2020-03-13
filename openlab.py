import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
local_filename, headers = urllib.request.urlretrieve('http://python.org/')
html = open(local_filename)