from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    firtsname = models.CharField(max_length=50, verbose_name='Apellido paterno')
    secondname= models.CharField(max_length=50, verbose_name='Apellido materno')
    numberPhone = models.CharField(max_length=20,verbose_name='Número de teléfono')
    birthday = models.DateField(verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=100, verbose_name='Dirección')
    entry = models.DateField(verbose_name='Fecha de ingreso al trabajo')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name= 'Trabajador'
        verbose_name_plural= 'Trabajadores'

class LemonBoxes(models.Model):
        name = models.CharField(max_length=50, verbose_name='NOMBRE DEL TRABAJADOR')
        greenLemonMonday = models.CharField(max_length=20, verbose_name='Lunes cantidad de limón verde')
        stainedLemonMonday = models.CharField(max_length=20, verbose_name='Cantidad de limón manchado')
        greenLemonTuesday = models.CharField(max_length=20, verbose_name='Martes cantidad de limón verde')
        stainedLemonTuesday = models.CharField(max_length=20, verbose_name='Cantidad de limón manchado')
        greenLemonWednesday = models.CharField(max_length=20, verbose_name='Miércoles cantidad de limón verde')
        stainedLemonWednesday = models.CharField(max_length=20, verbose_name='Cantidad de limón manchado')
        greenLemonThursday = models.CharField(max_length=20, verbose_name='Jueves cantidad de limón verde')
        stainedLemonThursday = models.CharField(max_length=20, verbose_name='Cantidad de limón manchado')
        greenLemonFriday = models.CharField(max_length=20, verbose_name='Viernes cantidad de limón verde')
        stainedLemonFriday = models.CharField(max_length=20, verbose_name='Cantidad de limón manchado')
        greenLemonSaturday = models.CharField(max_length=20, verbose_name='Sábado cantidad de limón verde')
        stainedLemonSaturday = models.CharField(max_length=20, verbose_name='Cantidad de limón manchado')

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Entrega de carga'
            verbose_name_plural = 'Entrega de cajas'

class Tool(models.Model):
        use = models.CharField(max_length=100, verbose_name='Uso')
        brand = models.CharField(max_length=100, verbose_name='Marca')
        nameTool= models.CharField(max_length=100, verbose_name='Herramienta')

        def __str__(self):
            return self.use

        class Meta:
            verbose_name = 'Herramienta'
            verbose_name_plural = 'Herramientas'


class ChemicalProducts(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre del producto')
    brand = models.CharField(max_length=100, verbose_name='Marca')
    function = models.CharField(max_length=100, verbose_name='Función del producto químico')
    quantity = models.CharField(max_length=100, verbose_name='Cantidad por producto')
    components = models.CharField(max_length=100, verbose_name='Componentes')
    dateElaboration = models.CharField(max_length=100, verbose_name='Fecha de elaboraciónn')
    dateElaboration = models.CharField(max_length=100, verbose_name='Fecha de caducidad')

    def __str__(self):
        return self.brand 

    class Meta:
        verbose_name = 'Producto químico'
        verbose_name_plural = 'Productos químicos'

