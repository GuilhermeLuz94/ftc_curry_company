# 1. Problema de negócio

A Cury Company é uma empresa de tecnologia que criou um aplicativo que conecta restaurantes, entregadores e pessoas.

Através desse aplicativo, é possível realizar o pedido de uma refeição, em qualquer restaurante cadastrado, e recebê-lo no conforto de sua casa por um entregador também cadastrado no aplicativo da Cury Company. 

A empresa realiza negócios entre restaurantes, entregadores e pessoas, e gera muito
sobre entregas, tipos de pedidos, condições climáticas, avaliação dos entregadores e etc. Apesar da entrega estar crescendo, em termos de entregas, o CEO não tem visibilidade completa dos KPis de crescimento da empresa. 

Você foi contratado como cientista de dados para criar soluções de dados para entrega, mas antes de treinar algoritmos, a necessidade da empresa é ter um dos principais KPis estratégicos organizados em uma única ferramenta, para que o CEO possa consultar e conseguir tomar decisões simples, porém importantes. 

A Cury Company possui um modelo de negócio chamado Marketplace, que faz o intermédio do negócio entre três clientes principais: Restaurantes, entregadores e pessoas compradoras. Para acompanhar o crescimento desses negócios, o CEO gostaria de ver as seguintes métricas de crescimento: 

# Do lado da empresa:

1. Quantidade de pedidos por dia. 
2. Quantidade de pedidos por semana. 
3. Distribuição dos pedidos por tipo de tráfego 
4. Comparação do volume de pedidos por cidade e tipo de tráfego. 
5. A quantidade de pedidos por entregador por semana.  
6. A localização central de cada cidade por tipo de tráfego. 

# Do lado entregador 
1. A menor e maior idade dos entregadores. 
2. A pior e a melhor condição de veiculos. 
3. A avaliação média por entregador. 
4. A avaliação média e os desvio padrão por tipo de tráfego.
5. A avaliação média e os desvio padrão por condições climáticas.
6. Os 10 entregadores mais rápidos por cidade.
7. Os 10 entregadores mais lentos por cidade. 


# 2. Premissas assumidas para análise
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa. 

1. A análise foi realizada com dados entre 11/02/2022 e 06/04/2022. 
2. Marketplace foi o modelo de negócio assumido.
3. As 3 principais visões de negócio foram: Visão transação de pedidos e visão entregadores.  

# 3. Estratégia da solução
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa. 

1. Visão do crescimento da empresa
2. Visão do crescimento dos entregadores. 
Cada visão é representada pelo seguinte conjunto de métricas.

## Visão da empresa. 
1. Pedidos por dia. 
2. Porcentagem de pedidos por condições climáticas.
3. Quantidade de pedidos por tipo e por cidade
4. Pedidos por semana. 
5. Quantidade de pedidos por tipo de entrega. 
6. Quantidade de pedidos por condições climáticas. 

## Visão dos entregadores.
1. Idade do entregador mais velho e o mais novo.
2. Avaliação do melhor e do pior veículo.
3. Avaliação média por entregador. 
4. Avaliação média por condições de trânsito.
5. Avaliação média por condições climáticas.
6. Tempo médio do entregador mais rápido. 
7. Tempo médio do entregador mais lento. 


# 4. Top 3 Insights de dados

1. A sazonalidade da quantidade de pedidos é diária. Há uma variação de aproximadamente 10% do número de pedidos em dia sequenciais.
2. As cidades do tipo Semi-Urban não possuem condições baixas de trânsito.
3. As maiores variações no tempo de entrega, acontecem durante o clima ensolarado.  
 

# 5. O produto final do projeto

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O painel pode ser acessado através deste link:
https://guilhermeluz94-ftc-curry-company-home-e47v31.streamlit.app/

# 6. Conclusão

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibem essas métricas da melhor forma possível para o CEO. 

Da visão da empresa, podemos concluir que o número de pedidos cresceu entre a semana 06 e a semana 13 do ano de 2022. 

# 7. Próximos passos. 
1. Reduzir o número de métricas. 
2. Criar novos filtros. 
3. Adicionar novas visões de negócios. 

