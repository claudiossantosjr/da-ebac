import seaborn as sns
import pandas as pd

with open(file="./gasolina.csv", mode='r', encoding='utf8') as arquivo:
  conteudo = arquivo.read()

texto = conteudo.split('\n')

dia = []
for linha in texto:
  linha_separada = linha.split(',')
  dia.append(linha_separada[0])
dia.remove('dia')

_venda = []
for linha in texto:
  linha_separada = linha.split(',')
  _venda.append(linha_separada[1])
_venda.remove('venda')

venda = []
for linha in _venda:
  linha = float(linha)
  venda.append(linha)

list_final = pd.DataFrame((zip(dia, venda)), columns = ['dia', 'venda'])
list_final.to_csv("./gasolina_DF.csv", index=False)

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=list_final, x="dia", y="venda", palette="pastel")
  grafico.set(title='Grafico passageiros por ano', xlabel='Dias', ylabel='Preços');

grafico.figure.savefig('gasolina.png')