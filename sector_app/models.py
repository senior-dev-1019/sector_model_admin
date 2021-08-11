from django.db import models

# Create your models here.

class Sector(models.Model):
    sector_name = models.CharField(max_length=64)

def _str_(self):
    return f"{self.sector_name}"

class Organization(models.Model):
    org_sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='org_sector')
    org_name = models.CharField(max_length=64)
    legal_name = models.CharField(max_length=64)
    alt_name1 = models.CharField(max_length=64)
    alt_name2 = models.CharField(max_length=64)
    alt_name3 = models.CharField(max_length=64)
    Ticker = models.CharField(max_length=10)  
   
def _str_(self):
    return f"{self.org_name}"

class Debt_Class(models.Model):
    class_name = models.CharField(max_length=64)

def _str_(self):
    return f"{self.class_name}"

class Debts(models.Model):
    debt_org = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='debt_org')
    debt_name = models.CharField(max_length=64)
    maturity_date = models.DateField()
    debt_amount = models.IntegerField()
    debt_class = models.ForeignKey(Debt_Class, on_delete=models.CASCADE, related_name='debt_class')

def _str_(self):
    return f"{self.debt_name}"

class Rating_Entity(models.Model):
    entity_name = models.CharField(max_length=64)

def _str_(self):
    return f"{self.entity_name}"

class Rating_Scale(models.Model):
    scale_name = models.CharField(max_length=64)

def _str_(self):
    return f"{self.scale_name}"

class Rating_Value(models.Model):
    scale = models.ForeignKey(Rating_Scale, on_delete=models.CASCADE, related_name='scale') 
    value_name = models.CharField(max_length=64)

def _str_(self):
    return f"{self.value_name}"

class Rating_Outlook(models.Model):
    outlook_entity = models.ForeignKey(Rating_Entity, on_delete=models.CASCADE, related_name='outlook_entity') 
    outlook_name = models.CharField(max_length=64)

def _str_(self):
    return f"{self.outlook_name}"

class Rating_Watch(models.Model):
    watch_entity = models.ForeignKey(Rating_Entity, on_delete=models.CASCADE, related_name='watch_entity') 
    watch_name = models.CharField(max_length=64)

def _str_(self):
    return f"{self.outlook_name}"

class Ratings(models.Model):
    rating_debt = models.ForeignKey(Debts, on_delete=models.CASCADE, related_name='rating_debt')
    rating_entity = models.ForeignKey(Rating_Entity, on_delete=models.CASCADE, related_name='rating_entity')
    rating_scale = models.ForeignKey(Rating_Scale, on_delete=models.CASCADE, related_name='rating_scale')
    rating_assigned = models.ForeignKey(Rating_Value, on_delete=models.CASCADE, related_name='rating_assigned')
    rating_outlook = models.ForeignKey(Rating_Outlook, on_delete=models.CASCADE, related_name='rating_outlook')
    rating_watch = models.ForeignKey(Rating_Watch, on_delete=models.CASCADE, related_name='rating_watch')
    rating_date = models.DateField()