# def simple_middleware(get_response):
# # One-time configuration and initialization.
#     def middleware(request):
#     # Code to be executed for each request before
#     # the view (and later middleware) are called.
#         print("before response")
#         response = get_response(request)
#         print("After response")
#         # Code to be executed for each request/response after
#         # the view is called.
#         return response
#     return middleware

# class simple_middleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         print("Befoeeeeeeeeeeeeee")
#         response = self.get_response(request)
#         print("Afterrrrrrrrrrrr")
#         return response
    