

[![Test Multiple Python Versions](https://github.com/rudiheydra/python-for-devops-2022/actions/workflows/main.yml/badge.svg)](https://github.com/rudiheydra/python-for-devops-2022/actions/workflows/main.yml)
# python-for-devops-2022

python-for-devops-2022

YouTube Python Devops Tutorial with Noah Gift



![Python-for-Devops](https://user-images.githubusercontent.com/53549619/177138595-88c444d6-c560-445b-b442-ef8796f1412b.png)

You can get a copy of the book [here](https://www.google.com/search?q=python+for+devops+book&rlz=1C1CHZN_enAU968AU968&oq=python+for+&aqs=chrome.0.69i59j69i57j0i433i512j0i512j46i131i433i512j69i60l3.7471j0j7&sourceid=chrome&ie=UTF-8).


![YouTube](https://user-images.githubusercontent.com/53549619/177138625-38fae8c1-f14d-4da1-8a24-980aae127dfa.PNG)

You can view the full YouTube video [here](https://www.youtube.com/watch?v=kwZNpieUreA&t=1907s).

## Creating Overview

### Create project scaffold

#### Creating a cloud based development environment such as:
  * Colab Notebook: Here is an example of how to use [Colab](https://colab.research.google.com/github/rudiheydra/python-for-devops-2022/blob/main/Getting_started_python_devops.ipynb#scrollTo=7OZyMC8JrUN2)

#### Important Components
  * Makefile 
  * Requirements.txt 
  * test_library.py
  * python_library 
  * Dockerfile
  * CLI
  * Microservices
  
  ##### 1. Create files and folders
    * touch Makefile
    * touch requirements.txt
    * mkdir devopslib && touch devopslib/__init__.py
    * touch hello.py && touch test_hello.py
  ##### 2. Create a virtual environment 
    * python3 -m venv .venv
    * source ~/.venv/bin/activate
  ##### 3. Edit Bash
    * vim ~/.bashrc
    * source ~/.venv/bin/activate

  #### 4. Final step
    * clone project and run `make all`

### Create CLI (Command Line Tools)

  * Create CLI with pyhton fire
  * run pyhton hello.py with flag --beverage muffins


### Create Microservices
  * Go to http://localhost:8080/docs to view Swagger Documentation
  ![SwaggerDocs](https://user-images.githubusercontent.com/53549619/177696504-99eab719-f04a-49ef-8b65-69848bdad857.PNG)


### Containerized Continuous Delivery
