# SECOND MAXIMUM WITHOUT METHOD


# list1=[1,-2,6,8,-1,-7,-6]
# i=0
# while i<len(list1):
#     j=0
#     while j<len(list1):
#         if list1[i]<list1[j]:
#             b=list1[i]
#             list1[i]=list1[j]
#             list1[j]=b
#         j+=1
#     i+=1
# print(b)



list1=[1,-2,6,8,-1,-6,-7]
i=0
largest=list1[0]
sec=list1[0]
while i<len(list1):
    if list1[i]>largest:
        largest=list1[i]
    if list1[i]>sec and list1[i]!=largest:
        sec=list1[i]
    i+=1
print(sec)