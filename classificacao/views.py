from django.shortcuts import render
from .classifier import classificar_imagem, extrair_imagem_do_pdf
from .forms import UploadFileForms
from PIL import Image
from PIL import UnidentifiedImageError
import os


def upload_file(request):
    resultado = None
    if request.method == 'POST':
        form = UploadFileForms(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            ext = os.path.splitext(arquivo.name)[1].lower()
            if ext == '.pdf':
                # Salve o arquivo temporariamente e use extrair_imagem_do_pdf
                pass
            else:
                try:
                    imagem = Image.open(arquivo)
                    resultado = classificar_imagem(imagem)
                except UnidentifiedImageError:
                    resultado = None
    else:
        form = UploadFileForms()
    return render(request, 'classificacao/upload.html', {'form': form, 'resultado': resultado})




