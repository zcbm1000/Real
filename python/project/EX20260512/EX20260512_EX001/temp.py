# 데이터 중 실수는 현존하는 어떤 언어도 완벽하게 컨트롤 불가

'''
.1부터 .1씩 점차적으로 증가시킴
'''

# flt = .1
# while True:
#     print(f'flt{flt}')
#     flt += .1

#     if flt >= 1:
#         break

total = .1+ .2            # theory : 0.3 이되야함
print(f'total: {total}')  # total  : 0.30000000000000004
if total > 0.3:
    print('total은 0.3보다 크다.')