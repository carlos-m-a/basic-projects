from django.conf import settings

def base_data(request):
    base_context = {}
    base_context['SITE_DOMAIN_NAME'] = settings.SITE_DOMAIN_NAME
    return base_context