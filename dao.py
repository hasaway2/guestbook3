import datetime as d

guest_books=[]
gno=1

def save(content:str, writer:str)->bool:
  global gno
  writeday = d.datetime.now().date()
  guest_books.append(dict(gno=gno, writeday=writeday, content=content, writer=writer))
  gno+=1
  return True

def findall()->list:
  return guest_books

def findone(gno)->dict:
  for gb in guest_books:
    if gb['gno']==gno:
      return gb
  return None

def update(gno, content)->bool:
  for gb in guest_books:
    if gb['gno']==gno:
      gb['content']=content
      return True
  return False 

def delete(gno)->bool:
  for gb in guest_books:
    if gb['gno']==gno:
      guest_books.remove(gb)
      return True
  return False 