from django.contrib import admin
from myapp.models import AccessRecord,Topic,Webpage

# Register your models 

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
