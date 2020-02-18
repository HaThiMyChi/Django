from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question



# Create your views here.

# request yêu cầu, response trả về

def index(request):
	# return HttpResponse("xin chao")
	myname = "nguyễn sơn"
	taisan1 = ["Điện thoại", "máy tính", " máy bay", "nhiều tiền"]
	
	context = {"name":myname, "taisan":taisan1}
	return render(request, "polls/index.html", context)

def viewlist(request):
	# list_question = Question.objects.all()
	# (truyen vao đối tượng question để nó biết lấy đối tượng object nào, pk là khóa chính)
	# get_object_or_404(Question, pk = 1 hoac question_test = 'ban an gi'...)
	# list_question = get_object_or_404(Question, pk = 1)
	
	list_question = Question.objects.all()
	context = {"dsquest": list_question}
	return render(request, "polls/question_list.html", context)

def  detailView(request, question_id):
	# khi tạo dữ liệu trong models thì nó sẽ tự động có trường id
	q = Question.objects.get(pk = question_id)
	return render(request, "polls/detail_question.html", {"qs": q })

def vote(request, question_id):
	q = Question.objects.get(pk = question_id)
	try:
		dulieu = request.POST["choice"]
		c = q.chooice_set.get(pk=dulieu)
	except:
		HttpResponse("Lỗi không có choice")
	c.vote = c.vote + 1
	c.save()
	# return HttpResponse(c.vote)
	return render(request, "polls/result.html", {"q": q})


def ham1(request):
	return HttpResponse("<h1>ham linh tinh</h1><p>xin chao</p>")