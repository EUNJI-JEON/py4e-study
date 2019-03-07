fname= input('Enter File:')
if len(fname)<1: fname='clown.txt'
hand = open(fname)

di=dict()

for line in hand:
    line = line.rstrip()
    wds=line.split()
    for w in wds:
        #효율적인 idiom: retrieve/create/update counter
        di[w]=di.get(w,0)+1
#print(di)

#now we want to find the most common word
largest=-1
theword=None #어떤 키가 제일 큰 값을 가졌는지 알고 싶은데 어떤 키(단어)인지 모르므로 none
for k,v in di.items():
    #print(k,v)는 확인용이었으므로 comment로 바꿔줌
    if v>largest:
        largest = v
        theword= k #capture/remember the key that was largest

print(theword, largest) #'Done'도 확인용이었으므로 지워줬음
