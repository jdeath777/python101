#program to find the memory of variables

#defining strings
s1,s2,s3 = "first","second","third"

#defining int
c,d,e = 1,2,3

#defining float
f,f1,f2 = 1.234,3.456,3.666


#show the memory using id function

print("The memory location output are")

print("The memory locations of string: \ns1 :",id(s1),"\ns2 :",id(s2),"\ns3 :",id(s3))

print("The memory locationsn of the int: \nc :",id(c),"\nd :",id(d),"\ne :",id(e))

print("The memory location of the float: \nf :",id(f),"\nf1",id(f1),"\nf2",id(f2))

