from django.contrib import admin
from .models import WelcomeWords, MissionVision, Slider, HeadingOne, HeadingTwo, HeadingThree, Intro, MidImage
from about.models import Ceo, AboutUs, Team, Media
from gallery.models import GallerySlider, Gallery, GalleryExtra
from service_products.models import  Preview, ServiceFive, ServiceSix, Sliding, Impression, ServiceOne, ServiceTwo, ServiceThree, Title, ServiceFour, ServiceFive, ServiceSix, TitleTwo, ServiceSeven
from publication.models import Publication
from opportunities.models import Opportunity
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Intro)
admin.site.register(Impression)
admin.site.register(WelcomeWords)
admin.site.register(MissionVision)
admin.site.register(Slider)
admin.site.register(HeadingOne)
admin.site.register(HeadingTwo)
admin.site.register(HeadingThree)
admin.site.register(MidImage)


admin.site.register(Ceo)
admin.site.register(AboutUs)
admin.site.register(Media)
admin.site.register(Team)

admin.site.register(GallerySlider)
admin.site.register(Gallery)
admin.site.register(GalleryExtra)

admin.site.register(Preview)
admin.site.register(Sliding)
admin.site.register(ServiceOne)
admin.site.register(ServiceTwo)
admin.site.register(ServiceThree)
admin.site.register(Title)
admin.site.register(ServiceFour)
admin.site.register(ServiceFive)
admin.site.register(ServiceSix)
admin.site.register(TitleTwo)
admin.site.register(ServiceSeven)




admin.site.register(Publication)
admin.site.register(Opportunity, MyModelAdmin)

