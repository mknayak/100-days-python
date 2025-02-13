def TestFun(a=1,b=2,c=3):
    print(a,b,c)

TestFun(4,5)

#args is Tuple accepting > 1 arguments
def TestFunArgs(*args):
    print(args)

TestFunArgs(4,5)
TestFunArgs(4,5,"manas")

#kwargs (Key Word Args) is dictionary
def TestFunKwargs(**kwargs):
    print(kwargs)

TestFunKwargs(a=1,b=2,c=3)

def TestFunMix(a,b=1,*args,**kwargs):
    print(a,b,args,kwargs)

TestFunMix(2,3,2,2,2,2,d="manas")