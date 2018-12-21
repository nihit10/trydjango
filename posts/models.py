from django.db import models
from django.urls import reverse #absolute url
from django.db.models.signals import pre_save
from django.utils.text import  slugify
from django.conf import settings


def upload_location(instance,filename):
	return"%s%s" %(instance.pk, filename)


class Post(models.Model):
	STATUS_CHOICES=(
		('draft','Draft'),
		('published','Published'),
	)
	title=models.CharField(max_length=50)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
	#slug=models.SlugField(unique=True, max_length=100)
	#image=models.FileField(null=True,blank=True)
	image=models.ImageField(upload_to=upload_location,null=True,blank=True,width_field="width_field",height_field="height_field")
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	content=models.TextField(max_length=200)
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	status=models.CharField(max_length=10, choices=STATUS_CHOICES,default='published')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posted:post_detail",kwargs={"pk":self.pk})
		#return "/posts/%s/" %(self.pk)


#def create_slug(instance, new_slug=None):
#	slug=slugify(intance.title)
#	if new_slug is not None:
#		slug=new_slug
#	qs=Post.objects.filter(slug=slug).order_by("-id")
#	exists=qs.exists()

#def pre_save_post_reciever(sender, instance, *args, **kwargs):
#	if not instance.slug:
#		instance.slug=create_slug(instance)

#pre_save.connect(pre_save_post_reciever, sender=Post)