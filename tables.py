#
# $Id$
#
from BeautifulSoup import BeautifulSoup
import sys, string
import HTMLParser
from utils import commaSep

parser = HTMLParser.HTMLParser()

soup = BeautifulSoup(file(sys.argv[1]).read())

#def commaSep(items):
#  return ",".join(['"' + i + '"' for i in items])

for division in soup.findAll('tr', {'bgcolor':'silver'}):
  parent = division.parent
  rows = parent.findAll('tr')
  division_name = rows[0].contents[0].contents[0].contents[0]
  division = division_name.split(' ')[1]
  headers = [str(cell.contents[0]) for cell in rows[0].findAll('b')]
  headers[0] = 'Team Name'
  headers.append('Division')
  headers.append('Position')
  if division == "1":
    print commaSep(headers)

  position = 1
  for row in rows[1:]:
    data = [parser.unescape(str(cell.contents[0])) for cell in row.findAll('td') if str(cell.contents[0]) != '&nbsp;']
    data.append(division)
    data.append(str(position))
    position = position + 1
    print commaSep(data)
