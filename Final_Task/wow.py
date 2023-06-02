def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    import numpy as np

    def function_knife(number,predict,count=None,x=None,y=None):
        if (x==None and y==None):
            x,y=1,101
        
        if count==None:
          count=1
        else:
          count+=1
        predict=np.random.randint(x,y)
        if predict==number:
            return count
        elif predict > number:
            return function_knife(number,predict,count,x,y=predict+1)
        elif predict < number:
            return function_knife(number,predict,count,y,x=predict)
    
    predict = (np.random.randint(1, 101))
    count=function_knife(number,predict,count=None,x=None,y=None)
    print(count)
    

    # Ваш код заканчивается здесь

    return count
#---------------------
asd=game_core_v3()
print('По итогу count = ',asd)

