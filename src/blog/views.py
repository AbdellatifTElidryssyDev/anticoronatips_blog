from django.shortcuts import render

def home(request):

    context = {

            'title':'الصفحة الرئيسية',
            'content-section':'contents',
        }

    return render(request, 'blog/index.html', context)


def hadiths(request):
    return render(request, 'blog/hadiths.html', {'title':'احاديث دينية'})


def videos(request):
     return render(request, 'blog/videos.html', {'title':'فيديوهات إرشادية'})

def coronaintheworld(request):
    return render(request, 'blog/coronaintheworld.html', {'title':'كورونا حول العالم'})

def statistics(request):
    return render(request, 'blog/statistics.html', {'title':'إحصائيات الوباء في المغرب'})
        
