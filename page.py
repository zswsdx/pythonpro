from urllib import request, parse
import gzip
from http import cookiejar
from bs4 import BeautifulSoup


class WebPage:
    def __init__(self, cookieName):
        self.cookieName = cookieName
        httphd = request.HTTPHandler(debuglevel=1)
        httpshd = request.HTTPSHandler(debuglevel=1)
        self.ckojb = cookiejar.LWPCookieJar(self.cookieName)
        cookiehd = request.HTTPCookieProcessor(self.ckojb)
        self.opener = request.build_opener(httphd, httpshd, cookiehd)

    def getPage(self, url, postData=None, headerInfo={}):
        if postData:
            postData = parse.urlencode(postData).encode('utf-8')
        reqhd = request.Request(url, data=postData, headers=headerInfo)
        req = self.opener.open(reqhd)
        con = req.read()
        coding = req.headers.get('Content-Encoding')
        if coding == 'gzip':
            con = gzip.decompress(con)
        con = con.decode('utf-8')
        return con

    def getHtml5(self, con):
        return BeautifulSoup(con, 'html5lib')

    def saveCookie(self):
        self.ckojb.save(ignore_discard=True, ignore_expires=True)

    def loadCookie(self):
        self.ckojb.load(self.cookieName, ignore_expires=True, ignore_discard=True)
