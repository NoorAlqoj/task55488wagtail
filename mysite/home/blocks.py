from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock


class HowStepBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    description = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    icon_image = ImageChooserBlock(required=True)

    class Meta:  # noqa
        template = "home/how_step_block.html"
        icon = "edit"
        label = "Step"
        
class ClienticonBlock(blocks.StructBlock):
    icon_image = ImageChooserBlock(required=True)
    
    class Meta:  # noqa
        template = "home/client_icon_block.html"
        icon = "edit"
        label = "Icon"


class HowSectBlock(blocks.StructBlock):
    step = blocks.ListBlock(HowStepBlock)

    class Meta:  # noqa
        template = "home/how_step_block.html"
        icon = "edit"
        label = "Step"