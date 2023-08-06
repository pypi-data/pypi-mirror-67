from django.urls import re_path

from ..views import (
    ProjectsView,
    ProjectExportXMLView,
    ProjectExportCSVView,
    ProjectImportXMLView,
    ProjectCreateView,
    ProjectDetailView,
    ProjectUpdateView,
    ProjectDeleteView,
    MembershipCreateView,
    MembershipUpdateView,
    MembershipDeleteView,
    SnapshotCreateView,
    SnapshotUpdateView,
    SnapshotRollbackView,
    ProjectAnswersView,
    ProjectAnswersExportView,
    ProjectViewView,
    ProjectViewExportView,
    ProjectQuestionsView,
    ProjectErrorView
)

urlpatterns = [
    re_path(r'^$', ProjectsView.as_view(), name='projects'),
    re_path(r'^(?P<pk>[0-9]+)/export/xml/$', ProjectExportXMLView.as_view(), name='project_export_xml'),
    re_path(r'^(?P<pk>[0-9]+)/export/(?P<format>[a-z]+)/$', ProjectExportCSVView.as_view(), name='project_export_csv'),
    re_path(r'^import/(?P<format>[a-z]+)/$', ProjectImportXMLView.as_view(), name='project_import'),
    re_path(r'^import/$', ProjectImportXMLView.as_view(), name='project_import'),

    re_path(r'^create/$', ProjectCreateView.as_view(), name='project_create'),
    re_path(r'^(?P<pk>[0-9]+)/$', ProjectDetailView.as_view(), name='project'),
    re_path(r'^(?P<pk>[0-9]+)/update/$', ProjectUpdateView.as_view(), name='project_update'),
    re_path(r'^(?P<pk>[0-9]+)/delete/$', ProjectDeleteView.as_view(), name='project_delete'),

    re_path(r'^(?P<project_id>[0-9]+)/memberships/create$', MembershipCreateView.as_view(), name='membership_create'),
    re_path(r'^(?P<project_id>[0-9]+)/memberships/(?P<pk>[0-9]+)/update/$', MembershipUpdateView.as_view(), name='membership_update'),
    re_path(r'^(?P<project_id>[0-9]+)/memberships/(?P<pk>[0-9]+)/delete/$', MembershipDeleteView.as_view(), name='membership_delete'),

    re_path(r'^(?P<project_id>[0-9]+)/snapshots/create/$', SnapshotCreateView.as_view(), name='snapshot_create'),
    re_path(r'^(?P<project_id>[0-9]+)/snapshots/(?P<pk>[0-9]+)/update/$', SnapshotUpdateView.as_view(), name='snapshot_update'),
    re_path(r'^(?P<project_id>[0-9]+)/snapshots/(?P<pk>[0-9]+)/rollback/$', SnapshotRollbackView.as_view(), name='snapshot_rollback'),

    re_path(r'^(?P<pk>[0-9]+)/answers/$', ProjectAnswersView.as_view(), name='project_answers'),
    re_path(r'^(?P<pk>[0-9]+)/answers/export/(?P<format>[a-z]+)/$', ProjectAnswersExportView.as_view(), name='project_answers_export'),

    re_path(r'^(?P<pk>[0-9]+)/snapshots/(?P<snapshot_id>[0-9]+)/answers/$', ProjectAnswersView.as_view(), name='project_answers'),
    re_path(r'^(?P<pk>[0-9]+)/snapshots/(?P<snapshot_id>[0-9]+)/answers/export/(?P<format>[a-z]+)/$', ProjectAnswersExportView.as_view(), name='project_answers_export'),

    re_path(r'^(?P<pk>[0-9]+)/views/(?P<view_id>[0-9]+)/$', ProjectViewView.as_view(), name='project_view'),
    re_path(r'^(?P<pk>[0-9]+)/views/(?P<view_id>[0-9]+)/export/(?P<format>[a-z]+)/$', ProjectViewExportView.as_view(), name='project_view_export'),

    re_path(r'^(?P<pk>[0-9]+)/snapshots/(?P<snapshot_id>[0-9]+)/views/(?P<view_id>[0-9]+)/$', ProjectViewView.as_view(), name='project_view'),
    re_path(r'^(?P<pk>[0-9]+)/snapshots/(?P<snapshot_id>[0-9]+)/views/(?P<view_id>[0-9]+)/export/(?P<format>[a-z]+)/$', ProjectViewExportView.as_view(), name='project_view_export'),

    re_path(r'^(?P<pk>[0-9]+)/questions/', ProjectQuestionsView.as_view(), name='project_questions'),
    re_path(r'^(?P<pk>[0-9]+)/error/', ProjectErrorView.as_view(), name='project_error'),
]
