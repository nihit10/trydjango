from django.db import models
from django.urls import reverse #absolute url


def upload_location(instance,filename):
	return"%s%s" %(instance.id, filename)


class Post(models.Model):
	title=models.CharField(max_length=50)
	#image=models.FileField(null=True,blank=True)
	image=models.ImageField(upload_to=upload_location,null=True,blank=True,width_field="width_field",height_field="height_field")
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	content=models.TextField(max_length=200)
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posted:post_detail",kwargs={"pk":self.pk})
		#return "/posts/%s/" %(self.pk)