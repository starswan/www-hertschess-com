import sys, BeautifulSoup
from utils import commaSep

HEADER_TRANS = { 'TEAM':'Team Name', 'PLAYED':'P', 'WON':'W', 'DRAWN':'D', 'LOST':'L', 
                'GAMES':'For','POINTS':'Ps', 'POSITION':'Position', 'DIVISION':'Division'}

def celldata(cells, index):
  if index == 1:
    return cells[index].findAll('a')[0].contents[0]
  elif index > 7:
    return cells[index]
  else:
    return cells[index].contents[0].replace('&#189;','.5')

def parse(division, table):
  header_data = table.findAll('th')

  header_dict = { 'TEAM':1, 'POSITION':8, 'DIVISION':9 }
  index = 0
  for header in header_data:
    if len(header.contents) > 0:
       header_dict[header.contents[0]] = index
    index = index + 1
  print commaSep([HEADER_TRANS[h] for h in header_dict])

  index = 1
  for row in table.findAll('tr')[1:6]:
    cells = row.findAll('td')
    cells.append(str(index))
    cells.append(division)
    data = [celldata(cells, header_dict[h]) for h in header_dict]
    print commaSep(data)
    index = index + 1

division = sys.argv[1]
table = BeautifulSoup.BeautifulSoup(file(division + '.html').read())

parse(division, table)
