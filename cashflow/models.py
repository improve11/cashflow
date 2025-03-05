from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('name', 'type')
    
    def __str__(self):
        return f"{self.name} ({self.type})"

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('name', 'category')
    
    def __str__(self):
        return f"{self.name} ({self.category})"

class Transaction(models.Model):
    date = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.date} - {self.amount}"