from django.http import HttpResponse
from django.utils import timezone


def index(request):
    now = timezone.now().strftime('%A, %d %B %Y at %X')
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
