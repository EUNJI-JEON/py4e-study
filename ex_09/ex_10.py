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
#print(di) 주석화

tmp=list()
for k,v in di.items():
    #print(v,k) 잘 만들어졌으면 주석화
    newt=(v,k)
    tmp.append(newt)
#print('Flipped',tmp) 잘 만들어졌는지 확인 됐음 주석화
tmp=sorted(tmp, reverse=True)
#print('Sorted',tmp[:5]) 잘 만들어졌는지 확인, 주석화

for v,k in tmp[:5]:
    print(k,v)
