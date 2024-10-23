SpaceX Launch Data Analysis
Project Overview
This project leverages data from SpaceX launches to predict the success of Falcon 9’s first-stage landings. Using historical data provided through the SpaceX REST API, we analyze a range of variables, such as flight numbers, launch dates, booster versions, payload masses, orbit types, and landing outcomes. The primary goal of this project is to develop machine learning models that predict the likelihood of a successful landing, thus aiding decision-making for future missions and optimizing resource allocation for SpaceX's reusable rockets.

Dataset
The dataset used for this analysis consists of SpaceX launch data and includes:

Launch sites
Booster versions
Payload masses
Orbit types
Flight numbers
Launch outcomes (Success/Failure)
Landing outcomes (Drone ship, ground pad, etc.)
Customer information

Key Data Points:
Timeframe: Data ranges from 2010 to 2020.
Payload Masses: Range from 4000 kg to 6000 kg.
Launch Sites: Data includes multiple launch sites, with success rates varying across locations.
Project Objectives
Analyze trends in launch outcomes based on payload mass, launch site, and booster versions.
Build machine learning models to predict the likelihood of successful landings.
Provide actionable insights to improve future mission success rates.

Methodology
Exploratory Data Analysis (EDA):
Visualized the distribution of launch outcomes and payload mass.
Identified trends and patterns using scatter plots and pie charts.

Modeling:
Trained and evaluated multiple machine learning models, including Logistic Regression, Support Vector Machine (SVM), Decision Tree, and K-Nearest Neighbors (KNN).
Decision Tree emerged as the best-performing model with an accuracy of 87.5%.

Data Visualization:
Created visual representations such as scatter plots for Payload vs. Launch Outcomes and pie charts for Launch Success ratios by site.

Results Summary
The Decision Tree model performed the best, achieving an accuracy of 87.5%, with other models (SVM, KNN, and Logistic Regression) delivering similar but slightly lower accuracies (~84.6% to 84.8%).
A scatter plot of Payload Mass vs. Launch Outcome highlighted the payload ranges where success was more likely.
Launch sites were compared in a pie chart, with the site having the highest success ratio emerging as a strong candidate for future launches.

Tools & Technologies
Python: For data processing, analysis, and modeling.
Pandas: For data manipulation and preprocessing.
Seaborn & Matplotlib: For data visualization.
Scikit-learn: For building machine learning models.
Jupyter Notebook: For developing and documenting the analysis.

Future Work:
Expand the analysis to include more recent SpaceX data beyond 2020.
Incorporate advanced models like Random Forest and Gradient Boosting for better predictive performance.
Fine-tune existing models using hyperparameter optimization techniques to further improve accuracy.
Implement real-time predictions using live data from SpaceX API.
Conclusion
This project provides a comprehensive analysis of SpaceX launch data, highlighting trends in payload mass and launch success, and delivering a predictive model to enhance decision-making for future space missions. The findings align with SpaceX's objectives of improving reusability and cost-efficiency by optimizing launch site selection and mission planning.
