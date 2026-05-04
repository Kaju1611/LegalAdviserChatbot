Project README
This is a Python project with three Python files representing different phases of the project. Below are the instructions for setting up the environment and running the project.

Table of Contents
Environment Setup
Using Pipenv
Using Conda
Using Pip
Running the Project
Environment Setup
Using Pipenv
Pipenv is a tool that manages dependencies and virtual environments for Python projects.

Install Pipenv if you don't have it:

pip install pipenv
Navigate to the project directory and create a virtual environment:

pipenv install
Activate the virtual environment:

pipenv shell
(Optional) Install any additional dependencies:

pipenv install <package_name>
Using Conda
Conda is an open-source package management system and environment management system.

Create a new conda environment:

conda create -n myenv python=3.9
Activate the environment:

conda activate myenv
Install dependencies from requirements.txt (if available):

pip install -r requirements.txt
Using Pip
Pip is the standard package installer for Python.

Install virtualenv if you don't have it:

pip install virtualenv
Create a virtual environment:

virtualenv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Install dependencies from requirements.txt (if available):

pip install -r requirements.txt
Running the Project
The project consists of three Python files, each corresponding to a different phase of the project:

To run the App directly
streamlit run main.py
To run app in different phases
Phase 1: Run the first phase using:

streamlit run frontend.py
Phase 2: Run the second phase using:

python vector_database.py
Phase 3: Run the third phase using:

python rag_pipeline.py
Ensure that all dependencies are installed before running the scripts.

If you encounter any issues, feel free to reach out or check the documentation for the tools mentioned above.
