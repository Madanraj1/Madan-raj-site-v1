from django.shortcuts import render


def Homepage_view(request):

    return render(request, 'main_site/home_page.html')

def journals(request):

     return render(request, 'main_site/journals.html')
