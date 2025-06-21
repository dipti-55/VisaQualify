# VisaQualify: US Visa Eligibility Classifier

A machine learning-based web application to predict whether a U.S. visa application will be **certified** or **denied** based on applicant profile data.

### 🔗 Demo 👉 [Click here](https://drive.google.com/file/d/1WqcZO0EyG-wUP0XI0xJiUCBBbGeooO3M/view?usp=sharing)


# 🧩 Problem Statement
The U.S. Office of Foreign Labor Certification (OFLC) receives a vast number of job certification applications from employers each year to hire foreign workers. Due to the significant increase in application volume, there is a pressing need to streamline and optimize the visa evaluation process.

This project aims to develop a machine learning classification model that predicts whether a visa application is likely to be certified or denied based on historical data. By analyzing key features from previous applications, the model can assist in prioritizing and shortlisting candidates, thereby reducing manual workload and improving decision-making efficiency.


# 🎯 Objectives
* ✅ Analyze and preprocess historical visa application data provided by OFLC.

* ✅ Identify the most influential factors that affect the visa approval process.

* ✅ Build and evaluate a classification model to predict visa approval outcomes (Certified/Denied).

* ✅ Assist in recommending suitable applicant profiles based on predictive insights.

* ✅ Provide a deployable solution (e.g., web app) for internal use by immigration officers or consultancy services.

# 📊 Dataset Description
* The Dataset is part of Office of Foreign Labor Certification (OFLC)
* The data consists of 25480 Rows and 12 Columns

   ## Features

- **Continent**: Asia, Africa, North America, Europe, South America, Oceania  
- **Education**: High School, Master's Degree, Bachelor's, Doctorate  
- **Job Experience**: Yes, No  
- **Required Training**: Yes, No  
- **Number of Employees**: 15,000 to 40,000  
- **Region of Employment**: West, Northeast, South, Midwest, Island  
- **Prevailing Wage**: 700 to 70,000  
- **Contract Tenure**: Hour, Year, Week, Month  
- **Full Time**: Yes, No  
- **Age of Company**: 15 to 180  



# ⚙️ Project Structure
```
├── .github/
|   ├── workflows/
|       ├── aws.yaml
├── artifact/
├── config/
|   ├── model.yaml
|   ├── schema.yaml 
├── flowcharts/ 
├── logs/  
├── us_visa/
│   ├── cloud_storage/
|   |   ├── aws_storage.py
│   ├── components/
|   |   ├── data_ingestion.py
|   |   ├── data_validation.py
|   |   ├── data_transformation.py
|   |   ├── model_trainer.py
|   |   ├── model_evaluation.py
|   |   ├── model_pusher.py
│   ├── configuration/
|   |   ├── aws_connection.py
|   |   ├── mongo_db_connection.py
│   ├── constants/
│   ├── data_access/
│   ├── entity/
|   |   ├── artifact_entity.py
|   |   ├── config_entity.py
|   |   ├── estimator.py
|   |   ├── s3_estimator.py
│   ├── exception/
│   ├── logger/
│   ├── pipline/
|   |   ├── training_pipeline.py
|   |   ├── prediction_pipeline.py
│   ├── utils/
│       ├── main_utils.py
├── app.py
├── demo.py
├── Dockerfile
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```



# 🔄 Workflow 

### 1. 📥 **Data Ingestion**

* Connects to **MongoDB** to fetch raw data.
* Stores locally for further processing.

### 2. ✅ **Data Validation**

* Validates schema and checks data quality.
* Detects **data drift** using **Evidently AI**.

### 3. 🔄 **Data Transformation**

* Encodes categorical features and scales numericals.
* Saves transformation objects for consistent inference.

### 4. 🧠 **Model Training**

* Trains ML models.
* Uses cross-validation and saves best model.

### 5. 📊 **Model Evaluation**

* Compares new model with previous ones.
* Promotes only if performance improves.

### 6. 📦 **Model Pushing**

* Uploads final model to **AWS S3**.

### 7. 🧪 **Prediction Pipeline**

* Makes predictions using saved model via:

  * ✅ **Streamlit Web App**
  * ⚙️ CLI (`demo.py`)


### 8. 🚀 **CI/CD Pipeline**

* Uses **GitHub Actions** + **Docker** + **AWS (ECR & EC2)** for automated deployment.

### 9. 💻 **Streamlit Web Application**
* User-friendly UI for non-technical users.


---

# 🧠 Tech Stack / Tools Used
<div align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-00466b?style=for-the-badge&logo=matplotlib&logoColor=white" />
  <img src="https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyYAML-000000?style=for-the-badge&logo=yaml&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" />  
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-FF5722?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" /> <!-- AWS EC2 --> 
  <img src="https://img.shields.io/badge/AWS%20EC2-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" /> 
  <img src="https://img.shields.io/badge/AWS%20ECR-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" /> 
  <img src="https://img.shields.io/badge/AWS_S3-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" />
  <img src="https://img.shields.io/badge/Evidently%20AI-000000?style=for-the-badge&logoColor=white" />
  
</div>



---

# 🚀 How to Run ?

Follow the steps below to set up and run locally:

### 1. 📦 Clone the Repository

```bash
git clone https://github.com/dipti-55/VisaQualify.git
cd VisaQualify
```

### 2. 🐍 Create a Virtual Environment

```bash
python -m venv venv
```

### 3. ▶️ Activate the Virtual Environment

* On **Windows**:

  ```bash
  venv\Scripts\activate
  ```

* On **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 4. 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. ⚙️ Set Up Configuration

Ensure the `config/` directory includes:

* `model.yaml`: defines model parameters
* `schema.yaml`: defines the input data structure

Also, check that your AWS and MongoDB credentials are properly set (in environment variables or `configuration/` scripts as required).

### 6. 🏁 Run the Application

```bash
streamlit run app.py
```

This will launch the web application in your browser.

### 7. 🧪 Optional: Run the Demo Script

```bash
python demo.py
```


<!-- ---

# 🔄 Project Workflow

This project follows a modular and production-ready **ML pipeline architecture**, broken down into the following stages:

### 1. 📥 **Data Ingestion**

* Load and extract raw data from the source (e.g., CSV, database).
* Store the data in a structured format for further processing.

### 2. ✅ **Data Validation**

* Validate schema based on `schema.yaml`.
* Check for missing values, incorrect data types, or outliers.
* Log anomalies and save validation reports.

### 3. 🔄 **Data Transformation**

* Apply encoding to categorical features.
* Scale numerical values.
* Save transformation objects (encoders, scalers) for future inference.

### 4. 🧠 **Model Training**

* Train classification model (e.g., RandomForest, Logistic Regression).
* Evaluate using accuracy, precision, recall, and F1-score.
* Save the trained model and artifacts.

### 5. 📈 **Model Evaluation**

* Compare the newly trained model against existing models (if any).
* Approve the new model if performance improves.

### 6. 📦 **Model Pushing**

* Push the final model and transformation objects to a persistent store (e.g., local file system, AWS S3).

### 7. 🧪 **Prediction Pipeline**

* Use saved model and preprocessing steps to make predictions.
* Input can be via:

  * Streamlit Web App
  * CLI script (`demo.py`)
  * Future API endpoint (optional)

### 8. 🧠 **Model Monitoring (Optional)**

* Use tools like **Evidently AI** to monitor:

  * Data drift
  * Concept drift
  * Performance degradation
* Useful in real-world deployment scenarios.

### 9. 🚀 **CI/CD Pipeline**

* Uses **GitHub Actions** to automate testing, building, and deployment.
* Dockerized application is pushed to **AWS ECR**.
* **AWS EC2** instance pulls and runs the updated container.
* Ensures consistent and continuous deployment with minimal downtime.

---

### 📌 Summary Diagram (Optional)

You can include a simple diagram in your `flowcharts/` folder and reference it:

```markdown
![Project Workflow](flowcharts/project_workflow.png)
``` -->

