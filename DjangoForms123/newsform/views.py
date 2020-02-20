from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostFormLogin


# Create your views here.

# cách viet nay la function
# def index(request):
# 	return HttpResponse("xin chao")
#

# cach viet nay la class view
class IndexClass(View):
	def get(self, request):
		ketqua = "1234567777"
		return HttpResponse(ketqua)
		
	
# cách viet nay la function
# def add_post(request):
# 	# return HttpResponse("them bai viet o day")
# 	a = PostForm()
# 	return render(request, 'news/add_news.html', {'f': a})
#

# cach viet nay la class view
class PostClass(View):
	def get(self, request):
		# return HttpResponse("them bai viet o day")
		a = PostForm()
		return render(request, 'news/add_news.html', {'f': a})
#


# def save_news(request):
# 	if request.method=="POST":
# 		q = PostForm(request.POST)
# 		if q.is_valid():
# 			q.save()
# 			return HttpResponse('luu ok')
# 		else:
# 			return HttpResponse('Khong duoc validate')
# 	else:
# 		return HttpResponse('khong phai post request')


class ClassSaveNew(View):
	# def get(self, request):
	# 	pass
	
	def get(self, request):
		# return HttpResponse("them bai viet o day")
		a = PostForm()
		return render(request, 'news/add_news.html', {'f': a})
	
	def post(self, request):
		q = PostForm(request.POST)
		if q.is_valid():
			q.save()
			return HttpResponse('luu ok')
		else:
			return HttpResponse('Khong duoc validate')
	
	def put(self, request):
		pass
	
	
def email_view(request):
	b = SendEmail()
	return render(request, 'news/email.html', {'f':b})

def process(request):
	if request.method=="POST":
		m = SendEmail(request.POST)
		if m.is_valid():
			# tieude = m.cleaned_data['title']
			# email = m.cleaned_data['email']
			# noidung = m.cleaned_data['content']
			# cc = m.cleaned_data['cc']
			# context = {'td':tieude, 'c':cc, 'b':noidung, 'd':email}
			context2 = {'email_data': m}
			# return render(request, 'news/print_email.html', context)
			return render(request, 'news/print_email.html', context2)
		else:
			return HttpResponse('form not validate')
	else:
		return HttpResponse('khong phai POST method')
			
	
class LoginClassIndex(View):
	def get(self, request):
		return HttpResponse('<h1>Xin chao</h1>')
	
class LoginClass(View):
	def get(self, request):
		return render(request, 'news/login.html')
	
	def post(self, request):
		user_name = request.POST.get('tendangnhap')
		matkhau = request.POST.get('password')
		my_user = authenticate(username=user_name, password=matkhau)
		if my_user is None:
			return HttpResponse('Dang nhap that bai, User khong ton tai')
		
		login(request, my_user)
		
		# return HttpResponse('ban vua bam dang nhap %s %s' %(user_name, matkhau))
		return render(request, 'news/thanhcong.html')
	
class ViewUser(LoginRequiredMixin, View):
	login_url = '/newsform/login/'
	def get(self, request):
		# if not request.user.is_authenticated:
		# 	return HttpResponse('ban vui long dang nhap')
		# else:
		# 	return HttpResponse('<h1>day la view user</h1>' )
		
		return HttpResponse('<h1>day la view user</h1>')
		
	def post(self, request):
		pass

@decorators.login_required(login_url ='/newsform/login/')
def view_product(request):
	return HttpResponse('Xem san pham')

class AddPost(LoginRequiredMixin, View):
	login_url = '/newsform/login/'
	def get(self, request):
		f = PostFormLogin()
		context = {'fm': f}
		return render(request, 'news/add_post.html', context)
	
	def post(self, request):
		f = PostFormLogin(request.POST)
		if not f.is_valid():
			return HttpResponse('Ban nhap sai du lieu roi')
		#cache reload tu database user
		print(request.user.get_all_permissions())
		
		if request.user.has_perm('newsform.add_post'): # viet thuong ten model
			f.save()
		else:
			return HttpResponse('may khong co quyen')
		return HttpResponse('Oke')