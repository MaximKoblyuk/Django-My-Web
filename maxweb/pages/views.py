from django.shortcuts import render

def portfolio(request):
    """Portfolio/Presentation page view"""
    return render(request, 'pages/portfolio.html')
