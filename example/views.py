from django.http import HttpResponse
from django.utils import timezone


def index(request):
    now = timezone.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercl!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
