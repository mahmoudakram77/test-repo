from django.shortcuts import render , get_object_or_404
from .models import Post
from django.http import Http404
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger
from .forms import EmailPostForm
from django.core.mail import send_mail
# def post_list(request):
#   posts = Post.objects.all()
#   paginator = Paginator(posts, 1)
#   page_number = request.GET.get('page')
#   page_obj = paginator.get_page(page_number)
  
#   return render(request, 'blog/post_list.html',{'page_obj':page_obj})

class PostListView(ListView):
    model = Post
    paginate_by = 1
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'




# Create your views here.

def post_detail(request , slug):
    post = get_object_or_404(Post , slug=slug , status=Post.Status.PUBLISHED)

    return render(request, 'blog/post_detail.html', {'post':post})





def post_share(request, slug):
    post = get_object_or_404(Post, slug=slug)
    sent = False
    recipient_email = None
    sender_email = None
    
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you reading '{post.title}'"
            message = f"Read {post.title} at {post_url}\n{cd['name']}'s comments: {cd['comments']}\n\nSent by: {cd['from_email']}"
            
            send_mail(subject, message, 'mahmoudeljaru@gmail.com', [cd['to']])
            
            # Set the sent flag to True and store the recipient and sender email
            sent = True
            recipient_email = cd['to']
            sender_email = cd['from_email']
            
            # Clear the form
            form = EmailPostForm()
    else:
        form = EmailPostForm()
    
    context = {
        'form': form,
        'post': post,
        'sent': sent,
        'recipient_email': recipient_email,
        'sender_email': sender_email
    }
    
    return render(request, 'blog/post_share.html', context)
           
