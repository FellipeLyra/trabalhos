import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dados_imoveis = np.array([[3, 200, 0, 1, 350000],
                         [4, 300, 1, 0, 480000],
                         [2, 150, 1, 1, 300000],
                         [5, 400, 0, 0, 550000],
                         [2, 100, 0, 0, 230000]])

X = dados_imoveis[:, :-1]
y = dados_imoveis[:, -1]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X_train, y_train, epochs=100, batch_size=16, verbose=0)

loss = model.evaluate(X_test, y_test)
print('Erro médio quadrático (RMSE):', np.sqrt(loss))

novo_imovel = np.array([[3, 250, 1, 1]])
novo_imovel = scaler.transform(novo_imovel)
previsao = model.predict(novo_imovel)
print('Preço previsto do novo imóvel:', previsao[0][0])
