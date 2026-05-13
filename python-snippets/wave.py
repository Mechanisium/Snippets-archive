
import time
'''while True:
    for a in [1,2,3,4,5,6,5,4,3,2,1]:
        
        x='*'
        print(x*a,end='\r')
        
        
        
        time.sleep(0.25)
        print(end='               ')

        time.sleep(0.25)
p='pppp'

k='kk'

print(p,end='\r')
time.sleep(2)
print(end='    ')

print(k)
'''

'''
s='/'
s1='-'
s2='\\'
s3='|'
while True:
    print(s,end='\r')
    time.sleep(0.25)
    print(s1,end='\r')
    time.sleep(0.25)
    print(s2,end='\r')
    time.sleep(0.25)
    print(s3,end='\r')
    time.sleep(0.25)
    
'''
def moving_bar():
    s1='   ***   ***   ***   ***'
    s2='*   ***   ***   ***   **'
    s3='**   ***   ***   ***   *'
    s4='***   ***   ***   ***   '
    s5=' ***   ***   ***   ***  '
    s6='  ***   ***   ***   *** '
    while True:
        for a in [s1,s2,s3,s4,s5,s6]:
            print(a,end='\r')
            time.sleep(0.5)
        
        
moving_bar()

    
    
    
    
    
    
    
    
    
    
    
    
    
    