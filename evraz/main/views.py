from collections import defaultdict

from django.shortcuts import render
from django.http import JsonResponse

from .models import DataItem


def unique_keys_view(request):
    result = DataItem.objects.order_by().values('key').distinct()
    result = [item['key'] for item in result]
    return JsonResponse({'unique': result})


def get_values_view(request):
    items = DataItem.objects.all()
    keys = request.GET.get('keys')
    if keys:
        items = items.filter(key__in=keys.split(','))
    n = request.GET.get('n', 120)
    if n:
        n = int(n)
        max_offset = DataItem.objects.order_by('-offset').first().offset
        from_offset = max_offset - n
        items = items.filter(offset__gt=from_offset)

    result = defaultdict(list)
    for item in items.order_by('offset'):
        moment = int(item.moment.timestamp())
        if not result['moment']:
            result['moment'].append(moment)
        elif result['moment'][-1] != moment:
            result['moment'].append(moment)
        result[item.key].append(item.value)

    return JsonResponse(result)
