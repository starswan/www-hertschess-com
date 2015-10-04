import urllib2, HTMLParser, cookielib

from BeautifulSoup import BeautifulSoup
import requests

site = "http://www.c4results.org.uk"
siteurl = "http://www.c4results.org.uk/chess/php/"
top_url = "http://www.c4results.org.uk/chess/php/index.php"
dbversion = { 'DBVersion': '2014-15' }

eacu_teams = ['1st Team', 'U160']

class SiteAccessor(object):
  def __init__(self):
    self.cookies = cookielib.CookieJar()
    self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
  def follow_url(self, url):
    self.opener.open(url)
  def load_url(self, base):
    if base.find('?') >= 0:
      url = base + '&'
    else:
      url = base + '?'

    for p in dbversion:
      url = url + p + '=' + dbversion[p]
    webpage = self.opener.open(url)
    top_page = BeautifulSoup(webpage.read())
    return top_page

accessor = SiteAccessor()

def process_team(link):
   print link['href'], link.contents
   #league_page = BeautifulSoup(urllib.urlopen(site + link['href']).read())
   #print league_page

def start_new():
  resp = requests.get(thisurl, params=dbversion)
  print resp.cookies
  top_page = BeautifulSoup(resp.text)
  return top_page

top_page = accessor.load_url(top_url)
#print top_page
for league in top_page.findAll('tr'):
  columns = league.findAll('td')
  if len(columns) > 0:
    if columns[0].contents[0].startswith('EACU'):
      for bit in columns:
        print bit.contents
      print
      href = columns[1].contents[0]['href']
      print 'First Href', href
      #page = BeautifulSoup(urllib2.urlopen(site + href).read())
      page = accessor.load_url(site + href)
      rows = page.findAll('tr')
      for row in rows:
         cells = row.findAll('td')
         if len(cells) > 0:
            anchors = cells[0].findAll('a')
            if len(anchors) > 0:
               if anchors[0].contents[0].startswith('EACU County'):
                  href = anchors[0]['href']
                  print 'Second Href', href
                  #eacupage = BeautifulSoup(urllib2.urlopen(siteurl + href).read())
                  eacupage = accessor.load_url(siteurl + href)
                  for link in eacupage.findAll('a'):
                     for team in eacu_teams:
                        if link.contents[0].endswith(team):
                           process_team(link)
