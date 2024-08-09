p, m = map(int, input().split())
roomList = list()

for _ in range(p) :
  l, n = input().split()
  l = int(l)
  
  flg = False
  
  for room in roomList :
    if len(room) < m and abs(l - room[0][0]) <= 10 :
      room.append((l, n))
      flg = True
      break
  if not flg :
    roomList.append([(l, n)])

for room in roomList :
  print('Started!' if len(room) == m else 'Waiting!')
  room.sort(key = lambda x : x[-1])
  for l, n in room :
    print(l, n)