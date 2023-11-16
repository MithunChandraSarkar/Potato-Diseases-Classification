from django.shortcuts import render
from .forms import ImageUploadForm
from .models import PredictionResult

from .predict import predict_image



from .predict import predict_image



def predict_potato_disease(request):
    image = None
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            prediction = predict_image(image)
            result = PredictionResult.objects.create(result=prediction)
    else:
        form = ImageUploadForm()
        result = None

    return render(request, 'predict.html', {'form': form, 'result': result})
