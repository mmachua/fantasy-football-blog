from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name='category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_re_path(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

def __str__(self):
    return self.user.bizname

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=False)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=False)

    descriptiontitle =models.CharField(blank=True, max_length=70)

    description =models.TextField(blank=True, max_length=1150)

    descriptiontitle2 =models.CharField(blank=True,max_length=80)

    description2 =models.TextField(blank=True)

    link = models.URLField(max_length=350, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    stock = models.PositiveIntegerField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
        
    def get_absolute_re_path(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
    

