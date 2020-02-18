from django.db import models

# Create your models here.

class Question(models.Model):
	question_test = models.CharField(max_length=200)
	time_pub = models.DateTimeField()
	
class Chooice(models.Model):
	# ForeignKey la khoa ngoai lien ket toi question ben tren
	# on_delete=models.CASCADE khi cau hoi dc xoa di thi cau tra loi cung xoa di
	# vote la diem so cua cau tra loi
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_test = models.CharField(max_length=100)
	vote = models.IntegerField(default=0)