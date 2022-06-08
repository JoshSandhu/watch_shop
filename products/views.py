from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Product
from .forms import ReviewForm


# Create your views here.

class ProductList(generic.ListView):
    model = Product
    queryset = Product.objects.filter(status=1).order_by('-created_on')
    template_name = 'products.html'
    paginate_by = 6
    
class ProductDetail(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Product.objects.filter(status=1)
        product = get_object_or_404(queryset, slug=slug)
        reviews = product.reviews.filter(approved=True).order_by('created_on')
        liked = False
        if product.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "product_detail.html",
            {
                "product": product,
                "reviews": reviews,
                "reviewed": False,
                "liked": liked,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Product.objects.filter(status=1)
        product = get_object_or_404(queryset, slug=slug)
        reviews = product.reviews.filter(approved=True).order_by('created_on')
        liked = False
        if product.likes.filter(id=self.request.user.id).exists():
            liked = True

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.post = post 
            review.save()

        else:
            review_form = ReviewForm()

        return render(
            request,
            "product_detail.html",
            {
                "product": product,
                "reviews": reviews,
                "reviewed": True,
                "liked": liked,
                "review_form": ReviewForm()
            },
        )