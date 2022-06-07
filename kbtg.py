A="""my.song.mp3 555b
betty.mp4 10b
Batman.org 19b"""



A=A.splitlines()
#print(A)
i=0
for word in A:
    A[i]=word.split()
    A[i]=[(A[i][0].split('.'))[-1],(A[i][1])[:-1]]
    i=i+1
print(A)

summary={'music':0,'image':0,'movie':0,'other':0}
for eachfile in A:
    if eachfile[0] in ['mp3','aac','flac']:
        summary['music']=summary['music']+int(eachfile[1])
        
        
#print(summary['music'])

n=10
n=str(n)

for i in range(len(n)):
    print(n[i])
