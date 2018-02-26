# QUIZ

## First try

### 01

We use it to pass variables computed during forward propagation to the corresponding backward propagation step. It contains useful values for backward propagation to compute derivatives.

### 02

- number of iterations
- learning rate α
- number of layers L in the neural network
- size of the hidden layers n[l]

### 03

The deeper layers of a neural network are typically computing more complex features of the input than the earlier layers.

### 04

False

### 05

for(i in range(1, len(layer_dims))):
  parameter[‘W’ + str(i)] = np.random.randn(layers[i], layers[i-1])) * 0.01
  parameter[‘b’ + str(i)] = np.random.randn(layers[i], 1) * 0.01

### 06

The number of layers L is 4. The number of hidden layers is 3.

### 07

True

### 08

True

### 09

- W[1] will have shape (4, 4)
- b[1] will have shape (4, 1)
- W[2] will have shape (3, 4)
- b[2] will have shape (3, 1)
- W[3] will have shape (1, 3)
- b[3] will have shape (1, 1)

### 10

W[l] has shape (n[l],n[l−1])
