from django.shortcuts import render
from Methods.common import Identificar_Usuario as IU
import os
# Create your views here.

def inicio(request):
    user = IU(request)
    print(os.environ.get('DJ_WEB_STATUS',''))
    return render(request,"index.html",{"user":user})