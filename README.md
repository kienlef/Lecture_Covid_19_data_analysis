# Applied Data Science - COVID 19 Data Analysis

**Additional content material to UDEMY video lecture course**


[UDEMY course Link - Video Lecture](https://www.udemy.com/course/applied-data-science-covid-19-prototype/?referralCode=5316264CAD7289C935C9)

The goal of this lecture is to transport the best practices of data science from the industry while developing a COVID-19 analysis prototype

The student should learn the process of modeling (Python) and a methodology to approach a business problem.

The final result will be a dynamic dashboard - which can be updated by one click - of COVID-19 data with filtered and calculated data sets like the current Doubling Rate of confirmed cases

Techniques used are REST Services, Python Pandas, scikit-learn, Facebook Prophet, Plotly, Dash, + bonus section Tableau

For this, we will follow an industry-standard process (CRISP-DM) by focusing on the iterative nature of agile development

* Business understanding (what is our goal)
* Data Understanding (where do we get data and cleaning of data)
* Data Preparation (data transformation and visualization)
* Modeling (Statistics, Machine Learning, and SIR Simulations on COVID Data)
* Deployment (how to deliver results, dynamic dashboards in python and Tableau)

The entire lecture follows the development flow of a rapid prototype project.

Focus for the student is to develop its prototype, source code snipped are provided.
Topics and the corresponding programming (Python) are introduced step by step in a very compact way.

The outline with the individual lectures and learning topics are as follows:

### Section 1: Introduction (10 min)

General introduction and course procedure

1.  Introduction (2 min)
2.  Learning Goals and Content Overview (5 min)
3. Used Python Resources               (3 min)

### Section 2: Business Understanding (28 min)

Applied data science should follow a process. We will use the CRISP-DM process to setup the project.

4.  Introduction to Data Science    (6 min)
5.  CRISP-DM                        (6 min)
6.  Terminology Data Science        (6 min)
7.  Python Project Setup            (9 min)
  * Python distribution via Anaconda
  * Project structure via Cookiecutter Data Science

## Section 3: Data understanding (37 min)

The data gathering can be a cumbersome task. We will access the COVID Johns Hopkins data set and other sources by an API call.

8. Introduction Data Understanding                (1 min)
9. Data Gathering - Johns Hopkins GITHUB          (6 min) -- check
  * GITHUB access of worldwide data
  * Project storage structure
10. Data Gathering Web Scraping Example           (10 min) -- check
 * Robert-Koch-Institute table scraping
 * Python requests
 * Python beautifulsoup
11. Data Gathering API call                       (7 min)
  * COVID-19 data Germany
  * JSON format
12. Data Gathering REST API call                  (6 min)
  * REST service definition
  * COVID-19 data USA via (smartable.ai)
13. Data Gathering wrap up                        (3 min)


## Section 4: Data Preparation  (18 min)
Data manipulation and transformation is an essential of any data scientist. We will transform the data towards clean data structures for test and feature construction purposes.

14. Initial Data Preparation                      (8 min)
  * Python pandas
  * First test data flat table
15. Conversion of Date Object                     (4 min)
  * Python datetime
16. Relational Data Structure                     (7 min)
  * Primary Key and relational data model

## Section 5: Explorative Data Analysis - Dynamic Dashboards     (23 min)
Visualizing the first result from static to dynamic dashboards

17. Introduction - Plotting with Matplotlib         (6 min)
  * Python matplotlib / seaborn
  * Quick static plots with matplotlib / seaborn
18. Dynamic Plots with Plot.ly                (5 min)
  * Python Plot.ly library
19. First Dynamic COVID 19 visualization      (4 min)
  * Callbacks Example and first prototype
20. Dynamic Plots via Dash                    (7 min)
  * Python Dash Example
  * Client Server Setup


## Section 6: Modeling  (55 min)
Within the modeling phase, the different mathematical transformation takes place. You will learn exponential slopes, linear regression, rolling linear regression, and signal filtering techniques.

21. Modeling Introduction           (1 min)
22. Modeling start with helper functions  (8 min)
  * Setting up helper functions for quick visualizations
  * Preparing Data

23. Exponential Slopes                      (4 min)
  * Calculating Doubling practices
  * Python apply a function via a time series
24.  Machine Learning Basics Introduction   (7 min)
  * Machine Learning Terminology
  * Learning pipeline and prediction pipeline
25. Scikit-Learn Linear Regression          (7 min)
  * Python scikit-learn
  * Ordinary Least Square (OLS)
26. ML model Hypothesis                (5 min)    
  * Learning/fit pipeline and prediction pipeline  
27. Log Feature Transformation              (3 min)
  * Transform the input data (feature transformation)
  * Applying linear regression on exponential data
28. Piecewise linear regression             (11 min)
  * Applying a regression over a sliding window
  * Approximating the doubling rates
29. Filtering the COVID Input and Doubling Rates  (8 min)
  * Python scipy
  * Savitzky-Golay filtering



## Section 7: Evaluation - Full Walkthrough       42:00

The goal is to update, process, and visualize all data on one click. We will stick all parts together on the full data set. All results will be visualized in the final DASH prototype

30. Preparing the full Walkthrough - Minimum Viable Product  (7 min)
  * setup the full walkthrough
31. Groupby apply on test data set (10 min)
  * groupby apply on a relational data set
  * deriving the individual parts
32. Merging the full dataset          (5 min)
  * Pandas left join on the full data set
33. Automated Feature Transformation   (11 min)
  * push to stand alone scripts
34. Finalizing the Minimum Viable Product (9 min)
  * Visualizing the full data set
  * Adapting the visualization script


## Section 8: Deployment 18:50
We will have a look at the next steps of professional application delivery and wrap up with best practices overview

35. Prepare for Professional Software Delivery  (8 min)
  * Requirements
  * Architecture Style
  * DevOps & Agile Delivery
36. Summary Best Practices (10 min)
  * Working in a company - it is all about value delivery


## Section 9: Predictive Machine Modeling        (62 min)

Modeling predictive applications is one key activity for data scientists. In this section, we will have a look
on time series forecasting with Facebook Prophet, how to train the machine learning model, and how to evaluate the results.

37. Forecasting / Predictions Overview  (9 min)
  * Terminology Forecasts vs. Predictions
  * Which technique for which problem
38. Overfitting Introduction            (1 min)
  * Overfitting explained
39. Overfitting data preparation        (9 min)
  * Show and prepare COVID data for overfitting example
40. Overfitting demo and metrics        (8 min)
  * Polynomial regression with different parameters
  * Overfitting demo and metrics
41. Cross-validation Explained          (3 min)  
  * Theory on cross-validation techniques
42. Forecasts Programming Intro         (6 min)
  * Forecast programming in Python
  * Introduction Facebook Prophet
43. Forecasts with Facebook Prophet     (9 min)
  * First forecast fo COVID data with FB Prophet
  * Short horizon predictions
44. Facebook Prophet Cross-validation   (5 min)
  * Using FB Prophet build-in validation functions
45. Controlling Results and trivial model (8 min)     
  * Understand and interpret Forecast results
  * Building a trivial model for a 7 day forecast
46. Selection Bias and Variance         (6 min)
  * Understanding the variance in the data and in the model
  * Link to Bayesian theory


## Section 10: Simulation of SIR compartmental model (30 min)

Compartmental models are a technique used to simplify the mathematical modeling of infectious disease.
In this section, we will understand and simulate the SIR model, including a curve-fitting approach.

47. SIR modeling of infectious disease (7 min)
  * mathematical modeling of infectious disease
  * coupled differential equation
48. Simulating the SIR curves (10 min)
  * Using simple Monte-Carlo simulation to visualize SIR curves
49. Curve fitting of SIR parameters (8 min)
  * Python scipy curve fitting
  * Python scipy integrate ordinary differential equations
50. Dynamic SIR Simulation Example (5 min)
  * Adapting and showing a dynamic infection rate


## Section 11: Bonus - Introduction to Tableau Dashboards (1h 10min)

You will learn the basics of Tableau, an interactive business intelligent software that helps to understand the data.
The section is stand alone and can be done at any time to learn and publish your first dashboard on COVID-19 data.

51. Introduction and Visual Tool overview (5:50)
52. Tableau and Section Goal (3:05)
53. Visualizing a world map (11:30)
54. Time series charts (7:15)
55. Rolling Mean Calculation (4:20)
56. Doubling Rate Calculation (6:45)
57. Linking Additional Data (11:30)
58. Dynamic Axis Selection (8:40)
59. Final Dashboard and Publishing (12:30)
