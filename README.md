
# Data Sweeper-- A Streamlit based Web App

Overview : 

Data Sweeper is a powerful tool designed for users to easily transform and analyze their CSV and Excel files.

It provides built-in functionalities for data cleaning, feature engineering, data visualization, and file conversion.

Whether you're a data scientist, business analyst, or a casual user, this app simplifies your data preprocessing tasks.


## Features

- Upload multiple files (CSV or Excel) for simultaneous processing.
- Data Cleaning: Handle missing values and remove duplicates with a single click.
- Feature Engineering: Select specific columns for study and analysis.
- Data Visualization: Generate quick visual insights with bar charts.
- File Conversion: Convert data between CSV and Excel formats with ease.


## Motivation

- Problem Statement: Data preprocessing can be tedious and repetitive, requiring technical expertise.

- Objective: To create an intuitive app that minimizes the effort required to clean, transform, and visualize data.

- Inspiration: Automating repetitive tasks for data preparation, inspired by the need for tools accessible to both technical and non-technical users.
## Tech Stack

- Frontend and Backend
Streamlit: For building the interactive web application interface.
Pandas: For data manipulation and analysis.
Python: Core programming language.

- File Handling
io.BytesIO: For converting files between formats (CSV and Excel).

- Deployment
Streamlit Community Cloud: Platforms for hosting the app online.

## Roadmap to Operate

- File Upload
Supports CSV and Excel file formats.
Accepts multiple files simultaneously for processing.

- Data Cleaning
Remove Duplicates: Eliminate redundant rows.
Handle Missing Values: Automatically fills numeric columns with their mean values.

- Feature Engineering
Allows users to choose specific columns for analysis.

- Data Visualization
Quickly visualize up to two numeric columns with bar charts.

- File Conversion
Convert processed files into desired formats (CSV or Excel) for download.



## Installation

Local Setup

- Clone the Repository:

```bash
git clone https://github.com/<your-username>/data-sweeper.git
cd data-sweeper
```
    
- Install Dependencies:

```bash
pip install -r requirements.txt
```

- Run the App:

```bash
streamlit run app.py
```

- Access the app in your browser at
http://localhost:8501
## Usage/Examples

How It Works:

- Upload your file(s) in the supported format (CSV or Excel).

- Choose data cleaning options to remove duplicates or handle missing values.

- Select columns relevant to your analysis.

- Visualize data insights with built-in charts.

- Convert and download your processed file.


## Deployment

### Steps to Deploy on Streamlit Cloud

- Push your project to GitHub.
- Go to Streamlit Community Cloud and sign in.
- Select your GitHub repository and deploy the app.
- Share the app URL with others.
- Deployed Link
- Add your deployed app link here once available.


## Optimizations in future

- Add more visualization types (e.g., pie charts, scatter plots).
- Support additional file formats (e.g., JSON, XML).
- Integrate machine learning for advanced feature engineering.
- Integrating a chatbot to summerize and answer the questions related to this project.


## Acknowledgements

- Inspiration from Streamlit tutorials and documentations , which provide stepwise guidance and the Python community.

- Thanks to open-source contributors for libraries like Pandas and Streamlit.


