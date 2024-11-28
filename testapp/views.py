from django.shortcuts import render
from testapp.forms import ItemAddForm



def ItemAddForm_view(request):
    return render (request, 'testapp/home.html')

def AddItem_view(request):
    form=ItemAddForm()
    response= render(request, 'testapp/additem.html',{'form':form})
    if request.method== 'POST':
        form= ItemAddForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['itemname']
            quanity=form.cleaned_data['itemQuantity']
            response.set_cookie(name, quanity, 60)
    return response
def displayItem_view(request):
    return render (request,'testapp/showItem.html')
    
        
        