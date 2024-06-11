from django.contrib import admin
from .models import Category, Customer, Product, Order

#NOW GO TO THE DJANGO ADMIN AND START ADDING CATEGORIES IN CATEGORIES AND
#PRODUCTS IN PRODUCTS
#https://www.youtube.com/watch?v=Cp7geK7xjyI AT 20:00
#CREATE A FOLDER OF IMAGES ON YOUR HARD DRIVE TO UPLOAD IMAGES FOR FAKE PRODUCTS
#WHEN YOU UPLOAD AN IMAGE, IT SHOULD CREATE A MEDIA FOLDER TO ECOMMERCE AND NEST IN
#THE MEDIA THEN PRODUCT FOLDERS
#https://www.youtube.com/watch?v=Cp7geK7xjyI AT 20
#To add categories, you have to go to Django Administration and add them
#Watch the above YouTube video at 23:11 to see how to do this under Store --> Categories
#Then add products under Products, including Price and Image
#Django automatically creates a Media directory (folder)

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)