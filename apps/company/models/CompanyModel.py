from django.db import models
from apps.company.models import CompanySize, CompanyEstablishmentType, CompanyRegistrationStatus, CompanyPaymentStatus

class Company(models.Model):
    document = models.CharField(verbose_name='CPF/CNPJ', max_length=25, unique=True, null=False, blank=False)
    state_registration = models.CharField(verbose_name='I.E', max_length=25, unique=True, null=True, blank=True)
    corporate_name = models.CharField(verbose_name='Razão Social', max_length=255, null=False, blank=False)
    fantasy_name = models.CharField(verbose_name='Nome Fanstasia', max_length=255, null=False, blank=False)
    logo = models.CharField(verbose_name='Logo', max_length=10, null=True)
    banner = models.CharField(verbose_name='Banner', max_length=10, null=True)
    primary_color = models.CharField(verbose_name='Cor Primaria', max_length=15, null=True, blank=True, default='#FF5733')
    secondary_color = models.CharField(verbose_name='Cor Secundaria', max_length=15, null=True, blank=True, default='#32D31C')
    address = models.CharField(verbose_name='Endereço', max_length=255, null=True, blank=True)
    number = models.CharField(verbose_name='Número', max_length=10, null=True, blank=True)
    complement = models.CharField(verbose_name='Complemento', max_length=255, null=True, blank=True)
    public_observation = models.TextField(verbose_name='Observação Publica', null=True, blank=True)
    private_observation = models.TextField(verbose_name='Observação Privada', null=True, blank=True)
    company_size = models.ForeignKey(CompanySize, on_delete=models.RESTRICT, verbose_name='Porte', null=False, blank=False)
    establishment_type = models.ForeignKey(CompanyEstablishmentType, on_delete=models.RESTRICT, verbose_name='Tipo Estabelecimento', null=False, blank=False)
    payment_status = models.ForeignKey(CompanyPaymentStatus, on_delete=models.RESTRICT, verbose_name='Status Pagamento', null=False, blank=False)
    registration_status = models.ForeignKey(CompanyRegistrationStatus, on_delete=models.RESTRICT, verbose_name='Situação Cadastro', null=False, blank=False)

    def __str__(self) -> str:
        return f"{str(self.document)} - {str(self.corporate_name)}"
        
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"