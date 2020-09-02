
def Layout(function):
    def wrapper():
     innerresult=function()
     result=innerresult**3
     return result
    return wrapper
@Layout
def Number():
    a=6
    return a
print(Number())



