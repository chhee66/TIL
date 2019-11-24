# 8장 종합문제-2.py

a = {'A':90, 'B':80}
'''
try:
    print(a['C'])
except Exception:
    print('70')
    '''
'''
if 'C' not in a:
    print('70')
    '''
result = a.get('C', '70')
print(result)
