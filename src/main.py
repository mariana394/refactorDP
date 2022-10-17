# Actividad: Refactorizacion con Design Patterns
# Equipo 5
# Mariana Favarony Avila A01704671
# Genaro Alonso Sañudo A01194919
# Marcelo Sebastian Aguirre Alfaro A01039753

from patterns import csv_utils
from patterns import web_report
from patterns import print_report
from patterns import command

CSV_FILE = "taxi-data.csv"


def main():

    # Suponemos que el archivo el cliente lo actualizara con informacion
    # El archivo crece hacia abajo, entendido como que se añaden registros mas no columnas

    command1 = command.createOneCommand('html', CSV_FILE)
    command2 = command.createOneCommand('txt', CSV_FILE)
    command3 = command.createTwoCommand('html', 'txt', CSV_FILE)

    #Reporte con formato HTML
    html_report = command1.execute()
    html_report.create_file()

    #Repote con formato TXT
    txt_report = command2.execute()
    txt_report.create_file()

    # Reporte con ambos formatos
    txt_rpt, html_rpt = command3.execute()
    txt_rpt.create_file()
    html_rpt.create_file()




    

if __name__ == '__main__':
    main()
