from django.db import models


class County(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "counties"

    def __str__(self):
        return self.name


class ItemCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "itemcategories"

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = "items"

    def __str__(self):
        return self.name
