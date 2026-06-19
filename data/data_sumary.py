import pandas as pd

# Cargar datos de demanda neta
df_demanda = pd.read_excel('data/Demanda sistematica real_04-2026.xlsx')

# Sumar toda la energia del cuatrimestre y dividir por 4 meses
# Cambiar 'Energia_MWh' por el nombre real de la cabecera en el CSV
demanda_total_mwh = df_demanda['Demanda sistémica real (Mwh)'].sum()
promedio_mensual_demanda_mwh = demanda_total_mwh / 4
promedio_mensual_demanda_gwh = promedio_mensual_demanda_mwh / 1000

print(f"Valor para Vensim (Demanda del Sistema): {promedio_mensual_demanda_gwh:.2f} GWh/mes")

# Cargar datos de retiros valorizados
# Los reportes del CEN suelen utilizar el punto y coma como separador
df_retiros = pd.read_csv('data/Descarga_Retiros_físicos_y_valorizados_01-2025_04-2025.csv', sep=';')

# Calcular el costo unitario promedio de la energia
# Cambiar las variables por los nombres exactos de las cabeceras en el CSV
df_retiros['retiro_ajustado_sum'] = df_retiros['retiro_ajustado_sum'].astype(str).str.replace(',', '.').astype(float)
df_retiros['retiro_ajustado_valorizado_sum'] = df_retiros['retiro_ajustado_valorizado_sum'].astype(str).str.replace(',', '.').astype(float)

total_fisico_mwh = df_retiros['retiro_ajustado_sum'].sum()
total_valorizado_usd = df_retiros['retiro_ajustado_valorizado_sum'].sum()

costo_promedio_mwh = total_valorizado_usd / total_fisico_mwh
costo_promedio_gwh = costo_promedio_mwh * 1000

print(f"Costo Unitario para Vensim (Calculo Rentabilidad): {costo_promedio_gwh:.2f} USD/GWh")
