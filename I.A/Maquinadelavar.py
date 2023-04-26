import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definindo as variáveis de entrada e saída
peso = ctrl.Antecedent(np.arange(0, 11, 1), 'peso')
sujeira = ctrl.Antecedent(np.arange(0, 11, 1), 'sujeira')
agua = ctrl.Consequent(np.arange(0, 101, 1), 'agua')

# Definindo as funções de pertinência das variáveis de entrada e saída
peso['leve'] = fuzz.trimf(peso.universe, [0, 2, 4])
peso['medio'] = fuzz.trimf(peso.universe, [3, 5, 7])
peso['pesado'] = fuzz.trimf(peso.universe, [6, 8, 10])

sujeira['baixo'] = fuzz.trimf(sujeira.universe, [0, 2, 4])
sujeira['medio'] = fuzz.trimf(sujeira.universe, [3, 5, 7])
sujeira['alto'] = fuzz.trimf(sujeira.universe, [6, 8, 10])

agua['pouca'] = fuzz.trimf(agua.universe, [0, 20, 40])
agua['media'] = fuzz.trimf(agua.universe, [30, 50, 70])
agua['muita'] = fuzz.trimf(agua.universe, [60, 80, 100])

# Definindo as regras
regra1 = ctrl.Rule(peso['leve'] & sujeira['baixo'], agua['pouca'])
regra2 = ctrl.Rule(peso['leve'] & sujeira['medio'], agua['media'])
regra3 = ctrl.Rule(peso['leve'] & sujeira['alto'], agua['muita'])
regra4 = ctrl.Rule(peso['medio'] & sujeira['baixo'], agua['media'])
regra5 = ctrl.Rule(peso['medio'] & sujeira['medio'], agua['media'])
regra6 = ctrl.Rule(peso['medio'] & sujeira['alto'], agua['muita'])
regra7 = ctrl.Rule(peso['pesado'] & sujeira['baixo'], agua['media'])
regra8 = ctrl.Rule(peso['pesado'] & sujeira['medio'], agua['muita'])
regra9 = ctrl.Rule(peso['pesado'] & sujeira['alto'], agua['muita'])

# Definindo o sistema de controle
sistema_ctrl = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

# Entrada do usuário para o peso e nível de sujeira das roupas
peso_input = float(input("Digite o peso das roupas (0 a 10 kg): "))
sujeira_input = float(input("Digite o nível de sujeira das roupas (0 a 10): "))
sistema.input['peso'] = peso_input
sistema.input['sujeira'] = sujeira_input

#Computando o resultado
sistema.compute()

#Saída do sistema de controle
print(f"A quantidade de água recomendada é {sistema.output['agua']:.2f}%.")
