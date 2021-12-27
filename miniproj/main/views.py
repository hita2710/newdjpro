from django.shortcuts import render,redirect
from  django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import UserDetails
from django.contrib import messages

from django.conf import settings
from pathlib import Path
from .forms import FileForm
from .models import FileDetails
from django.core.files.storage import FileSystemStorage

import pyaes, pbkdf2, binascii, os, secrets                         # pyaes implements the AES symmetric key encryption algorithm
                                                                    # pbkdf2 implements the PBKDF2 password-to-key derivation algorithm


global iv
global key
passw='hita2710'
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(passw, passwordSalt).read(32)
iv = secrets.randbits(256)
print('AES encryption key:', binascii.hexlify(key),end='\n')

def home(request):
    return render(request,"home.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['mailid']
        username = request.POST['username']
        password = request.POST['password']
        confpassword = request.POST['confpassword']

        if password == confpassword:
            if UserDetails.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken ")
                return redirect('register')
            elif UserDetails.objects.filter(mailid=email).exists():
                messages.error(request, "Mail ID is already taken ")
                return redirect('register')
            else:
                obj=UserDetails(first_name=first_name,last_name=last_name,mailid=email,username=username,password=password,confpassword=confpassword)
                obj.save()
                messages.success(request, "Succesfully Registered !!! Now login !!!" )
                return redirect('login')
        else:
            messages.error(request, "Entered passwords are not matching")
            return redirect('register')
    else:
        return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        global username
        username=request.POST['username']
        password=request.POST['password']

        #print(username,password)
        if UserDetails.objects.filter(username=username,password=password).exists():
            messages.success(request, "Logged in successfully" )
            return redirect('display')
        elif UserDetails.objects.filter(username=username).exists():
            messages.error(request, "Incorrect password")
            return redirect('login')
        else:
            messages.error(request, "User does not exist. Please register first !")
            return redirect('register')
    else:
        return render(request,"login.html")

def display(request):
    return render(request,"display.html")

def upload(request):
    context={}
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        uploaded_file = request.FILES['fileupl']
        n=uploaded_file.name
        txt=uploaded_file.read()
        encrypt(txt)
        #print(n)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        if form.is_valid():
            data = form.cleaned_data
            username= data['username']
            file_details=data['fileupl']
            #print(context['url'])
            context['url'] = "/main/" + uploaded_file.name
            obj=FileDetails(username=username,filename=uploaded_file.name,fileupl=context['url'])
            obj.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'upload.html', {
        'form': form
    })

def file_list(request):
    files = FileDetails.objects.filter(username=username)
    return render(request, 'file_list.html', {
        'files': files
    })

def logout(request):
    return render(request,"home.html")

def encrypt(plaintext):
    print(f'The read plaintext is {plaintext}',end='\n')
    pt=str(plaintext,'utf-8')
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(pt)
    print('Encrypted:', ciphertext,end='\n')
    print(ciphertext)
    decrypt(ciphertext)

def decrypt(ciphertext):
    print(f'The read ciphertext is {ciphertext}',end='\n')
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    decrypted = aes.decrypt(ciphertext)
    print('Decrypted:', decrypted,end='\n')
    