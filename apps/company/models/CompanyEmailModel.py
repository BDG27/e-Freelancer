from django.db import models
from apps.company.models import Company

class CompanyEmail(models.Model):
    email = models.CharField(verbose_name='Email', max_length=255, null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa', null=False, blank=False)

    def __str__(self) -> str:
        return f"{str(self.email)} - {str(self.company)}"
        
    class Meta:
        verbose_name = "Empresa - Email"
        verbose_name_plural = "Empresa - Emails"