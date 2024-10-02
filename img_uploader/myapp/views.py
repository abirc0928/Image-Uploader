from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ImageForm
from .models import Image
# Create your views here.
def img_upload(request):
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(img_upload)  
    else:
        form = ImageForm()
    images = Image.objects.all()
    context = {
        'form': form,
        'images': images
    }
    return render(request, 'home.html', context)

def delete_image(request, id):

    image = Image.objects.get(pk=id)
    image.delete()
    return redirect(img_upload)