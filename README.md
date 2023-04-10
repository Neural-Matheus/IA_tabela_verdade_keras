# IA Tabela Verdade Keras
![inicio](https://www.imagensanimadas.com/data/media/562/linha-imagem-animada-0398.gif)<br>
Projeto de IA usando a Tabela Verdade para uma previsão.

O projeto é uma implementação de uma Rede Neural Artificial (RNA) em Python utilizando a biblioteca Keras. O objetivo da RNA é realizar a previsão da tabela verdade de uma porta lógica XOR, que é uma operação lógica que retorna verdadeiro apenas quando as entradas são diferentes entre si.

A RNA foi implementada com uma arquitetura simples, com uma única camada oculta de 4 neurônios e uma camada de saída com uma única saída binária. A função de ativação utilizada em todas as camadas foi a função sigmoide.

O código é composto por três partes principais: a definição da função sigmoide, a criação da RNA utilizando a biblioteca Keras e o treinamento e teste da RNA utilizando a tabela verdade do XOR.

O projeto foi desenvolvido como uma solução didática para aprendizado de conceitos básicos de Redes Neurais Artificiais utilizando Python e Keras. Ele é adequado para estudantes iniciantes em aprendizado de máquina que desejam ter uma compreensão melhor sobre Redes Neurais Artificiais e sua implementação em Python.

Para criar uma IA em Keras que preveja a tabela verdade, podemos utilizar uma rede neural com uma única camada de entrada, uma camada oculta e uma camada de saída. A camada de entrada terá duas entradas binárias, correspondentes às duas variáveis da tabela verdade. A camada oculta pode ter qualquer número de neurônios, mas usaremos 4 aqui. A camada de saída terá uma única saída binária correspondente ao resultado da tabela verdade.

Primeiramente, vamos importar as bibliotecas necessárias e criar a tabela verdade:<br>

![Parte 1](https://cdn.discordapp.com/attachments/690245537575731225/1094991964883128400/1.png)<br><br>
![Parte 2](https://cdn.discordapp.com/attachments/690245537575731225/1094991481988722748/2.png)

Em seguida, vamos definir a nossa rede neural. Para isso, precisamos definir a função de ativação que será usada nos neurônios. Vamos usar a função sigmoide, que é uma função matemática que comprime qualquer número real em um valor entre 0 e 1. Ela é definida como:

![Parte 3](https://cdn.discordapp.com/attachments/690245537575731225/1094991482475249724/3.png)

Agora, vamos criar a nossa rede neural com Keras. Usaremos a classe Sequential, que permite criar uma pilha linear de camadas de rede neural. Adicionaremos uma camada de entrada com duas entradas binárias, uma camada oculta com 4 neurônios e uma camada de saída com uma saída binária. Todas as camadas usarão a função sigmoide como função de ativação.

![Parte 4](https://cdn.discordapp.com/attachments/690245537575731225/1094991482789843044/4.png)

Agora, vamos compilar o modelo. Usaremos a função de perda binary_crossentropy, que é comumente usada para problemas de classificação binária, e o otimizador adam, que é um algoritmo de otimização comum para redes neurais.

![Parte 5](https://cdn.discordapp.com/attachments/690245537575731225/1094991483091824670/5.png)

Finalmente, vamos treinar o modelo. Usaremos 500 épocas de treinamento e um tamanho de lote (batch size) de 1.

![Parte 6](https://cdn.discordapp.com/attachments/690245537575731225/1094991483469299812/6.png)

Depois de treinado, podemos usar o modelo para fazer previsões. Por exemplo, podemos prever o resultado da tabela verdade para as entradas [0, 1]:

![Parte 7](https://cdn.discordapp.com/attachments/690245537575731225/1094991483754532974/7.png)

A saída indica que a rede neural prevê que o resultado da tabela verdade para as entradas [0, 1]

![Linha separação](https://pa1.narvii.com/6350/7d8ec35e754e829df6b350a891d7fb2cc3bc20d3_hq.gif)

Para rodar este código, você precisa ter as bibliotecas Numpy e Keras instaladas em seu ambiente Python. Você pode instalá-las utilizando o pip, que é o gerenciador de pacotes padrão do Python. Basta abrir o terminal ou prompt de comando e digitar os seguintes comandos:

![Numpy](https://cdn.discordapp.com/attachments/690245537575731225/1094991484035543130/install_1.png)<br>
![Keras](https://cdn.discordapp.com/attachments/690245537575731225/1094991484316549130/install_2.png)

Depois de instalar as bibliotecas, você pode criar um novo arquivo Python em seu editor de texto favorito (como o Visual Studio Code ou o Sublime Text) e copiar o código que eu forneci. Em seguida, basta salvar o arquivo com um nome (por exemplo, "previsao.py") e rodá-lo no terminal ou prompt de comando, digitando:

![Rodando](https://cdn.discordapp.com/attachments/690245537575731225/1094991484605976607/rodando.png)

O código irá executar e imprimir os resultados no terminal ou prompt de comando. É importante lembrar que o código deve estar no mesmo diretório (pasta) em que o terminal ou prompt de comando está apontando. Se o código estiver em um diretório diferente, você precisará navegar até o diretório correto no terminal ou prompt de comando antes de executá-lo.

![Linha separação](https://pa1.narvii.com/6350/7d8ec35e754e829df6b350a891d7fb2cc3bc20d3_hq.gif)
