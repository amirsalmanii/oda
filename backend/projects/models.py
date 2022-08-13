from django.db import models


class Project(models.Model):
    title_image = models.ImageField(upload_to="projects/", null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    year = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    project_owner = models.CharField(max_length=200, null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)

    meterial_a_image = models.ImageField(upload_to="meterials/", null=True, blank=True)
    meterial_a_title = models.CharField(max_length=200, null=True, blank=True)
    meterial_a_description = models.TextField(null=True, blank=True)

    meterial_b_image = models.ImageField(upload_to="meterials/", null=True, blank=True)
    meterial_b_title = models.CharField(max_length=200, null=True, blank=True)
    meterial_b_description = models.TextField(null=True, blank=True)

    meterial_c_image = models.ImageField(upload_to="meterials/", null=True, blank=True)
    meterial_c_title = models.CharField(max_length=200, null=True, blank=True)
    meterial_c_description = models.TextField(null=True, blank=True)

    image1 = models.ImageField(upload_to="gallery/", null=True, blank=True)
    image2 = models.ImageField(upload_to="gallery/", null=True, blank=True)
    image3 = models.ImageField(upload_to="gallery/", null=True, blank=True)
    image4 = models.ImageField(upload_to="gallery/", null=True, blank=True)
    image5 = models.ImageField(upload_to="gallery/", null=True, blank=True)
    image6 = models.ImageField(upload_to="gallery/", null=True, blank=True)
    image7 = models.ImageField(upload_to="gallery/", null=True, blank=True)
    image8 = models.ImageField(upload_to="gallery/", null=True, blank=True)
    image9 = models.ImageField(upload_to="gallery/", null=True, blank=True)
    image10 = models.ImageField(upload_to="gallery/", null=True, blank=True)
    image11 = models.ImageField(upload_to="gallery/", null=True, blank=True)
    image12 = models.ImageField(upload_to="gallery/", null=True, blank=True)

    class Meta:
        ordering = ('-id',) 

    def __str__(self):
        return self.title