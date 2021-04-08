n = int(input(),16)
for i in range(15):
    print('%X'%n, '*%X'%(i+1), '=%X'%(n*(i+1)), sep='') 


# 6081 : [기초-종합] 16진수 구구단 출력하기