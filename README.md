# Home Exercises : Top listened tracks per country project
Author : **KALMOGO Rodrigue Benjamin**

## How launch the project
The project uses Python Language in its version 3.x. 

the following commands allows to launch the project with the default data and parameters(to get the top 100 listened songs in each country )

```shell script
python main.py

or
python3 main.py data/input/song_data.csv 100
```


NB: you can get the answer of the first question (1. If you have a table like this, how do you write a query to get the most listened song for each country?) by:
```
python3 main.py data/input/song_data.csv 1
```

But if you want, you can use other data by this way() :

```shell script
python3 main.py path/to/song_data.csv top_k
```


## Run on Docker Container

You can also run the project inside a Docker Container. For this purpose the file Dockerfile was created.

```dockerfile
 docker build -t deadoralive .
 docker run deadoralive
```



## Standard of entities'naming in the project 

We have chosen to use the standard PEP 8 of python community in the entities naming in 
our project.
Let's check out this [link](https://pep8.org/)


### CI/CD
I put a very basic CI/CD workfow in the git repo just to test the execution by the commit or merge on the master.
For that, I used Github Action toolkit.
The workflow is described in the file located as followed 
> .github/workflows/python-app.yml