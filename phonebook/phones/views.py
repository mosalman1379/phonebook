import logging

import weasyprint
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from phones.forms import PhoneForm
from django.views.decorators.http import require_POST, require_GET
from phones.models import Entry

logger = logging.getLogger(__name__)


@csrf_exempt
@require_POST  # just use POST method for sending data to server
def create_entry(request):
    """
    create an entry via ajax
    """
    form_instance = PhoneForm(data=request.POST)
    if form_instance.is_valid():
        entry_object = form_instance.save()
        return JsonResponse(data={'surname': entry_object.surname,
                                  'family_name': entry_object.family_name,
                                  'phone_number': entry_object.phone_number,
                                  'pk': entry_object.pk, 'success': True}, status=201)
    else:
        return JsonResponse(data={'success': False}, status=405)


@require_GET
def show_add_entry(request):
    """
    shows add entry form page
    """
    return render(request, 'phones/add_entry.html', context={'form': PhoneForm()})


@require_GET
def show_search_entry(request):
    """
    shows search form page
    """
    return render(request, 'phones/search.html')


def find_entry(request):
    """
    finds a phonebook entry by phone number with query string
    """
    phone_number = request.GET.get('phonenum', None)
    if not phone_number:
        logger.error(request, 'the number entered ia incorrect')
        return JsonResponse(data={'success': False, 'error': 'No number specified'}, status=400)
    entry_object = Entry.objects.filter(phone_number__contains=phone_number)
    out_list = list(entry_object.values())
    logger.info(request, 'we find some entry for entered number')
    return JsonResponse({'Results': out_list, 'Count': len(out_list)})


class CreatePDF(DetailView):
    model = Entry

    def get(self, request, *args, **kwargs):
        g = super(CreatePDF, self).get(request, *args, **kwargs)
        rendered_context = g.rendered_content
        pdf = weasyprint.HTML(string=rendered_context).write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        logger.info(request, 'pdf file created successfully')
        return response
