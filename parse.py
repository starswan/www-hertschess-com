import sys, BeautifulSoup

table = BeautifulSoup.BeautifulSoup(file(sys.argv[1]).read())

header_data = table.findAll('th')

header_dict = { 'TEAM':1 }
index = 0
for header in header_data:
   if len(header.contents) > 0:
      header_dict[header.contents[0]] = index
   index = index + 1

def commaSep(array):
  return ",".join(['"' + a.strip() + '"' for a in array])

print commaSep([h for h in header_dict])

def celldata(cells, index):
  if index == 1:
    return cells[index].findAll('a')[0].contents[0]
  else:
    return cells[index].contents[0].replace('&#189;','.5')

for row in table.findAll('tr')[1:6]:
  cells = row.findAll('td')
  print commaSep([celldata(cells, header_dict[h]) for h in header_dict])
