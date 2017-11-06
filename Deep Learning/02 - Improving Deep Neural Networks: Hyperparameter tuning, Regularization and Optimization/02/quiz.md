# Quiz

## First try

### 01

a[3]{8}(7)

### 02

Training one epoch (one pass through the training set) using mini-batch gradient descent is faster than training one epoch using batch gradient descent.

### 03

- If the mini-batch size is 1, you lose the benefits of vectorization across examples in the mini-batch.
- If the mini-batch size is m, you end up with batch gradient descent, which has to process the whole training set before making progress.

### 04

If you’re using mini-batch gradient descent, this looks acceptable. But if you’re using batch gradient descent, something is wrong.

### 05

v2=10, vcorrected2=10

### 06

α=etα0

### 07

- Decreasing β will create more oscillation within the red line.
- Increasing β will shift the red line slightly to the right.

### 08

- (1) is gradient descent. (2) is gradient descent with momentum (small β). (3) is gradient descent with momentum (large β)

### 09

- Try tuning the learning rate α
- Try mini-batch gradient descent
- Try using Adam

### 10

Adam should be used with batch gradient computations, not with mini-batches.

### Résultat: 7/10
Faux: 2, 5, 9

## Second try

### 02

One iteration of mini-batch gradient descent (computing on a single mini-batch) is faster than one iteration of batch gradient descent.

### 05

v2=10, vcorrected2=7.5

### 09

- Try tuning the learning rate α
- Try mini-batch gradient descent
- Try using Adam
- Try better random initialization for the weights

### Résultat: 9/10
Faux: 5

## Third Try

### 05

v2=7.5, vcorrected2=10

### Résultat: 10/10
