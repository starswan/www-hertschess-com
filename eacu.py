import urllib, HTMLParser

from BeautifulSoup import BeautifulSoup

site = "http://www.c4results.org.uk"
siteurl = "http://www.c4results.org.uk/chess/php/"
thisurl = "http://www.c4results.org.uk/chess/php/index.php?DBVersion=2014-15"

eacu_teams = ['1st Team', 'U160']

handle = urllib.urlopen(thisurl)
top_page = BeautifulSoup(handle.read())
#print top_page
for league in top_page.findAll('tr'):
  columns = league.findAll('td')
  if len(columns) > 0:
    if columns[0].contents[0].startswith('EACU'):
      for bit in columns:
        print bit.contents
      print
      href = columns[1].contents[0]['href']
      page = BeautifulSoup(urllib.urlopen(site + href).read())
      href = page.findAll('td')[0].contents[0]['href']
      eacupage = BeautifulSoup(urllib.urlopen(siteurl + href).read())
      for link in eacupage.findAll('a'):
        for team in eacu_teams:
           if link.contents[0].endswith(team):
              print link['href'], link.contents
