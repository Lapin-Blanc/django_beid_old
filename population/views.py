from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from models import Personne
import barcode

def get_fidelity_card(request, person_id):
    try:
        p  = get_object_or_404(Personne, pk=person_id)
    except Http404:
        return reverse("population.views.get_person_by_barcode")
    ean = barcode.get_barcode('ean13', "2" + p.num_nat)
    return render_to_response("population/carte_fidelite.html", {
                                                          "personne": p,
                                                          "barcode":ean.render(),
                                                          })
    
def get_person_by_barcode(request):
    if request.GET:
        try:
            p = get_object_or_404(Personne, num_nat=request.GET['code'][1:-1])
            return HttpResponseRedirect("/admin/population/personne/%s/" % p.id)
        except Http404:
            return HttpResponseRedirect("/")
    else:
        return render_to_response("population/get_person.html")    