from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class AboutMe(models.Model):
    shortDescription = models.CharField(max_length=300)
    image = models.ImageField(upload_to="myimages", default="me.png")
    mobile_image = models.ImageField(upload_to="myimagesMobile", default="me.png")
    tab_image = models.ImageField(upload_to="myimagesTablet", default="me.png")
    note = models.TextField(default="Mobile: 348X766, Tablet: 646X1200, Desktop: 890X1440")
    
    # richText = models.CharField(max_length=300)

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "All About Us"

    def __str__(self):
        return self.shortDescription


class PortFolioCategory(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    category = models.ForeignKey(
        PortFolioCategory, on_delete=models.SET_NULL, related_name="portfolios", null=True, blank=True)
    title = models.CharField(max_length=60)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to="projects")
    small_image = models.ImageField(upload_to="projectsSmall")
    shortdescription = models.TextField()
    
    details = RichTextUploadingField()
    # specifications = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"

    def __str__(self):
        return self.title


class Technologies(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="tags")
    name = models.CharField(max_length=100)
   
    

class Skills(models.Model):
    title = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)


class ServiceCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Services(models.Model):
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.SET_NULL, related_name="services", null=True, blank=True)
    title = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=300)
    # richText = models.CharField(max_length=300)
    # specifications = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Our Services"

    def __str__(self):
        return self.title


class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    review = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.name




class Articles(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to="projects")
    small_image = models.ImageField(upload_to="projectsSmall")
    shortdescription = models.TextField()
    details = RichTextUploadingField()
    # specifications = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title




class Tags(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name="tags")
    name = models.CharField(max_length=100)
   
    


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=600, null=True, blank=True)
    message = models.CharField(max_length=200, null=True, blank=True)
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"






class Seo(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to="seo")
    keywords = models.TextField()
    # specifications = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Seo"
        verbose_name_plural = "Seo"

    def __str__(self):
        return self.title
