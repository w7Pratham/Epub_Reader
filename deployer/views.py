from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EpubUploadForm
from .models import EpubFile
from ebooklib import epub
import ebooklib

def home(request):
    ebooks = EpubFile.objects.all()
    return render(request, 'deployer/home.html', {'ebooks': ebooks})

def upload_epub(request):
    if request.method == 'POST':
        form = EpubUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, message=f"EPUB File Uploaded Successfully")
            return redirect('home')
    else:
        form = EpubUploadForm()
    return render(request, 'deployer/upload_epub.html', {'form': form})

def read_epub(request, epub_id):
    epub_file = get_object_or_404(EpubFile, id=epub_id)
    file_path = epub_file.epub_file.path

    book = epub.read_epub(file_path)
    content = ""

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content += item.get_content().decode('utf-8')

    return render(request, 'deployer/read_epub.html', {'content': content})
