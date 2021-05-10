from django.urls import path

from xray_detect import views as xray_view


urlpatterns = [
    #path('', animal_view.define_model, name='homepage'),
    path('', xray_view.predict_xray, name='predict_xray'),
    path('train/', xray_view.train_model, name='train_model'),
    path('image/', xray_view.create_image, name="create_image"),

    
]