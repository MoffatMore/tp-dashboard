import re

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator
from edc_base.view_mixins import EdcBaseViewMixin
# from edc_constants.constants import ABNORMAL
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin

from ....model_wrappers import EnrollmentLossModelWrapper


class ListBoardView(NavbarViewMixin, EdcBaseViewMixin,
                    SearchFormViewMixin, ListboardView):

    listboard_template = 'enrollment_listboard_template'
    listboard_url = 'enrollment_listboard_url'
    listboard_panel_style = 'info'
    listboard_fa_icon = "fa-user-times"

    model = 'tp_screening.enrollmentloss'
    model_wrapper_cls = EnrollmentLossModelWrapper
    navbar_name = 'tp_dashboard'
    navbar_selected_item = 'screened_subject'
    search_form_url = 'enrollment_listboard_url'

#     def get_queryset_filter_options(self, request, *args, **kwargs):
#         options = super().get_queryset_filter_options(request, *args, **kwargs)
#         if kwargs.get('screening_identifier'):
#             options.update(
#                 {'screening_identifier': kwargs.get('screening_identifier')})
#         return options
# 
#     def extra_search_options(self, search_term):
#         q = Q()
#         if re.match('^[A-Z]+$', search_term):
#             q = Q(first_name__exact=search_term)
#         return q
