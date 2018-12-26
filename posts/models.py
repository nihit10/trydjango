from django.db import models
from django.urls import reverse #absolute url
from django.db.models.signals import pre_save
from django.utils.text import  slugify
from django.conf import settings


def upload_location(instance,filename):
	return"%s%s" %(instance.pk, filename)


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
	objects=models.Manager() #Our default Manager
	published= PublishedManager() #our custom Model Manager

	STATUS_CHOICES=(
		('draft','Draft'),
		('published','Published'),
	)
	title=models.CharField(max_length=50)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
	#slug=models.SlugField(unique=True, max_length=100)
	#image=models.FileField(null=True,blank=True)
	image=models.ImageField(upload_to=upload_location,null=True,blank=True,)
	#height_field=models.IntegerField(default=550)
	#width_field=models.IntegerField(default=600)
	content=models.TextField(max_length=4000)
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	status=models.CharField(max_length=10, choices=STATUS_CHOICES,default='published')

	#class Meta: reverse ordering can also be done from here
	#	ordering=['-id']

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
