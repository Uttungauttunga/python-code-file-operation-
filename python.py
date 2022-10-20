import pandas
from collections import Counter
from matplotlib import pyplot as plt

inputfile=input("enter the text file name:");

f=open(inputfile,'w');
print("please write the content of the file");
k=input()

while(True):
   
    print("do u want to write the content in the next line enter 1 else enter 0")
    if(int(input())==1):
        k+="\n"
        k+=input();
    else:
        break;
        
f.write(k)
f.close()

f=open(inputfile,'r');
s=''
alphastring=""
s=(f.read())

count=0
uppercase=0
lowercase=0


for i in range(len(s)):
    if(65<=ord(s[i])<=90):
        uppercase+=1;
        alphastring+=s[i];
        

    elif(97<=ord(s[i])<=122):
        lowercase+=1;
        alphastring+=s[i];



alphastring=list(alphastring)

alphastring.sort()


letter_counts = Counter(alphastring)

for i in range(65,91):
    print(chr(i),"---->",s.count(chr(i)));
    

for i in range(97,123):
    print(chr(i),"---->",s.count(chr(i)));



print("The file includes",uppercase,"uppercase letters");
print("The file includes",lowercase,"lowercase letters");

if(len(alphastring)!=0):
    
  plt.bar(dict(letter_counts).keys(),dict(letter_counts).values())
  plt.show()
