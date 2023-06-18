from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.dispatch import receiver

# Create your models here.

### CRUD ###
# Create ( انشاء بيانات ) ## POST ### Response ( رسالة "تم انشاء المنتج بنجاح" )
# Read ( قراءة البيانات ) ## GET  ### Response ( Query ) الداتا المخزنة فى قاعدة البيانات
# Update ( تعديل البيانات ) ## PUT & POST  ### Response ( رسالة + المنتج بعد تعديله )
# Delete ( حذف البيانات ) ## DELETE ### Respone ( رسالة " تم مسح المنتج بنجاح" )

# Searchs
###################### Fields Option #######################
# blank = False = مطلوب = Required = *  بتاعت الفورم
# null = بتاعت الداتابيز = e7gzly mkan f el database
# editable = غير قابل للتعديل = لا يظهر فى الفورم
###################### Fields Option #######################


# Model Form

## Foreign Key  = واحد لكثير  class name + on_delete
## Many To Many = كثير لكثير  class name 
## One To One   = واحد لواحد  class name + on_delete

#TYPE_OF_PRODUCT = (
#   ("Save in Database","Show in Site")
# )

TYPE_OF_PRODUCT = (
    ("1","جهاز"),
    ("2","اكسسوار"),
    ("3","غير ذلك"),
)

class Product(models.Model):
    name = models.CharField(max_length=32,verbose_name="اسم المنتج")
    price = models.FloatField(blank=True,verbose_name="السعر",null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_create = models.DateField(blank=True,null=True)
    model_prod = models.CharField(max_length=30,verbose_name="الموديل",blank=True,null=True)
    image = models.ImageField(upload_to="product",verbose_name="صورة المنتج",blank=True,null=True)
    category = models.CharField(("المجموعة"), max_length=50,blank=True, null= True)
    actav = models.BooleanField(("الحالة"), blank=True,null=True)
    active = models.BooleanField(("نشيط ؟"),default=True)
    count = models.IntegerField(("الكمية"))
    magmo3a = models.ForeignKey('Elmagmo3a',verbose_name="المجموعة",on_delete=models.CASCADE,blank=True,null=True)
    tag = models.ManyToManyField('Tag',verbose_name="Tag",blank=True)
    type_product = models.CharField(max_length=320,choices=TYPE_OF_PRODUCT,blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    
    ### slug = unique = small = no spaces = no % no $ no @ = required
    
    #magmo3a = models.ForeignKey('app.Elmagmo3a')
    #magmo3a = models.ForeignKey(Elmagmo3a)
    #### اول حاجة فى foreign key لازم تكون اسم الكلاس
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product,self).save(*args,**kwargs)
    
    class Meta:
        verbose_name = ("المنتج")
        verbose_name_plural = ("المنتجات")
    
    def __str__(self):
        return self.name

class Elmagmo3a(models.Model):
    name = models.CharField(("الاسم"), max_length=50)
    type_magmo3a = models.CharField(max_length=32,blank=True,null=True)
    descrebtion = models.TextField(blank=True,null=True,default='',max_length=1000)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("المجموعة")
        verbose_name_plural = ("المجموعات")
        
class Tag(models.Model):
    name = models.CharField(("الاسم"), max_length=50)
    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.SET_NULL)
    mobile_number = models.CharField(("رقم التليفون"), max_length=12)
    
    class Meta:
        verbose_name = ("البروفايل")
        verbose_name_plural = ("بروفايلات المستخدمين")
    def __str__(self):
        return self.user.username
    
## post_save = بعد الحفظ
## pre_save = قبل الحفظ
    
## sender الكلاس اللى بيبعت الاشارة
## post_save بعد الحفظ تتنفذ الفانكشن
## pre_save قبل الحفظ مباشرة تنفذ الفانكشن
## يفضل عمل try و except فى الفانكشن لتجنب اى error

@receiver(post_save,sender=User)
def create_profile(instance,created,**kwargs):
    try:
        if created:
            Profile.objects.create(
                user = instance
            )
            print("تم انشاء البروفايل")
    except:
        print("Error In Create Profile")
        pass