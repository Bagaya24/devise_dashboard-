from django.http import HttpResponse
from django.shortcuts import render, redirect

import api


# Create your views here.
def dashboard(requests, days_range=50, currencies="CAD", affichage='line'):

    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)
    page_label = {7: "Semaine", 30: "Mois", 365: "Annee"}.get(days_range, "Personnalise")
    mode = {"bar": "bar", "line": "line"}
    return render(requests, "devise/index.html", context={"data": rates,
                                                          "days_label": days,
                                                          "currencies": currencies,
                                                          "days": days_range,
                                                          "page_label": page_label,
                                                          "line": "line",
                                                          "bar": "bar",
                                                          "affichage": mode[f'{affichage}']})

def page_d_acceuill(requests):
    return redirect("home", days_range=30, currencies="USD", affichage="line")
