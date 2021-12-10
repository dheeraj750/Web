from django.shortcuts import  render
from polls.models import Contact

# Create your views here.


def index(request):
    return render(request,"home.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        con = Contact(name=name,email=email,phone=phone,content=content)
        con.save()
    return render(request, "contact.html")