🏏 T20 Cricket Score Predictor

A full-stack Machine Learning-powered web application that predicts the final score of a T20 cricket match based on real-time match conditions.

Live Demo

🔗 Frontend (Streamlit App):
    https://worldcup-score-predictor-system.onrender.com
    
🔗 Backend API (FastAPI):
    https://cricket-score-predictor-system.onrender.com

📸 Screenshots

![UI](assets/score_pred_2.png)

🧠 Project Overview

Built a system to predict the final T20 match score using features such as batting team, bowling team, city, current score, overs completed, wickets fallen, and runs in the last five overs. I used historical match data from the Cricsheet: A Retrosheet for Cricket (https://www.kaggle.com/datasets/veeralakrishna/cricsheet-a-retrosheet-for-cricket), where I parsed raw YAML files and converted them into a structured dataset by extracting ball-by-ball information.

Performed feature engineering by:
* Converting overs into ball-level match progression
* Computing features such as balls remaining, wickets remaining, and current run rate
* Aggregating recent performance (last 5 overs runs)

Developed a Scikit-learn pipeline using a ColumnTransformer for preprocessing and a Random Forest Regressor for prediction, and deployed the model as a production-ready ML service.

The model was trained on historical match data from the Cricsheet: A Retrosheet for Cricket(https://www.kaggle.com/datasets/veeralakrishna/cricsheet-a-retrosheet-for-cricket), which contains ball-by-ball records of T20 matches. The processed data was used to build a robust machine learning pipeline and deployed as a production-ready ML service.

⚙️ Tech Stack

🔹 Machine Learning
* Scikit-learn (Pipeline + Random Forest)
* Feature Engineering (CRR, balls left, wickets left)
* OneHotEncoder + ColumnTransformer

🔹 Backend
* FastAPI
* Pydantic (data validation)
* Model served via REST API
* Hosted on Render

🔹 Frontend
* Streamlit
* Interactive UI with user-friendly inputs
* Deployed on Render

🔹 Model Hosting
Hugging Face (for large .pkl model storage)

📦 Features
* Real-time score prediction
* Clean and interactive UI
* Robust input validation
* Production-ready API
8 Scalable deployment (Render + HuggingFace)

🧪 Model Details
* Algorithm: Random Forest Regressor
* Pipeline: Preprocessing + Model
* Metrics:
* MAE: 3.02
* R² Score: 0.97

🚧 Challenges Faced
* Handling large model files (>500MB)
* Deployment issues on Render (memory + file paths)
* Model loading optimization
* Input normalization and validation

👨‍💻 Author

Sanjara
