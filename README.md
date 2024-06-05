# Text Classification POC

## Live application Links
[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1-07CaFMbPILIF5yrVsHmGKdp2dHxbKi3q-ICuYfRei0#0)

## Problem Statement 
The project focuses on applying NLP to classify financial excerpts, including both paragraphs and tables, into predefined categories. This classification aids in the efficient preprocessing of data for financial analysts.

## Project Goals
Develop a proof-of-concept system capable of accurately categorizing financial excerpts into the following classes:
- **TEXT**: This category includes textual content such as sentences or paragraphs relevant to financial analysis. Tables are classified as TEXT only if they and are formatted solely to present textual content.
- **NOISE**: This includes any text or tables that are not directly useful for financial analysis, such as generic legal disclaimers or miscellaneous non-specific content. For example, an index or table of contents is noise since it's not company specific and no analyst would submit queries to search for content in the table of contents.
- **FINANCIAL-TABLE**: This pertains to tables that display financial data structured in rows and columns, featuring key financial metrics.


While this project involves a task that typically requires the use of machine learning models, you are not restricted to these methods alone. Feel free to employ any approach that you believe is suitable, whether it be complex algorithms or simple heuristics, based on your assessment of the problem. Your solution should be designed with scalability in mind, ensuring it can efficiently handle increases in demand while maintaining reasonable latency and cost-effectiveness.

## Technologies Used
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FF9900?style=for-the-badge)](https://huggingface.co/docs/transformers/en/model_doc/bert)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)


```
📦 Text Classification
├─ data
│  ├─ clean_data.json
│  ├─ excerpts.jsonl
│  └─ unlabeled_data.json
├─ models
│  ├─ bert_custom_1
│  ├─ bert_custom_2
│  ├─ bert_custom_3
│  ├─ distilBert_custom_1
│  └─ encder_model.pkl
├─ notebooks
│  ├─ BERT_TextClassification.ipynb
│  ├─ data_cleaning.ipynb
│  ├─ play_area_bert_train.ipynb
│  └─ play_area_usage.ipynb
├─ streamlit
│  ├─ main.py
│  └─ models.py
├─ project-guideline.md
├─ README.md
└─ requirements.txt
```

## Folder Structure
1. data - contains the data provided to train and also the precessed data
2. models - to store the fine tuned model and the label encoder
3. notebooks - contains 2 main notebooks and 2 test play area notebook
4. streamlit - contains code for UI app 


## How to run Application Locally
1. unzip the Project
2. create virtual env and install the requirements
3. Run NoteBooks:
    - *Note*: update data import path for notebooks to run
    1. Run the data_cleaning.ipynb first (this will create clean_data, unlabeled_data and save the label encoder)
    2. Run BERT_TextClassification.ipynb (this will create 4 custom bert models)
4. Now there are all the necessary models trained and saved in the models folder 
5. Run Streamlit App
    1. cd to the streamlit dir
    2. run command "streamlit run main.py"
6. Now the app is running locally
