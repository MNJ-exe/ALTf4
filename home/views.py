from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from home.models import Content
from reviews.models import Review
from django.db.models import Avg

def home_view(request):
    home = Content.objects.filter(category='home')
    return render(request, 'home.html', {'contents': home, 'page': 'home'})

def movies_view(request):
    movies = Content.objects.filter(category='movie')
    return render(request, 'movies.html', {'contents': movies, 'page': 'movies'})

def tvshows_view(request):
    tvshows = Content.objects.filter(category='tvshow')
    return render(request, 'tvshows.html', {'contents': tvshows, 'page': 'tvshows'})

def documentaries_view(request):
    documentaries = Content.objects.filter(category='documentary')
    return render(request, 'documentaries.html', {'contents': documentaries, 'page': 'documentaries'})

def logout_view(request):
    logout(request)
    return redirect('login')

def content_detail(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    reviews = content.reviews.select_related('user').all().order_by('-created_at')
    avg_rating = reviews.aggregate(average=Avg('rating'))['average'] or 0

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')
        review_text = request.POST.get('review_text')
        rating_str = request.POST.get('rating', '0')
        try:
            rating = int(rating_str)
        except ValueError:
            rating = 0
        Review.objects.create(content=content, user=request.user, review_text=review_text, rating=rating)
        return redirect('content_detail', content_id=content_id)

    # you can pass category if you want extra display logic in the template
    return render(request, 'reviews/review.html', {
        'content': content,
        'reviews': reviews,
        'avg_rating': avg_rating,
    })
