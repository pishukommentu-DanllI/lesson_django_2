from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse(f'''
    <p>Host: {request.META['HTTP_HOST']}</p>
    <p>Info_about_browser: {request.META['HTTP_USER_AGENT']}</p>
    <p>Ip: {request.META['REMOTE_ADDR']}</p>
''')

def error(request, status=400, message='Unfortunately an error has occurred'):
    return HttpResponse(f'''
    <p>Status: {status}</p>
    <p>Message: {message}</p>
''', status=status, reason=message)

def folders(request, login='Daniil', name_folder='folder_to_1', number='12'):
    return HttpResponse(f'''
    <p>Login = {login}, folder = {name_folder}, number = {number}
''')

