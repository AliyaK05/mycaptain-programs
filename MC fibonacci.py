#writing a fibbonachi sequence until the first n numbers#

num= int(input("until how many numbers do you want this fibonacci series?"))
n1=0
n2=1
print (n1)
print (n2)
for x in range (2,num):
 n3= n1+n2
 n1=n2
 n2=n3
 print(n3)
