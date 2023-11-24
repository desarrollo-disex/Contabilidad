from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os
from Contabilidad.settings import MEDIA_ROOT
import zipfile
from openpyxl import load_workbook

@login_required
def home(request):
    return render(request,'registration/inicio.html')

# def Upload_zip(request):
#     return render(request,'registration/Upload_zip.html')

def Upload_zip(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        zip_file_path = os.path.join(MEDIA_ROOT, filename)
        extract_folder = os.path.join(MEDIA_ROOT, 'extracted')
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)

        # Leer el archivo Excel desde la carpeta temporal
        excel_files = [f for f in os.listdir(extract_folder) if f.endswith('.xlsx')]
        if excel_files:
            excel_path = os.path.join(extract_folder, excel_files[0])
            df = pd.read_excel(excel_path)

            wb = load_workbook(excel_path)
            sheet = wb.active
        
            rows_to_delete = [row[0].row for row in sheet.iter_rows() if any(isinstance(cell.value, str) and "Application response" in cell.value for cell in row)]

            for row_idx in reversed(rows_to_delete):
             sheet.delete_rows(row_idx)
            
            wb.save(excel_path)
            df = pd.read_excel(excel_path)

            for file_name in os.listdir(extract_folder):
                file_path = os.path.join(extract_folder, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path): 
                        os.rmdir(file_path)
                except Exception as e:
                    print(f'Error al eliminar {file_path}: {e}')

            os.rmdir(extract_folder)

            return render(request, 'registration/Upload_zip.html', {'filename': filename, 'data': df.to_html()})
        
        
        else:
            os.rmdir(extract_folder)
            return HttpResponse("No se encontró un archivo Excel (.xlsx) dentro del archivo zip.")
    
    return render(request, 'registration/Upload_zip.html')


