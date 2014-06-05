from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect

from blog.models import Post, Tag, Comment
from blog.forms import CommentForm

def index(request):
    context = RequestContext(request)
    posts = Post.objects.all()
    tags = Tag.objects.all()
    context_dict = {'tags': tags, 'posts': posts}
    return render_to_response('blog/index.html',
                              context_dict, context)

def tag(request, t_id):
    context = RequestContext(request)
    tag = get_object_or_404(Tag, text=t_id)
    posts = Post.objects.filter(tags=tag)
    tags = Tag.objects.all()
    context_dict = {'tags': tags, 'posts': posts}
    return render_to_response('blog/index.html',
                              context_dict, context)

def detail(request, p_id):
    context = RequestContext(request)
    tags = Tag.objects.all()
    context_dict = {'tags': tags}

    post = get_object_or_404(Post, id=p_id)
    context_dict['post'] = post

    comments = Comment.objects.filter(post=post)
    context_dict['comments'] = comments

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', p_id=p_id)
    else:
        form = CommentForm()

    context_dict['comment_form'] = form
    return render_to_response('blog/detail.html',
                              context_dict, context)
