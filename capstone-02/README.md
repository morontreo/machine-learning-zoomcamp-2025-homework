# Problem:  
Predicting  students' academic success or dropout  

# Description:  
Education is one of the pillars of the society hence is one of the most discussed topics in many nations worldwide.

The students are at the center of it as they are the product of such system and trying to get as many learn and be prepared for the future is the main goal.
However, this is a very difficult task.

As students come from different backgrounds it is more important than ever to consider which factors impacts the possibility for a students to graduate or dropout.

A model like the one presented in this project will help predict this outcome based on social-economic, demographic and academic factors that can be applied accross different countries.

# Files in project:
- capstone-evaluation.ipynb: Initial workbook containing the data import, EDA and evaluation of three models (LogisticRegression, DecisionTreeClassifier and RandomForestClassifier). All the steps taken are in the comments on the workbook.
- capstone-selected-model: Final workbook with the LogisticRegression as selected model
- higher-education-predictors-of-student-retention.csv: original dataset
- train.py: python script for training
- predict.py: python script for prediction
- model.bin: binary file of model created with pickle
- pyproject.toml: uv file with dependencies definition
- uv.lock: describe all dependency packages

# Folders in Project
- .ipynb.checkpoints: notebook related files
- .venv: folder with dependencies

# Instruction on how to use

## Without Docker - Virtual Environment (uv)
1. Open the Terminal/Command Prompt <BR>
2. cd into folder "capstone-02" <BR>
3. Execute the command: uv sync <BR>
4. Execute the command: uv run uvicorn predict:app --host 0.0.0.0 --port 9696 --reload <BR>
5. With the browser navigate to URL: http://localhost:9696/docs <BR>
6. Expand the block "POST / predict" and do "Try it out" <BR>
7. Enter the values you need in the different properties <BR>
8. Click Execute to see the result <BR>

## With Docker
1. Open the Terminal/Command Prompt <BR>
2. cd into folder "capstone-02" <BR>
3. Execute the command: docker build -t student-graduate-predictor . <BR>
4. Wait for the previous step to be done <BR>
5. Execute the command: docker run -it --rm -p 9696:9696 student-graduate-predictor <BR>
6. With the browser navigate to URL: http://localhost:9696/docs <BR>
7. Expand the block "POST / predict" and do "Try it out" <BR>
8. Enter the values you need in the different properties <BR>
9. Click Execute to see the result <BR>