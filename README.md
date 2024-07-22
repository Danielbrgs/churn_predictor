## Churn Prediction Project
#### Introduction:

This project aims to develop a web application to predict customer churn for a telecommunications company. The application uses a machine learning model trained to identify customers at high risk of churn, allowing the company to take proactive measures to retain them.

#### Development environment:

* Programming language: Python 3.12
* IDE: Visual Studio Code
* Libraries:
The required libraries are listed in the requirements.txt file.
#### Instructions for Local Execution:

* Clone the GitHub repository.
* Create a conda environment with Python 3.12 in the terminal.
* Install the libraries from the requirements.txt file using the pip install -r requirements.txt command.
* Navigate to the application directory (app).
* Run the application in the terminal using the command streamlit run app/app.py.
#### Data:

* The data dictionary used in this project can be found [at this link](https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset)

* The original data source can be accessed [here](https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113)

#### Data Analysis and Preprocessing:

Data analysis and pre-processing were carried out according to the CRISP-DM methodology and are documented in the notebook notebooks/note.ipynb. This notebook contains detailed comments, complete documentation and illustrative graphics. The trained model pipeline was saved in .pkl format using the joblib library and is used in the app.py application.

#### Web application

The web application is available at the following [link:](https://churnpredictor-oeqzx8kgmnsfbe9rtxernq.streamlit.app)

The application allows the user to make churn forecasts for several customers simultaneously, using a CSV file as input. The result of the forecast can be viewed in the application itself or downloaded in CSV format. The application also indicates whether the customer is at risk of churn and what the predicted churn probability is.

#### Additional Resources:

The notebook notebooks/note.ipynb contains detailed information on data analysis and pre-processing, model selection and training, hyperparameter optimization and model evaluation.
The requirements.txt file lists all the libraries needed to run the project.

#### Contributions:

Feel free to contribute to this project by opening issues on GitHub or sending pull requests with improvements.

**To learn more

* Connect with me on [LinkedIn](https://www.linkedin.com/in/daniel-braga-reis-725aa012a/)
* Explore my projects on [GitHub](https://github.com/Danielbrgs?tab=repositories)
