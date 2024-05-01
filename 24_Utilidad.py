# Función de utilidad para evaluar una decisión de inversión
def utility_investment(return_rate, risk_level):
    # Supongamos una función de utilidad simple que pondera el rendimiento y el riesgo
    utility = return_rate - 0.5 * risk_level
    return utility

# Ejemplo de uso de la función de utilidad para evaluar una decisión de inversión
return_rate = 0.08  # Rendimiento esperado del 8%
risk_level = 0.02   # Nivel de riesgo del 2%
decision_utility = utility_investment(return_rate, risk_level)
print("Utilidad de la decision de inversion:", decision_utility)
