from django.shortcuts import render

def home(request):

    context = {

            'title':'الصفحة الرئيسية',
            'content-section':'contents',
        }

    return render(request, 'blog/index.html', context)


def hadiths(request):
    return render(request, 'blog/hadiths.html')


def videos(request):
     return render(request, 'blog/videos')

def coronaintheworld(request):
    return render(request, 'blog/coronaintheworld')

def statistics(request):
    return render(request, 'blog/statistics')
        
