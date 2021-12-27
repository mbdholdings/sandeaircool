from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from .forms import CommentForm, PostForm
from .models import Post, Comment, Author
from home_page.models import WelcomeWords, Intro, MissionVision, Slider, HeadingOne, HeadingTwo, HeadingThree, MidImage
from about.models import Ceo, AboutUs, Media, Team
from gallery.models import GallerySlider, Gallery, GalleryExtra
#from subscription.models import Signup
from service_products.models import  Preview, ServiceFive, ServiceSix, Sliding, Impression, ServiceOne, ServiceTwo, ServiceThree, Title, ServiceFour, ServiceFive, ServiceSix, TitleTwo, ServiceSeven

from publication.models import Publication
from opportunities.models import Opportunity


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) 
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)



def get_category_count():
    queryset = Post \
        .objects \
        .values('Categories__title') \
        .annotate(Count('Categories__title'))
    return queryset

def index(request):
    featured = Post.objects.filter(featured=True)
    most_recent = Post.objects.order_by('-timestamp')[:3]
    recent_projects = Opportunity.objects.order_by('-timestamp')[:4]

    welcome_words = WelcomeWords.objects.all()
    mission_vision = MissionVision.objects.all()
    
    slider = Slider.objects.all()

    heading_one = HeadingOne.objects.all()
    mid_image = MidImage.objects.all()
    heading_two = HeadingTwo.objects.all()
    heading_three = HeadingThree.objects.all()
    intro = Intro.objects.all()

    context = {
        'object_list': featured,
        'welcome_words' : welcome_words ,
        'mission_vision' : mission_vision ,
        'most_recent': most_recent,
        'slider' : slider,
        'heading_one' : heading_one,
        'mid_image' : mid_image,
        'heading_two' : heading_two,
        'heading_three': heading_three,
        'intro': intro,
        'recent_projects': recent_projects,
    }
    return render(request, 'index.html', context)


def blog(request):

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:4]
    post_list = Post.objects.order_by('-timestamp')

    paginator = Paginator(post_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {
        'queryset' : paginated_queryset,
        'page_request_var': page_request_var,
        'most_recent': most_recent,
        'category_count': category_count,
    }
    return render(request, 'blog.html', context)

def post(request, id):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:4]

    post = get_object_or_404(Post, id=id)

    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'most_recent': most_recent,
        'category_count': category_count,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'post.html', context)

def about(request):
    most_recent = Post.objects.order_by('-timestamp')[:4]
    ceo = Ceo.objects.all()
    about_us = AboutUs.objects.all()
    media = Media.objects.all()
    team = Team.objects.all()
    
    context = {
        'ceo': ceo,
        'about_us' : about_us, 
        'media' : media,
        'team': team,
        'most_recent': most_recent,
        
    }
    return render(request, 'about.html', context)

def gallery(request):
    gallery_slider = GallerySlider.objects.order_by('-timestamp')
    gallery = Gallery.objects.order_by('-timestamp')
    gallery_extra = GalleryExtra.objects.order_by('-timestamp')

    context = {
        'gallery_slider' : gallery_slider,
        'gallery' : gallery,
        'gallery_extra' : gallery_extra,
        
    }
    return render(request, 'gallery.html', context)

def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "post_create.html", context)

def post_update(request, id):
    title = 'Update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "post_create.html", context)

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("post-list"))

def service_products(request):
    preview = Preview.objects.all()
    sliding = Sliding.objects.all()
    impression = Impression.objects.all()

    service_one = ServiceOne.objects.all()
    service_two = ServiceTwo.objects.all()
    service_three = ServiceThree.objects.all()
    title = Title.objects.all()

    service_four = ServiceFour.objects.all()
    service_five = ServiceFive.objects.all()
    service_six = ServiceSix.objects.all()
    title_two = TitleTwo.objects.all()
    service_seven = ServiceSeven.objects.all()


   
    context = {
        'preview' : preview,
        'sliding' : sliding,
        'impression' : impression,
        'service_one' : service_one,
        'service_two' : service_two,
        'service_three' : service_three,
        'title' : title,
        'service_four' : service_four,
        'service_five' : service_five,
        'service_six' : service_six,
        'title_two' : title_two,
        'service_seven' : service_seven,


    }
    return render(request, 'services.html', context)


def publication(request):
    publication_list = Publication.objects.order_by('-timestamp')

    paginator = Paginator(publication_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {
        'queryset' : paginated_queryset,
        'page_request_var': page_request_var,

    }
    return render(request, 'library.html', context)


def publication_detail(request, id):
    library_detail = get_object_or_404(Publication, id=id)

    context = {
        'library_detail': library_detail,
        
    }
    return render(request, 'library_detail.html', context)


def opportunity_list(request):
    opportunity_list = Opportunity.objects.order_by('-timestamp')

    paginator = Paginator(opportunity_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {
        'queryset' : paginated_queryset,
        'page_request_var': page_request_var,

    }
    return render(request, 'project_list.html', context)

def opportunity_detail(request, id):
    project_detail = get_object_or_404(Opportunity, id=id)

    context = {
        'opportunity_detail': opportunity_detail,
        
    }
    return render(request, 'project_detail.html', context)
