from django.conf.urls import url

from . import views

urlpatterns = (
    # urls for Application
    url(r'^application/$', views.ApplicationListView.as_view(), name='app_application_list'),
    url(r'^application/create/$', views.ApplicationCreateView.as_view(), name='app_application_create'),
    url(r'^application/detail/(?P<slug>\S+)/$', views.ApplicationDetailView.as_view(),
        name='app_application_detail'),
    url(r'^application/update/(?P<slug>\S+)/$', views.ApplicationUpdateView.as_view(),
        name='app_application_update'),
)

urlpatterns += (
    # urls for Owner
    url(r'^owner/$', views.OwnerListView.as_view(), name='app_owner_list'),
    url(r'^owner/create/$', views.OwnerCreateView.as_view(), name='app_owner_create'),
    url(r'^owner/detail/(?P<slug>\S+)/$', views.OwnerDetailView.as_view(), name='app_owner_detail'),
    url(r'^owner/update/(?P<slug>\S+)/$', views.OwnerUpdateView.as_view(), name='app_owner_update'),
)

urlpatterns += (
    # urls for Questionnaire
    url(r'^questionnaire/$', views.QuestionnaireListView.as_view(), name='app_questionnaire_list'),
    url(r'^questionnaire/create/$', views.QuestionnaireCreateView.as_view(), name='app_questionnaire_create'),
    url(r'^questionnaire/detail/(?P<pk>\d+)/$', views.QuestionnaireDetailView.as_view(),
        name='app_questionnaire_detail'),
    url(r'^questionnaire/update/(?P<pk>\d+)/$', views.QuestionnaireUpdateView.as_view(),
        name='app_questionnaire_update'),
)

urlpatterns += (
    # urls for Tag
    url(r'^tag/$', views.TagListView.as_view(), name='app_tag_list'),
    url(r'^tag/create/$', views.TagCreateView.as_view(), name='app_tag_create'),
    url(r'^tag/detail/(?P<slug>\S+)/$', views.TagDetailView.as_view(), name='app_tag_detail'),
    url(r'^tag/update/(?P<slug>\S+)/$', views.TagUpdateView.as_view(), name='app_tag_update'),
)

urlpatterns += (
    # urls for Rule
    url(r'^rule/$', views.RuleListView.as_view(), name='app_rule_list'),
    url(r'^rule/create/$', views.RuleCreateView.as_view(), name='app_rule_create'),
    url(r'^rule/detail/(?P<pk>\d+)/$', views.RuleDetailView.as_view(), name='app_rule_detail'),
    url(r'^rule/update/(?P<pk>\d+)/$', views.RuleUpdateView.as_view(), name='app_rule_update'),
)

urlpatterns += (
    # urls for TagType
    url(r'^tagtype/$', views.TagTypeListView.as_view(), name='app_tagtype_list'),
    url(r'^tagtype/create/$', views.TagTypeCreateView.as_view(), name='app_tagtype_create'),
    url(r'^tagtype/detail/(?P<slug>\S+)/$', views.TagTypeDetailView.as_view(), name='app_tagtype_detail'),
    url(r'^tagtype/update/(?P<slug>\S+)/$', views.TagTypeUpdateView.as_view(), name='app_tagtype_update'),
)
