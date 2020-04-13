from django.shortcuts import render

# Create your views here.
from .models import Component
from .forms import ComponentForm, RawComponentForm

# def component_create(request):
#     iForm = RawComponentForm()
#     if request.method == "POST":
#         iForm = RawComponentForm(request.POST)
#         if iForm.is_valid():
#             print(iForm.cleaned_data)
#             Component.objects.create(**iForm.cleaned_data)
#         else:
#             print(iForm._errors)
#     iContext = {
#         "iForm": iForm
#     }
#     return render(request, 'components/comp_create.html', iContext)

# def component_create(request):
#     # print(request.GET)
#     # print(request.POST)
#     iTitle = request.POST.get('title')
#     print(iTitle)
#     # Component.objects.create(CompName=iTitle)
#     iContext = {}

#     return render(request, 'components/comp_create.html', iContext)

def component_create(request):
    iForm = ComponentForm(request.POST or None)
    if iForm.is_valid():
        iForm.save()
        iForm = ComponentForm()

    iContext = {
        'iForm':iForm
    }

    return render(request, 'components/comp_create.html', iContext)

def component_view(request, *args, **kwargs):
    print("request=",request)
    print("args=",args)
    print("kwargs=",kwargs)
    iComp = {
        'iComp': Component.objects.get(id=1)
    }
    return render(request, 'components/component.html', iComp)

def dynamic_lookup_view(request, aId):
    iObj = Component.objects.get(id=aId)

    iContext = {
        'Object': iObj
    }

    return render(request, 'components/dynamiclookup.html', iContext)
