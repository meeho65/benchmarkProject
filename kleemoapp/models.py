from django.db import models

class MobileProducts(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(null=False, max_length=60, default='')
    product_price = models.IntegerField(null=True, blank=True)
    product_chipset = models.CharField(max_length=60, default='')
    product_gpu = models.CharField(max_length=60, default='')
    product_ram_storage = models.CharField(max_length=60, default='')
    product_battery = models.CharField(max_length=20, default='')
    product_screen_size = models.CharField(max_length=10, default='')
    product_main_camera = models.CharField(max_length=30, default='')
    product_front_camera = models.CharField(max_length=30, default='')
    product_fast_charging = models.CharField(max_length=10, default='')
    product_sim_support = models.CharField(max_length=30, default='')
    product_description = models.CharField(max_length=300, default='')
    product_image = models.ImageField(upload_to="kleemoapp/images", default='')
    release_date = models.DateField()
    market_share = models.JSONField()

    def __str__(self):
        return self.product_name

class LaptopProducts(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=60, default='')
    product_price = models.IntegerField()
    product_processor = models.CharField(max_length=60, default='')
    product_gpu = models.CharField(max_length=60, default='')
    product_ram = models.CharField(max_length=60, default='')
    product_battery = models.CharField(max_length=30, default='')
    product_display = models.CharField(max_length=30, default='')
    product_storage = models.CharField(max_length=30, default='')
    product_description = models.CharField(max_length=300, default='')
    product_image = models.ImageField(upload_to="kleemoapp/images", default='')
    release_date = models.DateField()
    market_share = models.JSONField()

    def __str__(self):
        return self.product_name

class SmartWatchProducts(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=60, default='')
    product_price = models.IntegerField()
    product_water_resistant = models.CharField(max_length=60, default='')
    product_sensor = models.CharField(max_length=60, default='')
    product_charger_type = models.CharField(max_length=60, default='')
    product_battery_life = models.CharField(max_length=30, default='')
    product_display = models.CharField(max_length=30, default='')
    product_storage = models.CharField(max_length=30, default='')
    product_description = models.CharField(max_length=300, default='')
    product_image = models.ImageField(upload_to="kleemoapp/images", default='')
    release_date = models.DateField()
    market_share = models.JSONField()

    def __str__(self):
        return self.product_name

from django.db import models

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    product_type = models.CharField(max_length=20)  # Add a field to store the product type
    product_id = models.PositiveIntegerField()  # Add a field to store the product ID

    def __str__(self):
        return f"Review for {self.product_type} - {self.product_id}"
