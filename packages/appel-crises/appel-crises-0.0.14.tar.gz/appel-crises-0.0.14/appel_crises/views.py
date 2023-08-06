"""Module that provides the views of the app."""
import random

from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.cache import cache_control, never_cache

from appel_crises.constants import ASSOCIATIONS
from appel_crises.data import EMAIL_TEMPLATES
from appel_crises.models import Signature


@cache_control(max_age=60)
def home(request: HttpRequest):
    """Home view."""
    signatures = '{:,}'.format(Signature.get_count()).replace(',', ' ')
    context = dict(counter=signatures, associations=ASSOCIATIONS,)
    return render(request, "home.html", context=context)


def success(request: HttpRequest):
    """Signature success page"""
    return render(request, "success.html")


def success_email(request: HttpRequest):
    """Signature success page"""
    return render(request, "success_email.html")


# Contains a CSRF token/cookie
@never_cache
def form_no_js(request: HttpRequest):
    """Special page without js for signature"""
    return render(request, "form_no_js.html")


# Contains a CSRF token/cookie
@never_cache
def call_out_no_js(request: HttpRequest):
    """Special page without js for call_out"""
    email_template = random.choice(EMAIL_TEMPLATES)
    context = dict(email_template=email_template)

    return render(request, "call_out_no_js.html", context=context)


def error_no_js(
    request: HttpRequest, title: str = "", text: str = "", status: int = 400
):
    """Error page"""
    return render(
        request,
        "error_no_js.html",
        status=status,
        context=dict(error_title=title, error_text=text,),
    )
