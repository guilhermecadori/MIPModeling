#!/usr/bin/env python
# coding: utf-8

# #### Ex 4) 
# 
# A empresa americana KMX do setor automobilistico lançará três novos modelos de carros no próximo ano: modelo Arlington, modelo Marilandy e modelo Gristedes. A produção de cada um dos modelos passa pelos seguintes processos: injeção, fundição, usinagem, estamparia e acabamento. Os tempos médios de operação (minutos) de uma unidade de cada componente encontram-se na Tabela 2.15.
# Cada uma das operação é 100% automatizada. A quantidade de máquinas disponíveis para cada setor também se encontra na mesma tabela. É importante mencionar que cada máquina trabalha 16 horas por dia, de segunda a sexta-feira. O lucro unitário, além ddo potencial minimo de vendas por semana, de cada modelo de automóvel, de acordo o setor comercial, está especificado na tabela 2.16. Supondo que 100% dos modelos serão vendidos, formule o problema de programação linear que busca determinar as quantidades de automóveis de cada modelo a serem fabricados, a fim de maximizar o lucro liquido semanal.

# #### Processo de Modelagem
# ##### 1) Variáveis de Decisão:
# 
# *Generalizado:*
# 
# Variável de Decisão:
# * $ x_i $: Quantidade de carros do modelo ***i*** a ser produzida, un/semana
# 
# Índices
# * $ i $: Carro do modelo *i*, sendo *i* = {1, 2, 3}, representando os modelos *Arlington*, *Marilandy* e *Gristedes*
# * $ j $: Processo *j* de fabricação utilizado na produção do modelo *i*, sendo *j* = {1, 2, 3, 4, 5}, representando os processos de *Injeção*, *Fundição*, *Usinagem*, *Estamparia* e *Acabamento*
# 
# Dimensão dos Conjuntos dos Índices
# * $ n $: Modelos de carros a serem fabricados, sendo *n* = 3, a extensão do conjunto representado pelo índice *i*
# * $ m $: Processos necessários para a fabricação dos modelos considerados, sendo *m* = 5, a extensão do conjunto representado pelo índice *j*
# 
# *Aplicado ao Problema:*
# * $ x_1 $: Quantidade de carros do modelo *Arlington* (*1*) a ser produzida
# * $ x_2 $: Quantidade de carros do modelo *Marilandy* (*2*) a ser produzida
# * $ x_3 $: Quantidade de carros do modelo *Gristedes* (*3*) a ser produzida
# 
# 
# #### 2) Parâmetros
# 
# ***Consumo de Horas por Processo de Fabricação***
# 
# *Generalizado*
# * $ CONSUMOHORAS_{ij} $: Consumo de tempo pela máquina responsável pelo processo *j* para a fabricação de uma unidade do componente para o carro de modelo *i*, em horas para cada semana
# 
# *Aplicado ao Problema*
# * $ CONSUMOHORAS_{11} $: Consumo de horas da máquina de *Injeção* para produzir um componente para o modelo *Arlington*
# * $ CONSUMOHORAS_{12} $: Consumo de horas da máquina de *Fundição* para produzir um componente para o modelo *Arlington*
# * $ CONSUMOHORAS_{13} $: Consumo de horas da máquina de *Usinagem* para produzir um componente para o modelo *Arlington*
# * $ CONSUMOHORAS_{14} $: Consumo de horas da máquina de *Estamparia* para produzir um componente para o modelo *Arlington*
# * $ CONSUMOHORAS_{15} $: Consumo de horas da máquina de *Acabamento* para produzir um componente para o modelo *Arlington*
# * $ CONSUMOHORAS_{21} $: Consumo de horas da máquina de *Injeção* para produzir um componente para o modelo *Marilandy*
# * $ CONSUMOHORAS_{22} $: Consumo de horas da máquina de *Fundição* para produzir um componente para o modelo *Marilandy*
# * $ CONSUMOHORAS_{23} $: Consumo de horas da máquina de *Usinagem* para produzir um componente para o modelo *Marilandy*
# * $ CONSUMOHORAS_{24} $: Consumo de horas da máquina de *Estamparia* para produzir um componente para o modelo *Marilandy*
# * $ CONSUMOHORAS_{25} $: Consumo de horas da máquina de *Acabamento* para produzir um componente para o modelo *Marilandy*
# * $ CONSUMOHORAS_{31} $: Consumo de horas da máquina de *Injeção* para produzir um componente para o modelo *Gristedes*
# * $ CONSUMOHORAS_{32} $: Consumo de horas da máquina de *Fundição* para produzir um componente para o modelo *Gristedes*
# * $ CONSUMOHORAS_{33} $: Consumo de horas da máquina de *Usinagem* para produzir um componente para o modelo *Gristedes*
# * $ CONSUMOHORAS_{34} $: Consumo de horas da máquina de *Estamparia* para produzir um componente para o modelo *Gristedes*
# * $ CONSUMOHORAS_{35} $: Consumo de horas da máquina de *Acabamento* para produzir um componente para o modelo *Gristedes*
# 
# 
# ***Lucro***
# 
# *Generalizado*
# * $ LUCRO_i $: Lucro de venda de uma unidade do modelo *i*, em \$/un.
# 
# *Aplicado ao Problema*
# * $ LUCRO_1 $: Lucro de venda de uma unidade do modelo *Arlington*, em \$ 2.500/un
# * $ LUCRO_2 $: Lucro de venda de uma unidade do modelo *Marilandy*, em \$ 3.000/un
# * $ LUCRO_3 $: Lucro de venda de uma unidade do modelo *Gristedes*, em \$ 2.800/un
# 
# 
# ***Potencial de Vendas***
# 
# *Generalizado*
# * $ POTENCIALVENDA_i $: Potencial de venda de carros do modelo *i*, un/semana
# 
# *Aplicado ao Problema*
# * $ POTENCIALVENDA_1 $: Potencial de venda de carros do modelo *Arlington*, 50 un/semana
# * $ POTENCIALVENDA_2 $: Potencial de venda de carros do modelo *Marilandy*, 30 un/semana
# * $ POTENCIALVENDA_3 $: Potencial de venda de carros do modelo *Gristedes*, 30 un/semana
# 
# 
# **Quantidade de Máquinas Disponíveis por Processo***
# 
# *Generalizado*
# * $ QUANTMAQ_j $: Quantidade de máquinas disponíveis para realização do processo *j*, un/semana
# 
# *Aplicado ao Problema*
# * $ QUANTMAQ_1 $: Quantidade de máquinas disponíveis para realização de *Injeção*, 6 un/semana
# * $ QUANTMAQ_2 $: Quantidade de máquinas disponíveis para realização de *Fundição*, 8 un/semana
# * $ QUANTMAQ_3 $: Quantidade de máquinas disponíveis para realização de *Usinagem*, 5 un/semana
# * $ QUANTMAQ_4 $: Quantidade de máquinas disponíveis para realização de *Estamparia*, 8 un/semana
# * $ QUANTMAQ_5 $: Quantidade de máquinas disponíveis para realização de *Acabamento*, 5 un/semana
# 
# 
# **Disponibilidade de Dias de Funcionamento na Semana**
# 
# *Generalizado*
# * $ DIASFUNC $: Quantidade de dias trabalhados na semana 
# 
# *Aplicado ao Problema - Parâmetro padrão para todas as máquinas*
# * $ DIASFUNC $: Quantidade de dias trabalhados na semana, 5 dias/semana
# 
# 
# **Disponibilidade de Horas de Funcionamento por Máquina no Dia**
# 
# *Generalizado*
# * $ HORASDIA $: Quantidade de horas de funcionamento de cada máquina durante o dia
# 
# *Aplicado ao Problema - Parâmetro padrão para todas as máquinas*
# * $ HORASDIA $: Quantidade de horas de funcionamento de cada máquina durante o dia, 16 h/dia
# 
# 
# **Capacidade de Horas na Semana por Máquina**
# 
# *Generalizado*
# * $ CAPACIDADEHORASMAQ_j $: Quantidade de horas de funcionamento de cada máquina para o processo *j*, h/semana
# 
# *Aplicado ao Problema - Parâmetro padrão para todas as máquinas*
# * $ CAPACIDADEHORASMAQ_1 $: Quantidade de horas de funcionamento de cada máquina para *Injeção*, 80 h/semana
# * $ CAPACIDADEHORASMAQ_2 $: Quantidade de horas de funcionamento de cada máquina para *Fundição*, 80 h/semana
# * $ CAPACIDADEHORASMAQ_3 $: Quantidade de horas de funcionamento de cada máquina para *Usinagem*, 80 h/semana
# * $ CAPACIDADEHORASMAQ_4 $: Quantidade de horas de funcionamento de cada máquina para *Estamparia*, 80 h/semana
# * $ CAPACIDADEHORASMAQ_5 $: Quantidade de horas de funcionamento de cada máquina para *Acabamento*, 80 h/semana
# 
# 
# **Tempo de Processamento Consumido**
# 
# *Generalizado*
# * $ TEMPOCONSUMIDO_{ij} $: Quantidade de horas consumidas por cada máquina responsável pelo processo *j* para produzir uma unidade do componenete do modelo *i*
# 
# *Aplicado ao Problema - Parâmtro padrão para todas as máquinas*
# * $ TEMPOCONSUMIDO_{11} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Injeção* para produzir uma unidade do componenete do modelo *Arlington*
# * $ TEMPOCONSUMIDO_{12} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Fundição* para produzir uma unidade do componenete do modelo *Arlington*
# * $ TEMPOCONSUMIDO_{13} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Usinagem* para produzir uma unidade do componenete do modelo *Arlington*
# * $ TEMPOCONSUMIDO_{14} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Estamparia* para produzir uma unidade do componenete do modelo *Arlington*
# * $ TEMPOCONSUMIDO_{15} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Acabamento* para produzir uma unidade do componenete do modelo *Arlington*
# * $ TEMPOCONSUMIDO_{21} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Injeção* para produzir uma unidade do componenete do modelo *Marilandy*
# * $ TEMPOCONSUMIDO_{22} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Fundição* para produzir uma unidade do componenete do modelo *Marilandy*
# * $ TEMPOCONSUMIDO_{23} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Usinagem* para produzir uma unidade do componenete do modelo *Marilandy*
# * $ TEMPOCONSUMIDO_{24} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Estamparia* para produzir uma unidade do componenete do modelo *Marilandy*
# * $ TEMPOCONSUMIDO_{25} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Acabamento* para produzir uma unidade do componenete do modelo *Marilandy*
# * $ TEMPOCONSUMIDO_{21} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Injeção* para produzir uma unidade do componenete do modelo *Gristedes*
# * $ TEMPOCONSUMIDO_{22} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Fundição* para produzir uma unidade do componenete do modelo *Gristedes*
# * $ TEMPOCONSUMIDO_{23} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Usinagem* para produzir uma unidade do componenete do modelo *Gristedes*
# * $ TEMPOCONSUMIDO_{24} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Estamparia* para produzir uma unidade do componenete do modelo *Gristedes*
# * $ TEMPOCONSUMIDO_{25} $: Quantidade de horas consumidas por cada máquina responsável pelo processo de *Acabamento* para produzir uma unidade do componenete do modelo *Gristedes*
# 
# 
# #### 3) Função Objetivo
# 
# ***Objetivo:*** Maximizar o lucro de vendas
# 
# *Função Objetivo - Generalizada:*
# 
# $$ max \, Z = \sum_{i = 1} ^{n} LUCRO_i x_i $$
# 
# 
# *Função Objetivo - Aplicada ao Problema:*
# 
# $$ max \, Z = LUCRO_1 x_1 + LUCRO_2 x_2 + LUCRO_3 x_3 $$
# 
# 
# 
# #### 4) Restrições
# 
# ***Restrições Generalizadas***
# 
# 1) Restrição de tempo disponível para o processo *j* para produção de componentes para o modelo *i* em cada semana
# 
# \begin{gathered}
# \begin{aligned}
# &\sum_{i=1}^{n}\sum_{j=1}^{m} TEMPOCONSUMIDO_{ij} x_i \leq CAPACIDADEHORASMAQ_j &
# \end{aligned}
# \end{gathered}
# 
# 2) Restrição de potencial de mínimo de vendas do modelo *i*
# 
# \begin{gathered}
# \begin{aligned}
# &x_i \geq POTENCIALVENDA_i &
# \end{aligned}
# \end{gathered}
# 
# 3) Restrição de não-negatividade
# 
# \begin{aligned}
# &x_i \geq 0
# \end{aligned}
# 
# 
# ***Restrições Aplicadas ao Problema***
# 
# 1) Restrição de tempo disponível para o processo *j* para produção de componentes para o modelo *i* em cada semana
# 
# \begin{gathered}
# \begin{aligned}
# &\ TEMPOCONSUMIDO_{11} x_1 + TEMPOCONSUMIDO_{21} x_2 + TEMPOCONSUMIDO_{31} x_3 \leq CAPACIDADEHORASMAQ_1 &
# \end{aligned}
# \end{gathered}
# 
# \begin{gathered}
# \begin{aligned}
# &\ TEMPOCONSUMIDO_{12} x_1 + TEMPOCONSUMIDO_{22} x_2 + TEMPOCONSUMIDO_{32} x_3 \leq CAPACIDADEHORASMAQ_2 &
# \end{aligned}
# \end{gathered}
# 
# \begin{gathered}
# \begin{aligned}
# &\ TEMPOCONSUMIDO_{13} x_1 + TEMPOCONSUMIDO_{23} x_2 + TEMPOCONSUMIDO_{33} x_3 \leq CAPACIDADEHORASMAQ_3 &
# \end{aligned}
# \end{gathered}
# 
# \begin{gathered}
# \begin{aligned}
# &\ TEMPOCONSUMIDO_{14} x_1 + TEMPOCONSUMIDO_{24} x_2 + TEMPOCONSUMIDO_{34} x_3 \leq CAPACIDADEHORASMAQ_4 &
# \end{aligned}
# \end{gathered}
# 
# \begin{gathered}
# \begin{aligned}
# &\ TEMPOCONSUMIDO_{15} x_1 + TEMPOCONSUMIDO_{25} x_2 + TEMPOCONSUMIDO_{35} x_3 \leq CAPACIDADEHORASMAQ_5 &
# \end{aligned}
# \end{gathered}
# 
# 2) Restrição de potencial de mínimo de vendas do modelo *i*
# 
# \begin{gathered}
# \begin{aligned}
# &x_1 \geq POTENCIALVENDA_1 &
# \end{aligned}
# \end{gathered}
# 
# \begin{gathered}
# \begin{aligned}
# &x_2 \geq POTENCIALVENDA_2 &
# \end{aligned}
# \end{gathered}
# 
# \begin{gathered}
# \begin{aligned}
# &x_3 \geq POTENCIALVENDA_3 &
# \end{aligned}
# \end{gathered}
# 
# 3) Restrição de não-negatividade
# 
# \begin{aligned}
# &x_1, x_2, x_3 \geq 0
# \end{aligned}
# 
# 
# #### 5) Formulação Matemática Formal
# 
# $\displaystyle\ max \, Z = \sum_{i = 1} ^{n} LUCRO_i x_i $
# 
# 
# $\displaystyle s.t. $
# 
# $\displaystyle\sum_{i=1}^{n}\sum_{j=1}^{m} TEMPOCONSUMIDO_{ij} x_i \leq CAPACIDADEHORASMAQ_j $ $\,\,\,$ $\forall$ *i* $=1,...,n,$ $\,$ $\forall$ *j* $=1,...,m $
# 
# $\displaystyle\ x_i \geq POTENCIALVENDA_i $ $\,\,\,$ $\forall$ *i* $ =1,...,n $
# 
# $\displaystyle\ x_i \geq 0 $ $\,\,\,$ $\forall$ *i* $ =1,...,n $

# #### 6) Implementação Generalizada - gurobipy
# 
# 

# In[1]:


# Importando bibliotecas de trabalho
import gurobipy as gp
import numpy as np


# In[2]:


# Definição da quatidade de horas disponíveis na semana para cada máquina
DIASFUNC = 5 # Dias de operação na semana

HORASDIA = 16 # Horas de operação no dia

QTMAQ = np.array([6, 8, 5, 8, 5]) # Quantidade de máquinas disponíveis para o processo i

CAPACIDADEHORASMAQ = DIASFUNC * HORASDIA * QTMAQ # Capacidade de horas por semana para o processo i

# Criando parâmetros de diponibilidade de horas para cada máquina para o proceso i na semana
# RHS
maqProcesso, QTMAQ, DIASFUNC, HORASDIA, CAPACIDADEHORASMAQ = gp.multidict({
    "maqPro1": [QTMAQ[0], DIASFUNC, HORASDIA, CAPACIDADEHORASMAQ[0]],
    "maqPro2": [QTMAQ[1], DIASFUNC, HORASDIA, CAPACIDADEHORASMAQ[1]],
    "maqPro3": [QTMAQ[2], DIASFUNC, HORASDIA, CAPACIDADEHORASMAQ[2]],
    "maqPro4": [QTMAQ[3], DIASFUNC, HORASDIA, CAPACIDADEHORASMAQ[3]],
    "maqPro5": [QTMAQ[4], DIASFUNC, HORASDIA, CAPACIDADEHORASMAQ[4]] })

# Conferindo atribuições
#print(maqProcesso)
#print(QTMAQ)
#print(DIASFUNC)
#print(HORASDIA)
#print(CAPACIDADEHORASMAQ)


# In[3]:


# Criando parâmetros de potencial de venda mínima
# RHS
vendaModelo, POTENVENDAS = gp.multidict({
    "Arlington": 50,
    "Marilandy": 30,
    "Gristedes": 30 })


# In[4]:


# Parâmetros de horas demandados para cada processo (matriz tecnológica)
# LHS
minHoras = 60 # min/h

tempProcessoMin = np.array([3, 5, 2, 4, 2, 4, 5, 4, 5, 3, 3, 4, 4, 5, 3]) # em minutos para cada processo j

tempProcesso = tempProcessoMin / minHoras # em horas para cada processo j

consumoRecursos = {
    ("maqPro1", "Arlington"): tempProcesso[0],
    ("maqPro2", "Arlington"): tempProcesso[1],
    ("maqPro3", "Arlington"): tempProcesso[2],
    ("maqPro4", "Arlington"): tempProcesso[3],
    ("maqPro5", "Arlington"): tempProcesso[4],
    ("maqPro1", "Marilandy"): tempProcesso[5],
    ("maqPro2", "Marilandy"): tempProcesso[6],
    ("maqPro3", "Marilandy"): tempProcesso[7],
    ("maqPro4", "Marilandy"): tempProcesso[8],
    ("maqPro5", "Marilandy"): tempProcesso[9],
    ("maqPro1", "Gristedes"): tempProcesso[10],
    ("maqPro2", "Gristedes"): tempProcesso[11],
    ("maqPro3", "Gristedes"): tempProcesso[12],
    ("maqPro4", "Gristedes"): tempProcesso[13],
    ("maqPro5", "Gristedes"): tempProcesso[14] }

# Parâmetros de potencial mínimo de venda (matriz tecnológica)
# LHS
potVendaModelo = {
    ("venda1", "Arlington"): 1,
    ("venda2", "Marilandy"): 1,
    ("venda3", "Gristedes"): 1 }


# In[5]:


# Criando parâmetros de lucro por modelo de carro
modeloCarro, LUCRO = gp.multidict({
    "Arlington": 2500,
    "Marilandy": 3000,
    "Gristedes": 2800})


# In[6]:


# Criando o modelo
m = gp.Model("Max Lucro Vendas")

# Criando variáveis de decisão
qtProdmodelo = m.addVars(modeloCarro, name = "Modelo de Carro")


# In[7]:


# Criando restrições de disponibilidade de horas na semana para cada processo j
restrDisponib = m.addConstrs(((sum(consumoRecursos[j, i] * qtProdmodelo[i] for i in modeloCarro) 
                     <= CAPACIDADEHORASMAQ[j]) for j in maqProcesso), name = 'Restrições de Disponibilidade de horas na semana para cada processo')


# In[8]:


# Criando restrições de potencial mínimo de venda
restrPotenVendasMin = m.addConstrs(((qtProdmodelo[i] >= POTENVENDAS[i]) for i in modeloCarro),
                                   name = 'Restrições de Potencial Mínimo de Venda')


# In[9]:


# Criando função objetivo
m.setObjective(qtProdmodelo.prod(LUCRO), gp.GRB.MAXIMIZE)

# Otimizando o modelo
m.optimize()


# #### 7) Plano de Produção

# In[10]:


# Valores das variáveis de decisão
x1 = m.x[0]
x2 = m.x[1]
x3 = m.x[2]

x1 = round(x1, 0)
x2 = round(x2, 0)
x3 = round(x3, 0)

print("Plano de Produção:\n")
print("Modelo de Carro e Quantidade (un):")
print("Modelo ", modeloCarro, ": ", x1, "; ", x2, "; ", x3, sep = "")

# Valor da Função Objetivo
print("\nCusto Total: R$", round(m.objVal, 2))


# In[ ]:




