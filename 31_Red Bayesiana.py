# Importar la librería pgmpy para trabajar con redes bayesianas
from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD

# Crear una instancia de la DBN
dbn = DBN()

# Definir las variables del modelo
dbn.add_edges_from([(('Time', 0), ('Time', 1)), (('Cost', 0), ('Cost', 1)), (('Decision', 0), ('Decision', 1))])

# Definir las CPDs para las variables
cpd_time_0 = TabularCPD(variable='Time', variable_card=2, values=[[0.7, 0.3]])
cpd_cost_0 = TabularCPD(variable='Cost', variable_card=2, values=[[0.6, 0.4]])
cpd_decision_0 = TabularCPD(variable='Decision', variable_card=2, values=[[0.8, 0.2]])

cpd_time_1 = TabularCPD(variable='Time', variable_card=2, values=[[0.9, 0.1], [0.7, 0.3]], evidence=['Time'], evidence_card=[2])
cpd_cost_1 = TabularCPD(variable='Cost', variable_card=2, values=[[0.7, 0.3], [0.5, 0.5]], evidence=['Cost'], evidence_card=[2])
cpd_decision_1 = TabularCPD(variable='Decision', variable_card=2, values=[[0.9, 0.1], [0.6, 0.4]], evidence=['Decision'], evidence_card=[2])

# Añadir las CPDs al modelo
dbn.add_cpds(cpd_time_0, cpd_cost_0, cpd_decision_0, cpd_time_1, cpd_cost_1, cpd_decision_1)

# Verificar la validez del modelo
assert dbn.check_model()

# Calcular la utilidad esperada de cada decisión
expected_utility_decision_0 = 0.8 * (0.7 * 0.6) + 0.2 * (0.3 * 0.4)
expected_utility_decision_1 = 0.9 * (0.1 * 0.3) + 0.1 * (0.9 * 0.7)

print("Utilidad esperada de Decision=0:", expected_utility_decision_0)
print("Utilidad esperada de Decision=1:", expected_utility_decision_1)
