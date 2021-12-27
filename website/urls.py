from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from news_media.views import index, blog, post, about, gallery, search, post_create, post_update, post_delete, opportunity_list, opportunity_detail, service_products, publication, publication_detail



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('post/<id>/', post, name='post-detail'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('tinymce/', include('tinymce.urls')),

    path('opportunity_list/', opportunity_list, name='opportunity_list'),
    path('opportunity_detail/<id>/', opportunity_detail, name='opportunity-detail'),
    path('service_products/', service_products, name='services'),
    path('publication/', publication, name='publication'),
    path('publication_detail/<id>/', publication_detail, name='publication-detail'),




 



#    path('madrassah/', madrassah),
 #   path('library/', library),
  #  path('library_detail/<id>/', library_detail, name='library-detail'),
   # path('project_list/', project_list),
    #path('project_detail/<id>/', project_detail, name='project-detail'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "MBD Holdings AdminPanel"
admin.site.site_title = "MBD Holdings App Admin"
admin.site.site_index_title = "Welcome To MBD Holdings Admin Panel"

