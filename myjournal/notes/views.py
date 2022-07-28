from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Notebook, Note


def index(request):
    notebooks = Notebook.objects.all()
    context = {"notebooks": notebooks}
    # notes/template/notes/index.html as notes/index.html => django format
    return render(request, "notes/index.html", context)  # returns httpresponse


def notebook(request, notebook_id):
    try:
        notebook = Notebook.objects.get(pk=notebook_id)
    except Notebook.DoesNotExist:
        raise Http404("Notebook does not exist")
    return render(request, "notes/notebook.html", {"notebook": notebook})


def note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, "notes/note.html", {"note": note})
