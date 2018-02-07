# QUIZ

## 1st try

### 01

x(i)<j>

### 02

Tx=Ty

### 03

- Sentiment classification (input a piece of text and output a 0/1 to denote positive or negative sentiment)
- Gender recognition from speech (input an audio clip and output a label indicating the speaker’s gender)

### 04

Estimating P(y<t>∣y<1>,y<2>,…,y<t−1>)

### 05 

(i) Use the probabilities output by the RNN to randomly sample a chosen word for that time-step as y^<t>. (ii) Then pass this selected word to the next time-step.

### 06

Exploding gradient problem.

### 07

100

### 08

Betty’s model (removing Γr), because if Γu≈0 for a timestep, the gradient can propagate back through that timestep without much decay.

### 09

Γu and 1−Γu

### 10

Unidirectional RNN, because the value of y<t> depends only on x<1>,…,x<t>, but not on x<t+1>,…,x<365>
