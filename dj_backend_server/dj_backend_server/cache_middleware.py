
from django.utils.deprecation import MiddlewareMixin

class CustomCacheControlMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Cache-Control'] = 'must-revalidate, no-cache'

        return response
