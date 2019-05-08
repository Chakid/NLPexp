# 用字典作为函数的参数
def get_square_list(num=0, l=[], dic={}):
  for i in range(num):
    l.append(i**2)
    pass
  dic[num] = l
  print ("list:",l)
  print ("dict:",dic)
  print ("l id:",id(l),"  |  dic id:",id(dic))

def new_get_square_list(num=0, l=[], dic={}):
  if not l :
    l = []
  if not dic :
    dic = {}
  for i in range(num):
    l.append(i**2)
    pass
  dic[num] = l
  print ("list:",l)
  print ("dict:",dic)
  print ("l id:",id(l),"  |  dic id:",id(dic))

if __name__ == "__main__":
  print ("ERROR!!:get_square_list")
  get_square_list(2)
  get_square_list(3)
