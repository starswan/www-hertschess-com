from utils import commaSep

HEADER_TRANS = { 'TEAM':'Team Name', 'PLAYED':'P', 'WON':'W', 'DRAWN':'D', 'LOST':'L', 
                'GAMES':'For','POINTS':'Ps', 'POSITION':'Position', 'DIVISION':'Division'}

def celldata(cells, division, index):
  if index == 1:
    return cells[index].findAll('a')[0].contents[0] + division
  elif index > 7:
    return cells[index]
  else:
    return cells[index].contents[0].replace('&#189;','.5')

def make_header_dict(table):
  header_data = table.findAll('th')

  header_dict = { 'TEAM':1, 'POSITION':8, 'DIVISION':9 }
  index = 0
  for header in header_data:
    if len(header.contents) > 0:
       header_dict[header.contents[0]] = index
    index = index + 1
  return header_dict

def print_headers(table):
  header_dict = make_header_dict(table)
  print commaSep([HEADER_TRANS[h] for h in header_dict])

def parse(division, table):
  header_dict = make_header_dict(table)

  index = 1
  for row in table.findAll('tr')[1:6]:
    cells = row.findAll('td')
    cells.append(str(index))
    cells.append(division)
    data = [celldata(cells, division, header_dict[h]) for h in header_dict]
    print commaSep(data)
    index = index + 1

if __name__ == '__main__':
  import sys, BeautifulSoup
  division = sys.argv[1]
  table = BeautifulSoup.BeautifulSoup(file(division + '.html').read())

  print_headers(table)
  parse(division, table)
