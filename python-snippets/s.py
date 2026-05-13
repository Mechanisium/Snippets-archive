

def scrolprint(x):
    import time
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','+','-','*','_','.','<']
    Input=x
    var=''
    for character in list(Input):
        for a in alpha:
            print(var+a,end='\r')
            time.sleep(0.05)
            if a == character:
                var=var+a
                print(var,end='\r')
                break
            
scrolprint(input('here:'))
