import urllib.request
import sys 

def download_function(url):
    content = urllib.request.urlopen(url)
    page_content = content.read()