list=[1,2,3,4,5]

for n in list:
    print(n)
    
for i in range(len(list)):
    print(list[i])
    
    
string="malayalam"
if string==string[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
    
    
    
for i,n in enumerate(list):
    print(i,n)