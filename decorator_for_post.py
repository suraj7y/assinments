class Request:
    def __init__ (self, method):
        self.method = method

def another_decorator (f):
    print ("another")
    return f

def decorator_for_post (f):
    def g (request, *args, **kwargs):
        if request.method == "POST":
            return another_decorator (f) (request, *args, **kwargs)
        return f (request, *args, **kwargs)

    return g

@decorator_for_post
def x (request):
    print ("doing x")

print ("GET")
x (Request ("GET") )
print ("POST")
x (Request ("POST") )
