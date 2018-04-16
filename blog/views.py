from django.shortcuts import render

# Create your views here.
def home_page(request):
	if request.method == 'POST' : 
		comment = request.POST.get('conmment')
		user = request.POST.get("username")

		print(comment * 10)
		return render(request, 'blog/home_page.html', {'comment': comment, 'username': user})

	return render(request, 'blog/home_page.html')
	