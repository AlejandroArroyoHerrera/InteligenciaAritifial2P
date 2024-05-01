# Función para calcular la utilidad de una estrategia de inversión
def utility_investment(return_rate, risk_level):
    # Supongamos una función de utilidad simple que pondera el rendimiento y el riesgo
    utility = return_rate - 0.5 * risk_level
    return utility

# Definir las opciones de inversión y sus características
investment_strategies = {
    'Strategy_A': {'return_rate': 0.08, 'risk_level': 0.02},
    'Strategy_B': {'return_rate': 0.10, 'risk_level': 0.04}
}

# Calcular la utilidad esperada para cada estrategia
expected_utilities = {}
for strategy, attributes in investment_strategies.items():
    expected_utilities[strategy] = utility_investment(attributes['return_rate'], attributes['risk_level'])

# Seleccionar la estrategia con la mayor utilidad esperada
best_strategy = max(expected_utilities, key=expected_utilities.get)
print("La mejor estrategia de inversion es:", best_strategy)
