from django.db import models

class CompanyRegistrationStatus(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100, null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return f"{str(self.id)} - {str(self.name)}"
        
    class Meta:
        verbose_name = "Empresa - Situação Cadastro"
        verbose_name_plural = "Empresa - Situações Cadastro"