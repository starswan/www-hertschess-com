def commaSep(array):
  return ",".join(['"' + a.strip() + '"' for a in array])
