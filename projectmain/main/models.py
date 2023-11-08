from django.db import models


class MainCarousel(models.Model) : 
    id = models.AutoField
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="main/images", default="")

    def __str__(self):
        return self.title

class OfferCarousel(models.Model) : 
    id = models.AutoField
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="main/images", default="")

    def __str__(self):
        return self.title


class Categories(models.Model) : 
    id = models.AutoField
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to="main/images", default="")

    def __str__(self):
        return self.name


class Captions(models.Model) :
    caption_id = models.AutoField
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to="main/images", default="")

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField
    code = models.CharField(max_length=20, default="")
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.name + ' (' + self.category + ')'
    

class Dynamic_Product(models.Model) :
    id = models.AutoField
    code = models.CharField(max_length=20, default="")
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    caption = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.name + ' (' + self.caption + ')'

    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
    

    
class Cont_info(models.Model):
    id = models.AutoField
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=1000)
    email = models.CharField(max_length=50)
    page = models.CharField(max_length=50)
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.phone


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    amount = models.IntegerField(default=0)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

    def __str__(self):
        return self.name



class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    # timestamp= models.DateField(auto_now_add= True)
    timestamp= models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return "ID: {}, Name: {}, Status: {}".format(self.order_id, Order.objects.filter(order_id=self.order_id).values_list('name', flat=True).first(), self.update_desc)

        # Orders.objects.filter(order_id=self.order_id).values_list('name', flat=True).first() 
        # The line above is not a must. It's just for a practice... 
        # To find specific value from a model's attribute: 
        # ModelName.objects.filter(PrimaryKey=UniqueValue).values_list('attribute', flat=True).first()