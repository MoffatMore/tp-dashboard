from django.conf import settings
from edc_model_wrapper.wrappers import ModelWrapper


class EnrollmentLossModelWrapper(ModelWrapper):

    model = 'tp_screening.enrollmentloss'
    next_url_name = settings.DASHBOARD_URL_NAMES.get('enrollment_listboard_url')
    next_url_attrs = ['screening_identifier']
