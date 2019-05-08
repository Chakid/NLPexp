import jieba
f = open("../txt/hlm.txt","r",encoding='UTF-8')   #设置文件对象

data=open("exp5_3.txt",'w+',encoding='utf-8')
str = f.read()     #将txt文件的所有内容读入到字符串str中
words = jieba.lcut(str)
#print(words)

counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        rword = word
        counts[rword] = counts.get(rword,0) + 1
        #print(counts)

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for item in items:
    word, count = item
    #print("{0:<10} {1:>5}".format(word, count))
    strC = "{0:<10} {1:>5}".format(word, count)
    print(strC,file=data)
    # 写入字符串
    #os.write(fd, strC+"\n")


f.close()   #将文件关闭

