import urllib.request
from urllib.parse import quote
import string

class HtmlDownloader(object):
    #一个参数，需要下载的url
    def download(self, url):
        if url is None:
            return None
        url=quote(url,safe=string.printable)
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()