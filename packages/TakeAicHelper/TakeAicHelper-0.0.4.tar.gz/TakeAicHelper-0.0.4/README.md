# TakeAicHelper

### Funções disponíveis
```Python
#Informações básicas sobre a base analisada;
  overview()
  
#Valor da Taxa de TCG;
  tcg()
  
#Dataframe específico sobre a intenção desejada;
  intentDetails("NOME_DA_INTENÇÃO")
  
#Ranking das entidades, pode ser gerado por intenção ou visualizar de forma geral;

  entities(n,'NOME_DA_INTENÇÃO') 
  entities(n)
  
#Ranking das intenções;
  intentions(n)
  
#Visualização da Taxa de Reconhecimento em gráfico;
  tr('chart')
  
#Visualização da Taxa de Reconhecimento em tabela;  
  tr('table')
  
#Visualização da Taxa de Reconhecimento em dataframe;
  tr()
  
#Visualização da Taxa de Compreensão interna por gráfico, com o score da NLP editável (default: 0.6);
  tci('table',0.9)
  
#Visualização da Taxa de Compreensão interna por tabela, com o score da NLP editável (default: 0.6);
  tci('chart',0.9)

#Visualização da Taxa de Compreensão geral em dataframe;
  tci() 

#Criação de arquivos em formato csv separados por intenção.
csvByIntentions(path='', sep=';')
```

### Regras do parâmetro n
O parâmentro *n* é um número inteiro, que se refere a quantidade de intenções ou entidades que serão listadas. 

> Caso o *n* for igual a **0** , **todas** as intenções/entidades serão listadas.

> Caso o *n* for um número positivo, as n intenções/entidades **mais** reconhecidas serão listadas.

> Caso o *n* for um número negativo, as n intenções/entidades **menos** reconhecidas serão listadas.

### Instanciando a classe

```Python
from TakeAicHelper.metrics import Metrics

analyse = Metrics(path=r'C:\Users\base.csv', encoding='utf-8', sep=';', minimunScore=0.6)
analyse.overview()
```


