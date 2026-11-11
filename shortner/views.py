from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import UrlForm
from .models import Url
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {'urls':Url.objects.filter(owner=request.user)}
    return render(request, 'shortner/home.html', context)

@login_required
def create_url(request):
    if request.method != 'POST':
        form = UrlForm()
    else:
        form = UrlForm(data=request.POST)
        if form.is_valid():
            new_url = form.save(commit=False)
            new_url.owner = request.user
            new_url.save()
            return HttpResponseRedirect(reverse('home'))

    context = {'form':form}
    return render(request, 'shortner/create_url.html', context)

@login_required
def edit_url(request, shortned_url):
    url = Url.objects.get(shortned_url=shortned_url)
    if url:
        if request.method != 'POST':
            form = UrlForm(instance=url)
        else:
            form = UrlForm(instance=url, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('home'))

        context = {'url':url,'form':form}
        return render(request, 'shortner/edit_url.html', context)
    else:
        raise Http404

@login_required
def delete_url(request, shortned_url):
    url = Url.objects.get(shortned_url=shortned_url)
    if url:
        url.delete()
        return HttpResponseRedirect(reverse('home'))
    else:
        raise Http404

def acess_url(request, shortned_url):
    url = Url.objects.get(shortned_url=shortned_url)
    if url:
        return HttpResponseRedirect(url.original_url)
    else:
        raise Http404


