# QUIZ

## 1

0.99

## 2

ACC = (96 + 19) / (96 + 19 + 4 + 8) 
    = 0.906

## 3

PRE = TP / (TP + FP)
    = 96 / (96 + 8)
    = 0.923

## 4

REC = TP / (TP + FN)
    = 96 / (96 + 4)
    = 0.960


## 5

0.6

## 6

Model 1: Roc 1
Model 2: Roc 3
Model 3: Roc 2

## 7

Not enough information is given.

## 8

0.805008635579

## 9

- The best possible score is 1.0
- A model that always predicts the mean of y would get a score of 0.0

## 10

Precision

## 11

Recall

## 12

The model is probably misclassifying the frequent labels more than the infrequent labels.

## 13

```
# print(m)
grid_values = {'gamma': [0.01, 0.1, 1, 10], 'C': [0.01, 0.1, 1, 10]}
grid_clf_acc = GridSearchCV(m, param_grid=grid_values, scoring='recall')
grid_clf_acc.fit(X_train, y_train)
y_pred = grid_clf_acc.predict(X_test)

rec = recall_score(y_test, y_pred)
pre = precision_score(y_test, y_pred)

print('Recall score: {0:0.3f}'.format(rec))
print('Precision score: {0:0.3f}'.format(pre))
print('Recall-Precision: {0:0.3f}'.format(rec-pre))
```

0.520


## 14

```
# print(m)
grid_values = {'gamma': [0.01, 0.1, 1, 10], 'C': [0.01, 0.1, 1, 10]}
grid_clf_acc = GridSearchCV(m, param_grid=grid_values, scoring='precision')
grid_clf_acc.fit(X_train, y_train)
y_pred = grid_clf_acc.predict(X_test)

rec = recall_score(y_test, y_pred)
pre = precision_score(y_test, y_pred)

print('Recall score: {0:0.3f}'.format(rec))
print('Precision score: {0:0.3f}'.format(pre))
print('Recall-Precision: {0:0.3f}'.format(pre-rec))
```



