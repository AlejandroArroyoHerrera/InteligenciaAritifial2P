# Función para calcular la utilidad de una estrategia de inversión
def utility_investment(return_rate, risk_level):
    # Supongamos una función de utilidad simple que pondera el rendimiento y el riesgo
    utility = return_rate - 0.5 * risk_level
    return utility

# Valor esperado de la inversión sin información adicional
expected_utility_no_info = utility_investment(0.08, 0.02)

# Valor esperado de la inversión con información adicional sobre el rendimiento futuro de la acción
expected_utility_with_info = utility_investment(0.10, 0.02)

# Calcular el valor de la información
value_of_information = expected_utility_with_info - expected_utility_no_info
print("El valor de la informacion es:", value_of_information)
