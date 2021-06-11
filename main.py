proj=input()
try:
  if proj < 0:
    print("negative integer")
  elif proj == 0:
    print("zero integer")
  else:
    print("input",proj)
except:
  print("Done")
