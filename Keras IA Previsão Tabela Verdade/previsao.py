import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Criar a tabela verdade
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Definir a função sigmoide
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

# Criar a rede neural
model = Sequential()
model.add(Dense(4, input_dim=2, activation=sigmoide))
model.add(Dense(1, activation=sigmoide))

# Compilar o modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinar o modelo
model.fit(X, y, epochs=500, batch_size=1)

# Fazer uma previsão
previsao = model.predict(np.array([[0, 1]]))
print(previsao) # saída: [[0.96985424]]