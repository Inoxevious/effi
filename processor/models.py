from django.db import models
# Create your models here.


class Ministry(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=70)
    office_contact = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=70)
    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    responsible_ministry = models.ForeignKey(Ministry, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Business(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    intro = models.TextField()
    production_capacity_technology_process = models.TextField()
    image = models.ImageField(upload_to='Farm/static/processor')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Business'
        verbose_name_plural = 'Businesses'

class CapitalInvestmentRequirementsItem(models.Model):
    name = models.CharField(max_length=70)
    units = models.CharField(max_length=70)
    qty = models.FloatField()
    at = models.FloatField()
    
    def __str__(self):
        return self.name

class CapitalInvestmentRequirements(models.Model):
    Business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.ManyToManyField(CapitalInvestmentRequirementsItem)
    
    def __str__(self):
        return self.Business.name

class GeneralCostsItem(models.Model):
    name = models.CharField(max_length=70)
    production_cost_month = models.FloatField()

    def __str__(self):
        return self.name



class GeneralCosts(models.Model):
    Business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.ManyToManyField(GeneralCostsItem)
    
    def __str__(self):
        return self.Business.name

class DirectCostsItem(models.Model):
    name = models.CharField(max_length=70)
    units = models.CharField(max_length=70,null=True ,blank=True)
    at = models.FloatField()
    qty = models.FloatField()
    month_days = models.IntegerField()
    production_cost_month = models.FloatField(null=True ,blank=True)
    def __str__(self):
        return self.name

class DirectCosts(models.Model):
    Business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.ManyToManyField(DirectCostsItem)

    def __str__(self):
        return self.Business.name
  


class ProductionOperatingCosts(models.Model):
    Business = models.ForeignKey(Business, on_delete=models.CASCADE)
    direct_overheads = models.ForeignKey(DirectCosts, on_delete=models.CASCADE)
    general_costs_overheads = models.ForeignKey(GeneralCosts, on_delete=models.CASCADE)
    notes = models.TextField()
    def __str__(self):
        return self.Business.name

class ProjectProductCostPriceStructureItem(models.Model):
    name = models.CharField(max_length=70)
    at = models.FloatField(null=True ,blank=True)
    qty_day = models.FloatField(null=True ,blank=True)
    production_cost_day = models.FloatField(null=True ,blank=True)
    unit_price = models.FloatField(null=True ,blank=True)
    period = models.IntegerField(null=True ,blank=True)
    output = models.FloatField(null=True ,blank=True)
    unit_cost = models.FloatField(null=True ,blank=True)
    month_days = models.IntegerField(null=True ,blank=True)

    def __str__(self):
        return self.name

class ProjectProductCostPriceStructure(models.Model):
    Business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.ManyToManyField(ProjectProductCostPriceStructureItem)
    
    
    def __str__(self):
        return self.Business.name
      
class MarketAnalysis(models.Model):
    Business = models.ForeignKey(Business, on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return self.Business.name

class Risk(models.Model):
    Business = models.ForeignKey(Business, on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return self.Business.name

class GovernmentFacilitiesIncentives(models.Model):
    Business = models.ForeignKey(Business, on_delete=models.CASCADE)
    item = models.TextField()
    def __str__(self):
        return self.Business.name

class SourceEquipmentMaterials(models.Model):
    Business = models.ForeignKey(Business, on_delete=models.CASCADE)
    company = models.CharField(max_length=270)
    def __str__(self):
        return self.Business.name



