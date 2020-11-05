from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting




@register_snippet
class Partner(models.Model):
    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )
    link = models.URLField(blank=False, null=True)
    panels = [ImageChooserPanel("logo_image"),FieldPanel("link")]
    
    def __str__(self):
        return "partner's link: "+self.link
@register_snippet
class ContactInfo(models.Model):
    icon_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )
    contact_by = models.CharField(max_length=30)
    
    panels = [ImageChooserPanel("icon_image"),FieldPanel("contact_by")]
    
    def __str__(self):
        return "connected via: "+self.contact_by
    
    
    
@register_snippet
class InformationCorner(models.Model):
    title=models.CharField(max_length=30)
    panels =[FieldPanel("title")]
    
    def __str__(self):
        return self.title
        
@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL')
    twitter = models.URLField(
        help_text='Your Twitter page URL')
    instagram = models.URLField(
        help_text='Your Instagram username, without the @')
    google = models.URLField(
        help_text='Your Instagram google account')