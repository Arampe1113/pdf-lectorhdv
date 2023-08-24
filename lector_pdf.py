import PyPDF2
import os



def extraer_correo(archivo_pdf):
    """
    Extrae el correo electrónico de un archivo PDF.
s
    Args:
      archivo_pdf (str): El nombre del archivo PDF.

    Returns:
      str: El correo electrónico extraído.
    """

    pdf_reader = PyPDF2.PdfFileReader(archivo_pdf)
    texto_pdf = pdf_reader.getPage(0).extractText()

    correo = ""
    for palabra in texto_pdf.split():
        if "@" in palabra:
            correo = palabra
            break

    return correo

def extraer_celular(archivo_pdf):
    """
    Extrae el número de celular de un archivo PDF.

    Args:
      archivo_pdf (str): El nombre del archivo PDF.

    Returns:
      str: El número de celular extraído.
    """

    pdf_reader = PyPDF2.PdfFileReader(archivo_pdf)
    texto_pdf = pdf_reader.getPage(0).extractText()

    celular = ""
    for palabra in texto_pdf.split():
        if "3" in palabra and palabra.isdigit():
            celular = palabra
            break

    return celular

def main():
    """
    Programa principal.
    """

    # Ruta de la carpeta con los archivos PDF
    directorio = r"C:\Users\aaramburo99\OneDrive - Cementos Argos S.A\Aaramburo99\Documentos\Requerimientos\REQUERIMIENTOS PENDIENTES DE FEEDBACK\REQUERIMIENTO TECH\Agosto 2023\PIPELINE CIENTIFICO DE DATOS"

    archivos_pdf = os.listdir(directorio)

    for archivo_pdf in archivos_pdf:
        if archivo_pdf.endswith(".pdf"):
            pdf_path = os.path.join(directorio, archivo_pdf)
            correo = extraer_correo(pdf_path)
            celular = extraer_celular(pdf_path)
            print(f"Correo electrónico: {correo}")
            print(f"Número de celular: {celular}")

if __name__ == "__main__":
    main()
