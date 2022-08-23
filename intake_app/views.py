from django.shortcuts import render, redirect
from .models import Application
def index(request):
    return render(request, 'pages/index.html')

def intake(request):
    print(request.POST)
    if request.method == 'GET':
        return render(request, 'pages/intake.html')
    elif request.method == 'POST':
        groom = request.POST.get('groom','') == "True"
        cat = request.POST.get('cat','') == "True"
        walk = request.POST.get('walk','') == "True"
        visit = request.POST.get('visit','') == "True"
        overnight = request.POST.get('overnight','') == "True"
        jewelry = request.POST.get('jewelry','') == "True"
        yard_cleaning = request.POST.get('yard_cleaning','') == "True"
        house_cleaning = request.POST.get('house_cleaning','') == "True"
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone_number = request.POST['pnumber']
        address = request.POST['address']
        pet_type = request.POST['pet_type']
        pet_name = request.POST['pet_name']
        breed = request.POST['breed']
        vet_name = request.POST['vet_name']
        apps = Application.objects.create(groom=groom, cat=cat, walk=walk, visit=visit, overnight=overnight, jewelry=jewelry, yard_cleaning=yard_cleaning, house_cleaning=house_cleaning, fname=fname, lname=lname,
        email=email, phone_number=phone_number, address=address, pet_type=pet_type, pet_name=pet_name, breed=breed, vet_name=vet_name)
        apps.save()
        return render(request, "pages/index.html", {'apps': apps})
    
def delete(request):
    #Removes client from intake forms list --> delete button
    id = request.POST['id']
    item = Application.objects.get(id = id)
    item.delete()
    return redirect('natadash')

def delete_client(request):
    #Removes client from intake forms list --> Accept Button 
    id = request.POST['id']
    item = Application.objects.get(id = id)
    item.delete()
    return redirect('clients')
    

def natadash(request):
    #Gathers items for Natadash page (list of intake forms)
    Items = Application.objects.all()
    return render(request, 'pages/natalieDash.html', {'Items': Items})


def clients(request):
    #Gathers items for List of Current Clients
    Items = Application.objects.all()
    return render(request, "pages/clients.html", {'Items': Items})

def accept(request):
    #Updates "accepted" field in table and adds client to List of Current Clients
    id = request.POST['id']
    item = Application.objects.get(id = id)
    item.accepted = True
    item.save()
    return redirect('natadash')

def client(request, id):
    #Gathers items for individual Client Profile
    item = Application.objects.get(id = id)
    return render(request, "pages/profile.html", {'Item': item})

    

