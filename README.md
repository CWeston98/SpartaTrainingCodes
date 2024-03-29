# python_codes
The following is a cleaned-up repo of all of the Python codes I was involved in during my training at Sparta


## pokemon_api
My first attempt to extract data from a website using requests, and first use of a config file to create a single point of truth. Creates customised pages for 'pokemon' and 'ability', but not for all of the pages in the contents. It can be run by running the 'contents.py' file inside the contents directory.


## population_model
Contains 2 attempts to simulate a growing rabbit population using Python. 1 attempt as a group; 1 attempt working by myself.

### data14_rabbit_project
Group attempt to simulate a rabbit population. We worked using an Agile approach using sprints with a length of 1 day for a week. I worked as a developer for the first 2 days, and as a BA for the remainder of the project. The hawks.py script was never integrated into the model as we ran out of time before we could finish it. It can be run using the 'main.py' file inside the directory.

### solo_rabbit_project
For the weekend after our attempt to complete the rabbit project, I worked on re-creating the task by myself. It uses some of the aspects from the group task - including the overall structure, but does not include others (e.g. the requirements.txt file). I attempted to use test-driven OOP to create the code and less of the code is hard-coded than in the group project making it easier to make changes. It can be run using the 'main.py' file inside the directory.


## starwars_mongodb
As with the pokemon_api, this uses the requests package to access an online API. However, this also saves the information into a MongoDB database, referencing the memory locations of items already present in the database. Can be run using the 'get_pilots.py' file - will only work if the MongoDB daemon is open in the background.


## Takeaway Project
Used databricks to run a notebook with access to PySpark. Included some data analysis, using Python to create visualisations. Can be found at:  
https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/8502256505760926/422960004629511/798258427306644/latest.html


## Kaggle Dataset Analysis
Analysed what contributes to the success rates of Kickstarter projects using Jupyter notebook. The data were taken from a Kaggle dataset available at:   
https://www.kaggle.com/kemical/kickstarter-projects?select=ks-projects-201801.csv
