from django.shortcuts import render


def index_view(request):
    return render(request=request,
                  template_name='app/main/index.html')


def shop_view(request):
    return render(request=request,
                  template_name='app/inpage/product/shop.html')


def new_arrials(request):
    return render(request=request,
                  template_name='app/inpage/product/new_arrials.html')


def blog_view(request):
    return render(request=request,
                  template_name='app/inpage/blog/blogs.html')


def blog_details(request):
    return render(request=request,
                  template_name='app/inpage/blog/blog_details.html')


def product_single(request):
    return render(request=request,
                  template_name='app/inpage/product/product_single.html')


def contact(request):
    return render(request=request,
                  template_name='app/inpage/contact/contact1.html')



def about(request):
    return render(request=request,
                  template_name='app/inpage/about/about.html')
