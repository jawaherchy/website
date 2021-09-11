# portfolio-project


This project has a presence across all urban, semi-urban, and rural areas. Customer-first applies for a bank loan after that bank validates the customer eligibility for a loan.  Banks can automate the loan eligibility process (real-time) based on customer detail provided while filling an online application form. These details are-  term,int_rate,home_ownership,annual_inc,purpose,addr_state,delinq_2yrs,revol_util,loan_amnt,total_acc and others. To automate this process, they have given a problem to identify the customer segments, That are eligible for loan amounts so that they can specifically target these customers.
This is a standard supervised classification task. A classification problem where we have to predict whether a loan would be approved or not. Below is the dataset attributes with a description.
 
Predictor Variables:
We have implemented Recursive Feature Elimination (RFE) using the Logistic Regression model to get the best 13 features.
Below mentioned are the features used for our model:
Predictor Variables
Description
term
The time it takes to eliminate the debt is a loan's term.
int_rate
Interest Rate on the loan.
home_ownership
The situation of owning a house, or of having a mortgage on it.
annual_inc
The self-reported annual income provided by the borrower during registration.
purpose
 the primary reason a borrower is requesting a loan.
addr_state
 The state is provided by the borrower in the loan application.
delinq_2yrs
Delinquency in 2 years: failure to make a required payment.
revol_util
the amount of the credit line used relative to total credit available.
loan_amnt
The total amount committed to that loan at that point in time. 
total_acc
 The total gross amount of Borrower's Accounts
bad_loan
A loan where repayments are not being made as originally agreed between the borrower and the lender.
emp_cr_length
how long any given account has been reported open.

 
Libraries
Pandas.
Matplotlib.
Seaborn.
Scikit-learn.
Numpy.
Joblib.
 
 
 
Algorithms
Extra Trees Classifier.
Logistic Regression Classifier.
Decision Tree Classifier.
Random Forest Classifier.
GradientBoostingClassifier.
MPL Classifier.
Linear Regression.
 
 
Best Model Accuracy: 69.34772516248839(GradientBoostingClassifier)
 
Models Applied and Motivation: 
 
Logistic Regression: 
With logistic regression, outputs have a nice probabilistic interpretation, and the algorithm can be regularized to avoid overfitting. Hence, we choose to build a logistic regression classifier.
Hyper Parameter tuning : 
We have implemented 2 models but applying hyperparameter tunning, cross-validation had decreased and the model accuracy increased.
Gradient Boosting Classifier:
Among those models, we found the best result from this model. And we applied this model to our project for prediction.
LinearRegression:
This model gave us overfitting in our project.
RandomForestClassifier and ExtraTreesClassifier:
It gave almost the same accuracy and cross validation into our project.
MLPClassifier:
A multilayer perceptron (MLP) is a class of feedforward artificial neural networks (ANN).
 
 
Confusion Matrix:
A confusion matrix is a summary of prediction results on a classification problem. The number of correct and incorrect predictions are summarized with count values and broken down by each class. It gives us insight not only into the errors being made by a classifier but more importantly the types of errors that are being made.
 
 
1.

2.

 
 
 
 
 
 
3.

 
4.

5.

 
6.

Model Accuracies: 
Random Forest Classifier----- 68.958
Logistic Regression ----- 61.652
Decision Tree Classifier----- 63.492
Extra Trees Classifier ----- 68.413
MLP Classifier----- 38.620
Linear Regression ----- 16.055
Gradient Boosting Classifier ----- 69.347
Cross-validation:
 
Random Forest Classifier----- 6.466
Logistic Regression ----- 61.649
Decision Tree Classifier----- 62.088
Extra Trees Classifier ----- 66.258
MLP Classifier----- 57.103
Linear Regression ----- 4.508
Gradient Boosting Classifier ----- 66.200
Overview:
● We had 68,928 observations of data, which took a lot of time for training. By implementing a learning curve for our data.
● Our data has been preprocessed using techniques like train_test split, filling null values, label encoder.
