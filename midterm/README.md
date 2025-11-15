# Problem: 
Water Potability Classifier

# Description:
There are many countries around the world with problems accessing potable water which means that many people does not have access to one of the most basic needs.

A model like this would help them categorize the water as potable or not based on some basic measurements without having to know all details hence reflecting the importance of applying it on the day to day.

# Files in project:

- midterm.ipynb: Initial workbook containing the data import, EDA and evaluation of three models (LogisticRegression, DecisionTreeClassifier and RandomForestClassifier)
- midterm-selected-model.ipynb: This is the final workbook with the selected model.
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
1- Open the Terminal/Command Prompt
2- cd into folder "midterm"
3- Execute the command: uv sync
4- Execute the command: uv run uvicorn predict:app --host 0.0.0.0 --port 9696 --reload
5- With the browser navigate to URL: http://localhost:9696/docs
6- Expand the block "POST / predict" and do "Try it out"
7- Enter the values you need in the different properties
8- Click Execute to see the result

## With Docker
1- Open the Terminal/Command Prompt
2- cd into folder "midterm"
3- Execute the command: docker build -t water-potability-predictor .
4- Wait for the previous step to be done
5- Execute the command: docker run -it --rm -p 9696:9696 water-potability-predictor
6- With the browser navigate to URL: http://localhost:9696/docs
7- Expand the block "POST / predict" and do "Try it out"
8- Enter the values you need in the different properties
9- Click Execute to see the result