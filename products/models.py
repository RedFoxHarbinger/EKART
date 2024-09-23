from django.db import models

# Create your models here.
class products(models.Model):
    class Meta:
         verbose_name_plural ="products"
    LIVE=0
    DELETE=1

        # Define the size choices
    SMALL = '12'
    MEDIUM = '14'
    LARGE = '15.6'

    SIZE_CHOICES = [
        (SMALL, 'Small (12 inch)'),
        (MEDIUM, 'Medium (14 inch)'),
        (LARGE, 'Large (15.6 inch)'),
    ]

    title=models.CharField(max_length=50)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    DELETE_CHOICES=((LIVE,'LIVE'),(DELETE,'DELETE'))
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    display_size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES,
        help_text="Select the laptop display size"
    )

    def __str__(self) -> str:
        return self.title
    

