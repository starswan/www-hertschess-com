#
# $Id$
#
from BeautifulSoup import BeautifulSoup
import sys, string
import HTMLParser

parser = HTMLParser.HTMLParser()

soup = BeautifulSoup(file(sys.argv[1]).read())

def writeToFile(items):
  print string.join(['"' + i + '"' for i in items], ',')

for division in soup.findAll('tr', {'bgcolor':'silver'}):
  parent = division.parent
  rows = parent.findAll('tr')
  division_name = rows[0].contents[0].contents[0].contents[0]
  division = division_name.split(' ')[1]
  headers = [str(cell.contents[0]) for cell in rows[0].findAll('b')]
  # Headers are <Division> <Team1> <Team2> <...> <M> <For> <Agin>
  print headers

  # Each row is the results for 1 team:
  # <TeamName> <a onclick=popup(lots of html)>
  # ----- when a team is due to play itself :-)
  for row in rows[1:]:
    for cell in row.findAll('td'):
      link = cell.find('a')
      if link:
        popup = link['onclick']
        html = popup[13:-3]
        chessmatch = BeautifulSoup(html)
        matchdate = chessmatch.find('p').contents[2]
        # First matchrow is team data again, second and subsequent is the players(with grades) and result between them
        # Last row is the match score
        matchrows = chessmatch.findAll('tr')
        headercells = matchrows[0].findAll('td')
        print division, 'Match', matchdate, headercells[1].contents[0], headercells[4].contents[0]
        for matchrow in matchrows[1:-1]:
          matchcells = matchrow.findAll('td')
          cells = [str(cell.contents[0]) for cell in matchcells]
          print 'Board', cells
        print 'Match Result', matchrows[-1].findAll('td')[3].contents[0]
