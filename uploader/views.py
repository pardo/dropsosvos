import os
import json

from .models import DropboxUpload
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt


def test(request):
    return render(request, "test.html", {
        "data": "test"
    })


@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        du = DropboxUpload.upload(
            request.FILES["file"],
            request.POST["name"],
            request.POST.get("metadata",""),
        )

        return HttpResponse(json.dumps(dict(
            id=du.id,
            name=du.name,
            metadata=du.metadata,
        )), status=201)

    return HttpResponse("bad request", status=400)


def upload_view(request, upload_id):
    du = get_object_or_404(DropboxUpload, id=upload_id)

    return HttpResponse(json.dumps(dict(
        id=du.id,
        name=du.name,
        metadata=du.metadata,
        link=du.get_link()
    )), status=200)


def home(request):
    return render(request, "home.html", {
    })
