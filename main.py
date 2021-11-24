import eaf
import os
from pathlib import Path


historial_de_cuchara = []

base_dir = Path(__file__).resolve().parent

cuchara = eaf.ColadaDeAcero(
    0.76424,
    0.06267,
    0.46864,
    0.01872,
    0.00799,
    0.11846,
    0.02023,
    0.087,
    0.00988,
    0.05545,
    0.00654,
    0.0099,
    0.0066,
    88000
)

historial_de_cuchara.append(cuchara)
1+1

archivo_csv_con_datos = os.path.join(base_dir, "datos_de_colada.csv")
eaf.cuchara.cargar_analisis(archivo_csv_con_datos)

print(cuchara.carbono)