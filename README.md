# intro-to-pytorch
Learning the Basics of Pytorch through an Online Course


Create Virtual Environment
`python3 -m venv env`


Activate the environment
`source env/bin/activate`
'


# Create Virtual Miniconda Environment

	- __Linux__ or __Mac__: 
	```
	conda create -n deep-learning python=3.6
    # For M1 macbooks, I had to just use the default python option

	conda create -n deep-learning python=3.8

	source activate deep-learning
	```

## Install PyTorch and torchvision; this should install the latest version of PyTorch.
	
	- __Linux__ or __Mac__: 
	```
	conda install pytorch torchvision -c pytorch 
	```

## Install the Required PIP Packages

```
pip install -r requirements.txt
```