from conman.models import *

def get_base_vars(request):
    logged = request.user.is_authenticated()
    tabs_qs = Sector.objects.filter(parent = None).order_by('display_order')
    footer_qs = FooterFormatter(Sector.objects.all())
    foot = footer_qs[0]
    sub_foot = footer_qs[1]

    foot_pool = {}

    for (k,v) in zip (foot, sub_foot):
        foot_pool[k] = v

    result ={'logged':logged,
            'tabsList':tabs_qs,
            'foot_pool':foot_pool}

    return result

def FooterFormatter(qs):
    foot = qs.filter(parent = None)
    sub_foot = []
    for item in foot:
        sub_foot.append(qs.filter(parent=item))
    result = (foot,sub_foot)
    return result
