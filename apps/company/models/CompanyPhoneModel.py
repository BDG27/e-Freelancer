from django.db import models
from apps.company.models import CompanyPhoneType, Company

class CompanyPhone(models.Model):
    phone_type = models.ForeignKey(CompanyPhoneType, on_delete=models.RESTRICT, verbose_name='Tipo de Telefone', null=False, blank=False)
    number = models.CharField(verbose_name='Número', max_length=20, null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa', null=False, blank=False)

    def __str__(self) -> str:
        return f"{str(self.phone_type.name)} - {str(self.number)} - {str(self.company)}"
        
    class Meta:
        verbose_name = "Empresa - Telefone"
        verbose_name_plural = "Empresa - Telefones"