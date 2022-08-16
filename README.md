# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The purpose of this project is to build a supervised learning model that will predict whether or not a loan would be approved. Eligibility is based on client details which were filled through an online application form. The details include the applicant's income, gender, marital status, education, number of dependents, and credit history.

## Hypothesis
* Applicants that have a good credit history are likely to get approved
* Applicants with higher applicant and coapplicant income
* Applicants with a higher level of education may earn more, and therefore more likely to be approved
* Number of dependents may affect eligibility due to less disposable income with more dependents
* Applicants who are not self-employed may have a more steady income

## EDA 
The amount of income that an applicant or coapplicant earns does not necessarily mean that the loan will be approved or denied. On average, applicants with higher education earn more and they are able to pay back a loan, yet they can still be denied. Other factors can play a role, such as, the number of dependents and credit history.


## Process
1) Hypothesis generation
2) Data exploration
3) Data cleaning 
4) Building a predictive model
5) Model deployment

The notebook containing the data preprocessing, model building, and the persisted model can be found [here](notebooks/).

The file to run the API is located [here](src/).

## Results/Demo
I used the logistic regression and random forest classifier to build the predictive model. Using the grid search method, the random forest classifier turned out to be the best model, yielding an accuracy score of around 79.5%.

## Challenges 
Currently, the model can be deployed locally. There were issues deploying the model to AWS EC2. 

## Future Goals
* There may be more criteria or relationships that could determine eligibility, but was not explored
* I could implement more metrics to determine how the model classifies Loan_Status
* Feature engineering could be implemented to improve predictions