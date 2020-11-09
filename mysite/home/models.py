from django.db import models
from django import forms
from django.db.models.fields import CharField

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
)
from wagtail.core.blocks import ListBlock, StreamBlock
from . import blocks
from modelcluster.fields import ParentalKey,ParentalManyToManyField
from wagtail.core.fields import RichTextField
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from mysite.models import InformationCorner,Partner,ContactInfo

class TopSlider(Orderable):
    page = ParentalKey("home.HomePage", related_name="top_slider_sec")
    title = models.CharField(max_length=30)
    paragraph = RichTextField(features=["bold", "italic"])
    button_label = models.CharField(max_length=30)
    background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    panels = [FieldPanel("title"),
              FieldPanel("paragraph"),
              FieldPanel("button_label"),
              ImageChooserPanel("background_image")
              ]


class HowSec(Orderable):
    page = ParentalKey("home.HomePage", related_name="how_it_works", null=True)
    title = models.CharField(max_length=30)
    description = RichTextField(features=["bold", "italic"])
    how_step = StreamField(
        [("h_s", blocks.HowStepBlock())], null=True, blank=False)
    panels = [FieldPanel("title"), FieldPanel("description"),
              StreamFieldPanel("how_step")]


class ClientsSec(Orderable):
    page = ParentalKey("home.HomePage", related_name="clients_sec", null=True)
    title = models.CharField(max_length=30)
    description = RichTextField(features=["bold", "italic"])
    client_icon = StreamField(
        [("client_icon", blocks.ClienticonBlock())], null=True, blank=False)

    panels = [FieldPanel("title"),
              FieldPanel("description"),
              StreamFieldPanel("client_icon")]


class HomePage(Page):
    max_count = 1
    template = "home/home_page.html"

    information_corner= ParentalManyToManyField(
        InformationCorner,
        blank=False
    )
    partner= ParentalManyToManyField(
        Partner,
        blank=False
    )
    contact_info= ParentalManyToManyField(
        ContactInfo,
        blank=False
    )


    how_section_title = CharField("How It Work Title", max_length=255, null=True, blank=False)
    how_section_description = RichTextField(features=["bold", "italic"], null=True)
    how_section_icon_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    # Try the following two options
    # how_section = StreamField([("how_works_section", ListBlock(blocks.HowStepBlock()))], null=True, blank=True)
    how_section = StreamField(StreamBlock([("how_works_section", blocks.HowSectBlock())], max_num=1), null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("top_slider_sec",min_num=1, label="Slider")],
            heading="Top Slider Section",
        ),
        MultiFieldPanel(
            [FieldPanel("how_section_title"), FieldPanel("how_section_description"), FieldPanel("how_section_icon_image"), StreamFieldPanel('how_section')],
            heading="How it Works Section 2",
        ),
        MultiFieldPanel(
            [InlinePanel("how_it_works", min_num=1,label="How it Works")],
            heading="How it Works Section",
        ),
        MultiFieldPanel(
            [InlinePanel("clients_sec",min_num=1, label="Clients")],
            heading="Clients Section",
        ),
        
        MultiFieldPanel(   
            [FieldPanel("information_corner", widget=forms.CheckboxSelectMultiple),
             FieldPanel("partner", widget=forms.CheckboxSelectMultiple),
             FieldPanel("contact_info", widget=forms.CheckboxSelectMultiple),
            
            ],heading="Header Configuration")        
        
 
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['top_sliders'] = TopSlider.objects.all()
        context['how_sec'] = HowSec.objects.all()
        context['clients'] = ClientsSec.objects.all()
        return context
