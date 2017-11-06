# QUIZ

## 1st Try

### Answers

#### 01
False

#### 02
Test Accuracy   Runtime   Memory size
98%             9 sec     9MB

#### 03
Accuracy is an optimizing metric; running time and memory size are a satisficing metrics.

#### 04
Train       Dev       Test
9,500,000   250,000   250,000

#### 05
True

#### 06
- This would cause the dev and test set distributions to become different. This is a bad idea because you’re not aiming where you want to hit.
- The test set no longer reflects the distribution of data (security cameras) you most care about.

#### 07
No, because there is insufficient information to tell.

#### 08
0.3% (accuracy of expert #1)

#### 09
A learning algorithm’s performance can be better human-level performance but it can never be better than Bayes error.

#### 10
- Train a bigger model to try to do better on the training set.
- Try decreasing regularization.

#### 11
- You should try to get a bigger dev set.
- You have overfit to the dev set.

#### 12
- It is now harder to measure avoidable bias, thus progress will be slower going forward.
- If the test set is big enough for the 0,05% error estimate to be accurate, this implies Bayes error is ≤0.05

#### 13
Look at all the models you’ve developed during the development process and find the one with the lowest false negative error rate.

#### 14
Try data augmentation/data synthesis to get more images of the new type of bird.

#### 15
- Needing two weeks to train will limit the speed at which you can iterate.
- Buying faster computers could speed up your teams’ iteration speed and thus your team’s productivity.
- If 100,000,000 examples is enough to build a good enough Cat detector, you might be better of training with just 10,000,000 examples to gain a ≈10x improvement in how quickly you can run experiments, even if each model performs a bit worse because it’s trained on less data.

### Resultat : 11/15
Faux: 1, 5, 13, 14

## 2nd try

### Answers

#### 01
True

#### 05
False

#### 13
Rethink the appropriate metric for this task, and ask your team to tune to the new metric.

#### 14
Add the 1,000 images into your dataset and reshuffle into a new train/dev/test split.

### Resultat : 14/15
Faux: 14

## 3rd try

### Answers

#### 14
Use the data you have to define a new evaluation metric (using a new dev/test set) taking into account the new species, and use that to drive further progress for your team.


