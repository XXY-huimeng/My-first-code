import random as r
dia={"gold":"TC","grep":"CS","blue":"LYL"}
run=True
while run:
  print(f'you are luck,it is {dia[r.choice(list(dia.keys()))]}
  if input('would you like?') == 'q':
        run=False
