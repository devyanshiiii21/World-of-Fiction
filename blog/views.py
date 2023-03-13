from django.shortcuts import render

posts = [
    {
        'author':'Collen Hoover',
        'title': 'Ugly Love',
        'summary':'lorem ipsum',
        'date_posted': 'January 16th, 2023',
    },
    {
        'author':'Collen Hoover',
        'title': 'Verity',
        'summary':'lorem ipsum',
        'date_posted': 'January 16th, 2023',
    },
    {
        'author':'Collen Hoover',
        'title': 'It Ends With Us',
        'summary':'lorem ipsum',
        'date_posted': 'January 16th, 2023',
    }
]


def home(request):
    return render(request,'blog/home.html',{
        'posts':posts
    })

def about(request):
    return render(request,'blog/about.html')


