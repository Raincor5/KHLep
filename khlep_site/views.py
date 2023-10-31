from django.shortcuts import render

def index(requests):
    """Index page."""
    return render(requests, 'khlep_site/index.html')
