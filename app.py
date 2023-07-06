import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_values(y):
     for i in range(len(y)):
        plt.text(i, y[i]//2, y[i], ha = 'center')

st.write("""
# Desafio da produção
Uma fábrica produz duas variedades de ração, A e B. Os dois tipos devem ser processados em duas máquinas diferentes, M1 e M2.
M1 possui uma disponibilidade mensal de processamento de 60h e M2 de 40. A ração A precisa de 2 horas
de processamento em ambas as máquinas. Já a ração B precisa de 3 horas na máquina M1 e somente 1 hora em M2. O lucro líquido/kg vendido de A é de R\$ 60,00 e o de B, R\$
70,00. Quais devem ser as quantidades produzidas das rações A e B? (Assuma que quantidades fracionárias
são permitidas, e toda a produção é vendida).
""")

st.write("### Variáveis")

st.write("""Queremos descobrir as quantidades (em kg) de cada produto, de forma que, obviamente, essas serão as nossas variáveis. Seja então:
$x_A$ : Quantidade produzida da ração A (kg) e 
$x_B$ : Quantidade produzida da ração B (kg).
""")

st.write("### Objetivo")

st.write("""Queremos descobrir as quantidades de $x_A$ e $x_B$ para que o lucro seja *maximizado*, ou seja, precisamos encontrar
uma função que descreve o lucro a partir das variáveis $x_A$ e $x_B$. Como cada kg de $x_A$ será vendida a R\$60,00 e cada kg de $x_B$
a R\$70,00, temos uma função da seguinte forma:
""")

st.write("\n                $f(x_A,x_B) = 60x_A + 70x_B$")

st.write("Considere os sliders abaixo. Alterando os valores de $x_A$ e de $x_B$ podemos ver no gráfico qual será o lucro da empresa.")
xa1 = st.slider('xA', step = 0.25, min_value = 0.0, max_value = 100.0)  # Esse é o slider
xb1 = st.slider('xB', step = 0.25, min_value = 0.0, max_value = 100.0)  # Esse é o slider

df1 = pd.DataFrame(  {"c1":[0,0,60 * xa1 + 70*xb1,0,0]}    )

fig1, ax1 = plt.subplots(1,1)
ax1.bar(df1.index,df1["c1"],  linewidth = 3, color = "g")
ax1.set_title("Lucro pela venda dos produtos")
ax1.set_ylabel("Lucro (R$)")

for i in range(len(df1["c1"].values)):
    ax1.text(i, df1["c1"].values[i]//2, df1["c1"].values[i], ha = 'center')

plt.ylim(0, 5000)
st.write(fig1)


st.write("""
O problema é que não podemos fabricar o quanto quisermos dos produtos, essas quantidades serão limitadas pelo tempo disponível nas máquinas...
""")

st.write("### Restrições")

st.write("""Cada kg de ração produzido consome um tempo nas duas máquinas M1 e M2, e as máquinas possuem um tempo máximo disponível para a 
produção. Dessa forma, os produtos "competem" para a utilização dos recursos M1 e M2. Existe uma restrição para o tempo
da máquina 1 e uma para o tempo da máquina 2, vamos criá-las separadamente:
""")

st.write("##### Máquina 1")

st.write("""Cada kg produzido de $x_A$ consome 2 unidades de tempo da máquina 1. E cada kg de $x_B$ 3. Assim, a quantidade
consumida de tempo da máquina 1, para quaisquer valores de $x_A$ e $x_B$ fica:
""")

st.write("\n                $2x_A + 3x_B$")

st.write("Como sabemos que a máquina tem uma disponibilidade de 12 horas, temos a seguinte restrição:")

st.write("\n                $2x_A + 3x_B \leq 60$ ")

st.write("""Também é possível verificar como o tempo da máquina é afetado pelas quantidade
produzidas de $x_A$ e $x_B$:
""")

xa2 = st.slider('xA', key = "xa2",step = 0.25, min_value = 0.0, max_value = 40.0)  # Esse é o slider
xb2 = st.slider('xB', key = "xb2", step = 0.25, min_value = 0.0, max_value = 40.0)  # Esse é o slider

df2 = pd.DataFrame(  {"c1":[0,0,2 * xa2 + 3 * xb2,0,0]}    )
fig2, ax2 = plt.subplots(1,1)
if 2 * xa2 + 3 * xb2 > 60:
    ax2.bar(["0","1","M1","2","3"],df2["c1"],  linewidth = 3, color = "r")
else:
    ax2.bar(["0","1","M1","2","3"],df2["c1"],  linewidth = 3, color = "g")
ax2.axhline(y = 60, color = 'r', linestyle = '--')
ax2.set_ylabel("Tempo (hs) consumido")
for i in range(len(df2["c1"].values)):
    ax2.text(i, df2["c1"].values[i]//2, df2["c1"].values[i], ha = 'center')


ax2.set_title("Tempo gasto na máquina M1")
plt.ylim(0, 90)
st.write(fig2)


st.write("##### Máquina 2")

st.write("""Da mesma forma, montamos a restrição de tempo da máquina 2:
""")

st.write("\n                $2x_A + x_B \leq 40$ ")

xa3 = st.slider('xA', key = "xa3",step = 0.25, min_value = 0.0, max_value = 40.0)  # Esse é o slider
xb3 = st.slider('xB', key = "xb3", step = 0.25, min_value = 0.0, max_value = 40.0)  # Esse é o slider
df3 = pd.DataFrame(  {"c1":[0,0,2 * xa3 + 3 * xb3,2 * xa3 + xb3,0,0]}    )
fig3, ax3 = plt.subplots(1,1)
if (2 * xa3 + 3 * xb3 > 60) or (2 * xa3 + xb3 > 40):
    ax3.bar(["0","1","M1","M2","2","3"],df3["c1"],  linewidth = 3, color = "r")
else:
    ax3.bar(["0","1","M1","M2","2","3"],df3["c1"],  linewidth = 3, color = "g")

for i in range(len(df3["c1"].values)):
    ax3.text(i, df3["c1"].values[i]//2, df3["c1"].values[i], ha = 'center')

ax3.axhline(y = 60, color = 'r', linestyle = '--')
ax3.axhline(y = 40, color = 'r', linestyle = '--')
ax3.set_title("Tempo gasto em M1 e M2")
plt.ylim(0, 90)
st.write(fig3)


st.write("##### Modelo completo")

st.write("""
O modelo completo (função objetivo + restrições) fica da seguinte forma:
""")

st.write("\n                $f(x_A,x_B) = 60x_A + 70x_B$")
st.write("Sujeito à:")
st.write("\n                $2x_A + 3x_B \leq 60$ ")
st.write("\n                $2x_A  + x_B \leq 40$ ")

st.write("""
Os gráficos das restrições junto à função objetivo ficam da seguinte forma:
""")

xa4 = st.slider('xA', key = "xa4", step = 0.25, min_value = 0.0, max_value = 40.0)  # Esse é o slider
xb4 = st.slider('xB', key = "xb4", step = 0.25, min_value = 0.0, max_value = 40.0)  # Esse é o slider
df4 = pd.DataFrame(  {"c1":[0,0,2 * xa4 + 3 * xb4,2 * xa4 + xb4,0,0]}    )
fig4, ax4 = plt.subplots(1,2)

if (2 * xa4 + 3 * xb4 > 60) or (2 * xa4 + xb4 > 40):
    ax4[0].bar(["0","1","M1","M2","2","3"],df4["c1"],  linewidth = 3, color = "r")
else:
    ax4[0].bar(["0","1","M1","M2","2","3"],df4["c1"],  linewidth = 3, color = "g")

ax4[0].axhline(y = 60, color = 'r', linestyle = '--')
ax4[0].axhline(y = 40, color = 'r', linestyle = '--')
ax4[0].set_title("Tempo gasto em M1 e M2")
ax4[0].set_ylim(0, 90)

for i in range(len(df4["c1"].values)):
    ax4[0].text(i, df4["c1"].values[i]//2, df4["c1"].values[i], ha = 'center')

df5 = pd.DataFrame(  {"c1":[0,0,60 * xa4 + 70*xb4,0,0]}    )

ax4[1].bar(df1.index,df5["c1"],  linewidth = 3, color = "g")
ax4[1].set_title("Lucro pela venda dos produtos")
plt.ylim(0, 5000)

plot_values(df5["c1"].values)


fig4.set_size_inches(10,5)


st.write(fig4)

st.write("# DESAFIO 2")
st.write("""
Se junte um grupos de no máximo 4 alunos e encontre a quantidade que deve ser produzida das rações.
O grupo que conseguir o maior lucro (L) terá um bônus na nota dado pela fórmula abaixo:
""")

st.write("$Nota = \dfrac{L}{5333.333}$")

st.write("Tempo total de 10 min.")

