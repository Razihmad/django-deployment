from django.shortcuts import render
from myapp.models import AccessRecord,Topic,Webpage
# Create your views here.
def home(request):
    web = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':web}
    return render(request,'index.html',context=date_dict)

