from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   
    url(r'^$', 'main.views.mainpage',name='main'),
    url(r'^send_message$', 'main.views.send_message',name='send_message'),
    url(r'^order$', 'main.views.add_order',name='order'),
    #url(r'^add_task/$','home.views.add_task',name='add_task'),
)
