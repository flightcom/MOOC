# Quiz

## First try

### 01

- X is a matrix in which each column is one training example.
- a[2]4 is the activation output by the 4th neuron of the 2nd layer
- a[2](12) denotes the activation vector of the 2nd layer for the 12th training example.
- a[2] denotes the activation vector of the 2nd layer.

### 02

True

### 03

Z[l]=W[l]A[l−1]+b[l]
A[l]=g[l](Z[l])

### 04

ReLU

### 05

(4, 1)

### 06

Each neuron in the first hidden layer will perform the same computation. So even after multiple iterations of gradient descent each neuron in the layer will be computing the same thing as other neurons.

### 07

True

### 08

This will cause the inputs of the tanh to also be very large, thus causing gradients to be close to zero. The optimization algorithm will thus become slow.

### 09

- b[1] will have shape (4, 1)
- W[1] will have shape (4, 2)
- b[2] will have shape (1, 1)

### 10

Z[1] and A[1] are (4,2)

### Résultat : 6/10
### Faux : 4,7,9,10

## Second try

### 04

sigmoid

### 07

False

### 09

+ W[2] will have shape (1, 4)

### 10

Z[1] and A[1] are (4,m)

