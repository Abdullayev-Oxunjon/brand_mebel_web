from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from app.form.other import ContactModelForm
from app.models import Product, Category, Blog, AboutBanner, SocialLinks, Team


def index_view(request):
    products = Product.objects.all()[:8]
    categories = Category.objects.all()
    latest_blogs = Blog.objects.order_by("created_at").all()[:3]
    return render(request=request,
                  template_name='app/main/index.html',
                  context={"products": products,
                           "categories": categories,
                           "latest_blogs": latest_blogs})


def shop_view(request):
    products = Product.objects.all()
    paginator = Paginator(object_list=products,
                          per_page=12)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(number=page_number)
    return render(request=request,
                  template_name='app/inpage/product/shop.html',
                  context={"products": product_list})


def new_arrials(request):
    products = Product.objects.all()
    return render(request=request,
                  template_name='app/inpage/product/new_arrials.html',
                  context={"products": products})


def blog_view(request):
    blogs = Blog.objects.all()
    paginator = Paginator(object_list=blogs,
                          per_page=9)
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(number=page_number)
    return render(request=request,
                  template_name='app/inpage/blog/blogs.html',
                  context={"blogs": blog_list})


def blog_details(request, blog_id):
    recent_blogs = Blog.objects.order_by("created_at").all()[:4]
    blog = Blog.objects.filter(id=blog_id).first()
    return render(request=request,
                  template_name='app/inpage/blog/blog_details.html',
                  context={"blog": blog,
                           "recent_blogs": recent_blogs})


def product_single(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    products = Product.objects.all()

    return render(request=request,
                  template_name='app/inpage/product/product_single.html',
                  context={"product": product,
                           'products': products})


def contact(request):
    if request.method == "POST":
        form = ContactModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
    form = ContactModelForm()

    return render(request=request,
                  template_name='app/inpage/contact/contact1.html',
                  context={"form": form})


def about(request):
    banners = AboutBanner.objects.all()
    social_links = SocialLinks.objects.all()
    teams = Team.objects.all()
    return render(request=request,
                  template_name='app/inpage/about/about.html',
                  context={"banners": banners,
                           "social_links": social_links,
                           "teams": teams})


def my_account(request):
    return render(request=request,
                  template_name='app/inpage/auth/my_account.html')


def home_2(request):
    return render(request=request,
                  template_name='app/main/home_2.html')


def checkout(request):
    return render(request=request,
                  template_name='app/inpage/product/checkout.html')

# def update_image(request, pk):
#     if request.method == 'POST':
#         my_model = Blog.objects.get(pk=pk)
#         new_image = request.FILES.get('new_image')
#
#         if new_image:
#             # Delete the old image from storage
#             if my_model.image:
#                 default_storage.delete(my_model.image.path)
#
#             # Generate a unique name for the new image file
#             new_image_name = f"blog_{my_model.pk}_{new_image.name}"
#
#             # Save the new image to the media directory and update the model field
#             my_model.image.save(new_image_name, new_image)
#             my_model.save()
#
#         return redirect('blog-details', pk=pk)
