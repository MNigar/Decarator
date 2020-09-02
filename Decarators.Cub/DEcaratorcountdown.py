def Layout(function):
    def wrapper():
        innerresult=function()
        for i in range(innerresult):
            result=innerresult-i
            print(result)
    return wrapper
        
@Layout
def countdown():
    a=6
    return a
countdown()