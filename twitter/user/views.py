from django.shortcuts import render
from .models import user
from .forms import UserForm
from django.shortcuts import get_object_or_404,redirect


# Create your views here.
def index(request):
    return render(request,'index.html')

def tweet_list(request):
    tweets=user.objects.all().order_by('-created_at')
    return render(request,'tweetlist.html',{'tweets':tweets})

def tweet_create(request):
    if request.method == 'POST':
       form = UserForm(request.POST,request.FILES)
       if form.is_valid():
           tweet=form.save(commit=False)
           tweet.user=request.user
           tweet.save()
           return redirect('tweet_list')

    else:
        form= UserForm()
        return render(request,'tweetform.html',{'form':form})