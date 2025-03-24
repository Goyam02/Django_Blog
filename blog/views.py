from django.shortcuts import render
# from django.http import HttpResponse  //no longer needed because we are using render

posts = [
{
    'author': 'Goyam02',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'March 23, 2025'
},
{
    'author': 'Jain Goyam',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'March 23, 2025'
}

]



# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html' , {'title': 'About'})
