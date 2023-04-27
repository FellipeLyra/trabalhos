import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Definindo as variáveis de entrada e saída
peso = ctrl.Antecedent(np.arange(0, 16.5, 0.1), 'peso')
sujeira = ctrl.Antecedent(np.arange(0, 11, 0.1), 'sujeira')
agua = ctrl.Consequent(np.arange(0, 101, 0.1), 'agua')

# Definindo as funções de pertinência das variáveis de entrada e saída
peso['muito_leve'] = fuzz.gaussmf(peso.universe, 2.5, 1)
peso['leve'] = fuzz.gaussmf(peso.universe, 6.5, 1)
peso['medio'] = fuzz.gaussmf(peso.universe, 10.5, 1)
peso['pesado'] = fuzz.gaussmf(peso.universe, 14, 1)

sujeira['baixo'] = fuzz.gaussmf(sujeira.universe, 2, 1)
sujeira['medio'] = fuzz.gaussmf(sujeira.universe, 5, 1)
sujeira['alto'] = fuzz.gaussmf(sujeira.universe, 8, 1)

agua['pouca'] = fuzz.gaussmf(agua.universe, 20, 10)
agua['media'] = fuzz.gaussmf(agua.universe, 50, 10)
agua['muita'] = fuzz.gaussmf(agua.universe, 80, 10)

# Definindo as regras
regra1 = ctrl.Rule(sujeira['baixo'] & peso['muito_leve'], agua['pouca'])
regra2 = ctrl.Rule(sujeira['baixo'] & peso['leve'], agua['pouca'])
regra3 = ctrl.Rule(sujeira['baixo'] & peso['medio'], agua['media'])
regra4 = ctrl.Rule(sujeira['baixo'] & peso['pesado'], agua['media'])
regra5 = ctrl.Rule(sujeira['medio'] & peso['muito_leve'], agua['pouca'])
regra6 = ctrl.Rule(sujeira['medio'] & peso['leve'], agua['media'])
regra7 = ctrl.Rule(sujeira['medio'] & peso['medio'], agua['media'])
regra8 = ctrl.Rule(sujeira['medio'] & peso['pesado'], agua['muita'])
regra9 = ctrl.Rule(sujeira['alto'] & peso['muito_leve'], agua['media'])
regra10 = ctrl.Rule(sujeira['alto'] & peso['leve'], agua['media'])
regra11 = ctrl.Rule(sujeira['alto'] & peso['medio'], agua['muita'])
regra12 = ctrl.Rule(sujeira['alto'] & peso['pesado'], agua['muita'])

#Definindo o sistema de controle
sistema_ctrl = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9, regra10, regra11, regra12])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

# Entrada do usuário para o peso e nível de sujeira das roupas
peso_input = float(input("Digite o peso das roupas (0 a 15.5 kg): "))
sujeira_input = float(input("Digite o nível de sujeira das roupas (0 a 10): "))
sistema.input['peso'] = peso_input
sistema.input['sujeira'] = sujeira_input

#Computando o resultado
sistema.compute()

#Saída do sistema de controle
print(f"A quantidade de água recomendada é {sistema.output['agua']:.2f}%.")

# Plotando os gráficos de pertinência das variáveis e a superfície de resposta
peso.view(sim=sistema)
sujeira.view(sim=sistema)
agua.view(sim=sistema)

# Mostrando os gráficos
plt.show()
