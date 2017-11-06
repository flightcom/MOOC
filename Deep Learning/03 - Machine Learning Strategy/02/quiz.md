# QUIZ

## 1st try

### Answers

#### 01
Spend a few days checking what is human-level performance for these tasks so that you can get an accurate estimate of Bayes error.

#### 02
False

#### 03
500 images on which the algorithm made a mistake

#### 04
False

#### 05
Choose the training set to be the 900,000 images from the internet along with 80,000 images from your car’s front-facing camera. The 20,000 remaining images will be split equally in dev and test sets.

#### 06
- You have a large data-mismatch problem because your model does a lot better on the training-dev set than on the dev set
- You have a large avoidable-bias problem because your training error is quite a bit higher than the human-level error.


#### 07
There’s insufficient information to tell if your friend is right or wrong.

#### 08
False because data augmentation (synthesizing foggy images by clean/non-foggy images) is more efficient.

#### 09
2.2% would be a reasonable estimate of the maximum amount this windshield wiper could improve performance.

#### 10
So long as the synthesized fog looks realistic to the human eye, you can be confident that the synthesized data is accurately capturing the distribution of real foggy images, since human vision is very accurate for the problem you’re solving.

#### 11
- You should also correct the incorrectly labeled data in the test set, so that the dev and test sets continue to come from the same distribution


#### 12
You cannot help her because the distribution of data you have is different from hers, and is also lacking the yellow label.

#### 13
Multi-task learning from your vision dataset could help your colleague get going faster. Transfer learning seems significantly less promising

#### 14
False

#### 15
Large training set

### Results
10/15
Faux: 1, 8, 11, 12, 13

## 2nd try

### Answers

#### 01
Spend a few days training a basic model and see what mistakes it makes.

#### 08
True because it is the largest category of errors. As discussed in lecture, we should prioritize the largest category of error to avoid wasting the team’s time.

#### 11
- You should also correct the incorrectly labeled data in the test set, so that the dev and test sets continue to come from the same distribution
- You should not correct incorrectly labeled data in the training set as well so as to avoid your training set now being even more different from your dev set.

#### 12
She should try using weights pre-trained on your dataset, and fine-tuning further with the yellow-light dataset.

#### 13
Neither transfer learning nor multi-task learning seems promising.

### Results
14/15
Faux: 8

## 3rd try

### Answers

#### 08 
False because this would depend on how easy it is to add this data and how much you think your team thinks it’ll help.