from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
def button(request):
    return render(request, 'hello.html')

def output(request) :
	data requests.get("https://google.com")
	print(data.text)
	data = data.text
	return render(request, "hello.html", {'data':data})

def external(request):
	input_data = request.POST.get('param')
	out = run([sys.executable,'C:\\Gnanesh\\python\\git-projects\\space-invaders-pygame\\test.py', input_data], shell =False, stout = PIPE )
	print(out)
	
	return render(request, 'home.html', {'data1':out})
	
	
	