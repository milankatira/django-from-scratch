
'''
def my_middleware(get_response):
 print("One Time Initialization")
 def my_function(request):
  print("This is before view")
  response = get_response(request)
  print("This is after view")
  
  return response
 return my_function

class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization")

    def __call__(self, request):
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return response
 '''




from django.shortcuts import HttpResponse
class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(request, *args, **kwargs):
        print("This is Process View -  Before View")
        # return HttpResponse("This is before view")
        return None


class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print("Exception Occured")
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        print(msg)
        return HttpResponse(msg)

class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print("Process Template Response From Middleware")
        response.context_data['name'] = 'milan'
        return response