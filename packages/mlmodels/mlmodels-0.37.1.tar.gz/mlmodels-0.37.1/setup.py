# pylint: disable=C0321,C0103,C0301,E1305,E1121,C0302,C0330,C0111,W0613,W0611,R1705
# -*- coding: utf-8 -*-
"""


"""
import io
import os
import subprocess
import sys

from setuptools import find_packages, setup

######################################################################################
root = os.path.abspath(os.path.dirname(__file__))


##### check if GPU available  #########################################################
try :
  p = subprocess.Popen(["command -v nvidia-smi"], stdout=subprocess.PIPE, shell=True)
  out = p.communicate()[0].decode("utf8")
  gpu_available = len(out) > 0
except : pass

##### Version  #######################################################################
version ='0.37.1'
print("version", version)
""""
with io.open(os.path.join(root, 'nlp_architect', 'version.py'), encoding='utf8') as f:
    version_f = {}
    exec(f.read(), version_f)
    version = version_f['NLP_ARCHITECT_VERSION']
"""




######################################################################################
with open('requirements.txt') as fp:
    install_requires = fp.read()



######################################################################################
with open("README.md", "r") as fh:
    long_description = fh.read()


long_description =  """



# mlmodels 


This repository is the ***Model ZOO for Pytorch, Tensorflow, Keras, Gluon, LightGBM, Keras, Sklearn models etc*** with Lightweight Functional interface to wrap access to Recent and State of Art Deep Learning, ML models and Hyper-Parameter Search, cross platforms that follows the logic of sklearn, such as fit, predict, transform, metrics, save, load etc. 
Now, more than **60 recent models** (> 2018) are available in those domains : 
* Time Series, 
* Text classification, 
* Vision, 
* Image Generation,Text generation, 
* Gradient Boosting, Automatic Machine Learning tuning, 
* Hyper-parameter search.

With the goal to transform Script/Research code into re-usable batch/code with minimal code change, we used functional interface instead of pure OOP. This is because functional reduces the amount of code needed which is good to scientific computing. Thus, we can focus on the computing part than design. Also, it is easy to maintain for medium size project. 

A collection of Deep Learning and Machine Learning research papers is available in this repository.


![alt text](docs/mxnetf.png) ![alt text](docs/pytorch.PNG) ![alt text](docs/tenserflow.PNG)

## Benefits :

Having a standard framework for both machine learning models and deep learning models, 
allows a step towards automatic Machine Learning. The collection of models, model zoo in Pytorch, Tensorflow, Keras
allows removing dependency on one specific framework, and enable richer possibilities in model benchmarking and re-usage.
Unique and simple interface, zero boilerplate code (!), and recent state of art models/frameworks are the main strength 
of MLMODELS. Emphasis is on traditional machine learning algorithms but recent state of art Deep Learning algorithms. 
Processing of high-dimensional data is considered very useful using Deep Learning. For different applications, such as computer vision, natural language processing, object detection, facial recognition and speech recognition, deep learning created significant improvements and outstanding results.


Here you can find usages [guide](https://github.com/arita37/mlmodels/blob/dev/mlmodels/example/README_usage.md)

## Model List :
* [Time Series](#Time-series)
* [NLP](#NLP)
* [TABULAR](#TABULAR)
* [VISION](#VISION)



### Time Series:

1. MILA, Nbeats: 2019, Advanced interpretable Time Series Neural Network, [[Link](https://arxiv.org/abs/1905.10437)]

2. Amazon Deep AR: 2019, Multi-variate Time Series NNetwork, [[Link](https://ieeexplore.ieee.org/abstract/document/487783)]

3. Facebook Prophet 2017, Time Series prediction [[Link]](http://www.macs.hw.ac.uk/~dwcorne/RSR/00279188.pdf)

4. ARMDN, Advanced Multi-variate Time series Prediction : 2019, Associative and Recurrent Mixture Density Networks for time series. [[Link]](https://arxiv.org/pdf/1803.03800)

5. LSTM Neural Network prediction : Stacked Bidirectional and Unidirectional LSTM Recurrent Neural Network for Network-wide Traffic Speed Prediction [[Link]](https://arxiv.org/ftp/arxiv/papers/1801/1801.02143.pdf)


### NLP:

1. Sentence Transformers : 2019, Embedding of full sentences using BERT, [[Link](https://arxiv.org/pdf/1908.10084.pdf)]

2. Transformers Classifier : Using Transformer for Text Classification, [[Link](https://arxiv.org/abs/1905.05583)]

3. TextCNN Pytorch : 2016, Text CNN Classifier, [[Link](https://arxiv.org/abs/1801.06287)]

4. TextCNN Keras : 2016, Text CNN Classifier, [[Link](https://arxiv.org/abs/1801.06287)]

5. Bi-directionnal Conditional Random Field LSTM for Name Entiryt Recognition,  [[Link](https://www.aclweb.org/anthology/Y18-1061.pdf)]

5. DRMM:  Deep Relevance Matching Model for Ad-hoc Retrieval.[[Link](https://dl.acm.org/doi/pdf/10.1145/2983323.2983769?download=true)]

6. DRMMTKS:  Deep Top-K Relevance Matching Model for Ad-hoc Retrieval. [[Link](https://link.springer.com/chapter/10.1007/978-3-030-01012-6_2)]

7. ARC-I:  Convolutional Neural Network Architectures for Matching Natural Language Sentences
[[Link](http://papers.nips.cc/paper/5550-convolutional-neural-network-architectures-for-matching-natural-language-sentences.pdf)]

8. ARC-II:  Convolutional Neural Network Architectures for Matching Natural Language Sentences
[[Link](http://papers.nips.cc/paper/5550-convolutional-neural-network-architectures-for-matching-natural-language-sentences.pdf)]


### TABULAR:

#### LightGBM  : Light Gradient Boosting

#### AutoML Gluon  :  2020, AutoML in Gluon, MxNet using LightGBM, CatBoost

#### Auto-Keras  :  2020, Automatic Keras model selection


#### All sklearn models :

linear_model.ElasticNet\
linear_model.ElasticNetCV\
linear_model.Lars\
linear_model.LarsCV\
linear_model.Lasso\
linear_model.LassoCV\
linear_model.LassoLars\
linear_model.LassoLarsCV\
linear_model.LassoLarsIC\
linear_model.OrthogonalMatchingPursuit\
linear_model.OrthogonalMatchingPursuitCV


svm.LinearSVC\
svm.LinearSVR\
svm.NuSVC\
svm.NuSVR\
svm.OneClassSVM\
svm.SVC\
svm.SVR\
svm.l1_min_c


neighbors.KNeighborsClassifier\
neighbors.KNeighborsRegressor\
neighbors.KNeighborsTransformer

#### Binary Neural Prediction from tabular data:




### VISION:


1. Vision Models (pre-trained) :  
alexnet: SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size
[[Link](https://arxiv.org/pdf/1602.07360)]

2. densenet121: Adversarial Perturbations Prevail in the Y-Channel of the YCbCr Color Space
[[Link](https://arxiv.org/pdf/2003.00883.pdf)]

3. densenet169: Classification of TrashNet Dataset Based on Deep Learning Models
[[Link](https://ieeexplore.ieee.org/abstract/document/8622212)]

4. densenet201: Utilization of DenseNet201 for diagnosis of breast abnormality
[[Link](https://link.springer.com/article/10.1007/s00138-019-01042-8)]

5. densenet161: Automated classification of histopathology images using transfer learning
[[Link](https://doi.org/10.1016/j.artmed.2019.101743)]

6. inception_v3: Menfish Classification Based on Inception_V3 Convolutional Neural Network
[[Link](https://iopscience.iop.org/article/10.1088/1757-899X/677/5/052099/pdf )]

7. resnet18: Leveraging the VTA-TVM Hardware-Software Stack for FPGA Acceleration of 8-bit ResNet-18 Inference
[[Link](https://dl.acm.org/doi/pdf/10.1145/3229762.3229766)]

8. resnet34: Automated Pavement Crack Segmentation Using Fully Convolutional U-Net with a Pretrained ResNet-34 Encoder
[[Link](https://arxiv.org/pdf/2001.01912)]

9. resnet50: Extremely Large Minibatch SGD: Training ResNet-50 on ImageNet in 15 Minutes
[[Link](https://arxiv.org/pdf/1711.04325)]

10. resnet101: Classification of Cervical MR Images using ResNet101
[[Link](https://www.ijresm.com/Vol.2_2019/Vol2_Iss6_June19/IJRESM_V2_I6_69.pdf)]

11. resnet152: Deep neural networks show an equivalent and often superior performance to dermatologists in onychomycosis diagnosis: Automatic construction of onychomycosis datasets by region-based convolutional deep neural network
[[Link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5774804/pdf/pone.0191493.pdf)]


***More resources are available [here](https://github.com/arita37/mlmodels/blob/dev/README_model_list.md)***

######################################################################################

### ① Installation Guide:

### (A) Using pre-installed Setup (one click) :

[Read-more](https://github.com/arita37/mlmodels/issues/101)



### (B) Manual Install as editable package in Linux

```bash
conda create -n py36 python=3.6.5 -y
source activate py36

cd yourfolder
git clone https://github.com/arita37/mlmodels.git mlmodels
cd mlmodels
git checkout dev
```

### (C) Using Colab :
[Read-more](https://github.com/arita37/mlmodels/blob/dev/README_usage.md)


### Initialize template and Tests
Will copy template, dataset, example to your folder
```bash
ml_models --init  /yourworkingFolder/
```
   


##### To test Hyper-parameter search:
```bash
ml_optim
```


##### To test model fitting
```bash
ml_models
```
    
    
        
#### Actual test runs

[Read-more](https://github.com/arita37/mlmodels/actions)

![test_fast_linux](https://github.com/arita37/mlmodels/workflows/test_fast_linux/badge.svg)

![test_fast_windows](https://github.com/arita37/mlmodels/workflows/test_fast_windows/badge.svg?branch=dev)

![ All model testing (Linux) ](https://github.com/arita37/mlmodels/workflows/code_structure_linux/badge.svg)

_______________________________________________________________________________________

## Usage in Jupyter/Colab

[Read-more](https://github.com/arita37/mlmodels/blob/dev/README_usage.md)

_______________________________________________________________________________________

## Command Line tools:

[Read-more](https://github.com/arita37/mlmodels/blob/dev/README_usage_CLI.md)



_______________________________________________________________________________________

## Model List

[Read-more](https://github.com/arita37/mlmodels/blob/dev/README_model_list.md)

_______________________________________________________________________________________

## How to add a new model

[Read-more](https://github.com/arita37/mlmodels/blob/dev/README_addmodel.md)

_______________________________________________________________________________________

## Index of functions/methods

[Read-more](https://github.com/arita37/mlmodels/blob/dev/README_index_doc.py)

_______________________________________________________________________________________



### LSTM example in TensorFlow ([Example notebook](mlmodels/example/1_lstm.ipynb))

#### Define model and data definitions
```python
# import library
import mlmodels


model_uri    = "model_tf.1_lstm.py"
model_pars   =  {  "num_layers": 1,
                  "size": ncol_input, "size_layer": 128, "output_size": ncol_output, "timestep": 4,
                }
data_pars    =  {"data_path": "/folder/myfile.csv"  , "data_type": "pandas" }
compute_pars =  { "learning_rate": 0.001, }

out_pars     =  { "path": "ztest_1lstm/", "model_path" : "ztest_1lstm/model/"}
save_pars = { "path" : "ztest_1lstm/model/" }
load_pars = { "path" : "ztest_1lstm/model/" }


#### Load Parameters and Train
from mlmodels.models import module_load

module        =  module_load( model_uri= model_uri )                           # Load file definition
model         =  module.Model(model_pars=model_pars, data_pars=data_pars, compute_pars=compute_pars)             # Create Model instance
model, sess   =  module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)


#### Inference
metrics_val   =  module.fit_metrics( model, sess, data_pars, compute_pars, out_pars) # get stats
ypred         = module.predict(model, sess,  data_pars, compute_pars, out_pars)     # predict pipeline
```


---

### AutoML example in Gluon ([Example notebook](mlmodels/example/gluon_automl.ipynb))
```python
# import library
import mlmodels
import autogluon as ag

#### Define model and data definitions
model_uri = "model_gluon.gluon_automl.py"
data_pars = {"train": True, "uri_type": "amazon_aws", "dt_name": "Inc"}

model_pars = {"model_type": "tabular",
              "learning_rate": ag.space.Real(1e-4, 1e-2, default=5e-4, log=True),
              "activation": ag.space.Categorical(*tuple(["relu", "softrelu", "tanh"])),
              "layers": ag.space.Categorical(
                          *tuple([[100], [1000], [200, 100], [300, 200, 100]])),
              'dropout_prob': ag.space.Real(0.0, 0.5, default=0.1),
              'num_boost_round': 10,
              'num_leaves': ag.space.Int(lower=26, upper=30, default=36)
             }

compute_pars = {
    "hp_tune": True,
    "num_epochs": 10,
    "time_limits": 120,
    "num_trials": 5,
    "search_strategy": "skopt"
}

out_pars = {
    "out_path": "dataset/"
}



#### Load Parameters and Train
from mlmodels.models import module_load

module        =  module_load( model_uri= model_uri )                           # Load file definition
model         =  module.Model(model_pars=model_pars, compute_pars=compute_pars)             # Create Model instance
model, sess   =  module.fit(model, data_pars=data_pars, model_pars=model_pars, compute_pars=compute_pars, out_pars=out_pars)      


#### Inference
ypred       = module.predict(model, data_pars, compute_pars, out_pars)     # predict pipeline


```

---

### RandomForest example in Scikit-learn ([Example notebook](mlmodels/example/sklearn.ipynb))
```
# import library
import mlmodels

#### Define model and data definitions
model_uri    = "model_sklearn.sklearn.py"

model_pars   = {"model_name":  "RandomForestClassifier", "max_depth" : 4 , "random_state":0}

data_pars    = {'mode': 'test', 'path': "../mlmodels/dataset", 'data_type' : 'pandas' }

compute_pars = {'return_pred_not': False}

out_pars    = {'path' : "../ztest"}


#### Load Parameters and Train
from mlmodels.models import module_load

module        =  module_load( model_uri= model_uri )                           # Load file definition
model         =  module.Model(model_pars=model_pars, data_pars=data_pars, compute_pars=compute_pars)             # Create Model instance
model, sess   =  module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)          # fit the model


#### Inference
ypred       = module.predict(model,  data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)     # predict pipeline
```


---

### TextCNN example in keras ([Example notebook](example/textcnn.ipynb))

```python
# import library
import mlmodels

#### Define model and data definitions
model_uri    = "model_keras.textcnn.py"

data_pars    = {"path" : "../mlmodels/dataset/text/imdb.csv", "train": 1, "maxlen":400, "max_features": 10}

model_pars   = {"maxlen":400, "max_features": 10, "embedding_dims":50}
                       
compute_pars = {"engine": "adam", "loss": "binary_crossentropy", "metrics": ["accuracy"] ,
                        "batch_size": 32, "epochs":1, 'return_pred_not':False}

out_pars     = {"path": "ztest/model_keras/textcnn/"}



#### Load Parameters and Train
from mlmodels.models import module_load

module        =  module_load( model_uri= model_uri )                           # Load file definition
model         =  module.Model(model_pars=model_pars, data_pars=data_pars, compute_pars=compute_pars)             # Create Model instance
module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)          # fit the model


#### Inference
data_pars['train'] = 0
ypred       = module.predict(model,  data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)
```

---

### Using json config file for input ([Example notebook](example/1_lstm_json.ipynb), [JSON file](mlmodels/mlmodels/example/1_lstm.json))

#### Import library and functions
```python
# import library
import mlmodels

#### Load model and data definitions from json
from mlmodels.models import module_load
from mlmodels.util import load_config

model_uri    = "model_tf.1_lstm.py"
module        =  module_load( model_uri= model_uri )                           # Load file definition

model_pars, data_pars, compute_pars, out_pars = module.get_params(param_pars={
    'choice':'json',
    'config_mode':'test',
    'data_path':'../mlmodels/example/1_lstm.json'
})

#### Load parameters and train
model         =  module.Model(model_pars=model_pars, data_pars=data_pars, compute_pars=compute_pars)             # Create Model instance
model, sess   =  module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)          # fit the model

#### Check inference
ypred       = module.predict(model, sess=sess,  data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)     # predict pipeline


```

---

### Using Scikit-learn's SVM for Titanic Problem from json file ([Example notebook](mlmodels/example/sklearn_titanic_svm.ipynb), [JSON file](mlmodels/example/sklearn_titanic_svm.json))

#### Import library and functions
```python
# import library
import mlmodels

#### Load model and data definitions from json
from mlmodels.models import module_load
from mlmodels.util import load_config

model_uri    = "model_sklearn.sklearn.py"
module        =  module_load( model_uri= model_uri )                           # Load file definition

model_pars, data_pars, compute_pars, out_pars = module.get_params(param_pars={
    'choice':'json',
    'config_mode':'test',
    'data_path':'../mlmodels/example/sklearn_titanic_svm.json'
})

#### Load Parameters and Train

model         =  module.Model(model_pars=model_pars, data_pars=data_pars, compute_pars=compute_pars)             # Create Model instance
model, sess   =  module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)          # fit the model


#### Inference
ypred       = module.predict(model,  data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)     # predict pipeline
ypred


#### Check metrics
import pandas as pd
from sklearn.metrics import roc_auc_score

y = pd.read_csv('../mlmodels/dataset/tabular/titanic_train_preprocessed.csv')['Survived'].values
roc_auc_score(y, ypred)


```

---

### Using Scikit-learn's Random Forest for Titanic Problem from json file ([Example notebook](mlmodels/example/sklearn_titanic_randomForest.ipynb), [JSON file](mlmodels/example/sklearn_titanic_randomForest.json))

#### Import library and functions
```python
# import library
import mlmodels

#### Load model and data definitions from json
from mlmodels.models import module_load
from mlmodels.util import load_config

model_uri    = "model_sklearn.sklearn.py"
module        =  module_load( model_uri= model_uri )                           # Load file definition

model_pars, data_pars, compute_pars, out_pars = module.get_params(param_pars={
    'choice':'json',
    'config_mode':'test',
    'data_path':'../mlmodels/example/sklearn_titanic_randomForest.json'
})


#### Load Parameters and Train
model         =  module.Model(model_pars=model_pars, data_pars=data_pars, compute_pars=compute_pars)             # Create Model instance
model, sess   =  module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)          # fit the model


#### Inference

ypred       = module.predict(model,  data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)     # predict pipeline
ypred

#### Check metrics
import pandas as pd
from sklearn.metrics import roc_auc_score

y = pd.read_csv('../mlmodels/dataset/tabular/titanic_train_preprocessed.csv')['Survived'].values
roc_auc_score(y, ypred)

```

---

### Using Autogluon for Titanic Problem from json file ([Example notebook](mlmodels/example/gluon_automl_titanic.ipynb), [JSON file](mlmodels/example/gluon_automl.json))

#### Import library and functions
```python
# import library
import mlmodels

#### Load model and data definitions from json
from mlmodels.models import module_load
from mlmodels.util import load_config

model_uri    = "model_gluon.gluon_automl.py"
module        =  module_load( model_uri= model_uri )                           # Load file definition

model_pars, data_pars, compute_pars, out_pars = module.get_params(
    choice='json',
    config_mode= 'test',
    data_path= '../mlmodels/example/gluon_automl.json'
)


#### Load Parameters and Train
model         =  module.Model(model_pars=model_pars, compute_pars=compute_pars)             # Create Model instance
model   =  module.fit(model, model_pars=model_pars, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)          # fit the model
model.model.fit_summary()


#### Check inference
ypred       = module.predict(model,  data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)     # predict pipeline

#### Check metrics
model.model.model_performance

import pandas as pd
from sklearn.metrics import roc_auc_score

y = pd.read_csv('../mlmodels/dataset/tabular/titanic_train_preprocessed.csv')['Survived'].values
roc_auc_score(y, ypred)


```

---
---

### Using hyper-params (optuna) for Titanic Problem from json file ([Example notebook](mlmodels/example/sklearn_titanic_randomForest_example2.ipynb), [JSON file](mlmodels/example/hyper_titanic_randomForest.json))

#### Import library and functions
```python
# import library
from mlmodels.models import module_load
from mlmodels.optim import optim
from mlmodels.util import params_json_load


#### Load model and data definitions from json

###  hypermodel_pars, model_pars, ....
model_uri   = "model_sklearn.sklearn.py"
config_path = path_norm( 'example/hyper_titanic_randomForest.json'  )
config_mode = "test"  ### test/prod



#### Model Parameters
hypermodel_pars, model_pars, data_pars, compute_pars, out_pars = params_json_load(config_path, config_mode= config_mode)
print( hypermodel_pars, model_pars, data_pars, compute_pars, out_pars)


module            =  module_load( model_uri= model_uri )                      
model_pars_update = optim(
    model_uri       = model_uri,
    hypermodel_pars = hypermodel_pars,
    model_pars      = model_pars,
    data_pars       = data_pars,
    compute_pars    = compute_pars,
    out_pars        = out_pars
)


#### Load Parameters and Train
model         =  module.Model(model_pars=model_pars_update, data_pars=data_pars, compute_pars=compute_pars)y
model, sess   =  module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)

#### Check inference
ypred         = module.predict(model,  data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)     # predict pipeline
ypred


#### Check metrics
import pandas as pd
from sklearn.metrics import roc_auc_score

y = pd.read_csv( path_norm('dataset/tabular/titanic_train_preprocessed.csv') )
y = y['Survived'].values
roc_auc_score(y, ypred)
```


---

### Using LightGBM for Titanic Problem from json file ([Example notebook](mlmodels/example/model_lightgbm.ipynb), [JSON file](mlmodels/example/lightgbm_titanic.json))

#### Import library and functions
```python
# import library
import mlmodels
from mlmodels.models import module_load
from mlmodels.util import path_norm_dict, path_norm
import json

#### Load model and data definitions from json
# Model defination
model_uri    = "model_sklearn.model_lightgbm.py"
module        =  module_load( model_uri= model_uri)

# Path to JSON
data_path = '../dataset/json/lightgbm_titanic.json'  

# Model Parameters
pars = json.load(open( data_path , mode='r'))
for key, pdict in  pars.items() :
  globals()[key] = path_norm_dict( pdict   )   ###Normalize path

#### Load Parameters and Train
model = module.Model(model_pars, data_pars, compute_pars) # create model instance
model, session = module.fit(model, data_pars, compute_pars, out_pars) # fit model


#### Check inference
ypred       = module.predict(model,  data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)     # get predictions
ypred


#### Check metrics
metrics_val = module.fit_metrics(model, data_pars, compute_pars, out_pars)
metrics_val 

```

---


### Using Vision CNN RESNET18 for MNIST dataset  ([Example notebook](mlmodels/example/model_restnet18.ipynb), [JSON file](mlmodels/model_tch/torchhub_cnn.json))

```python
# import library
import mlmodels
from mlmodels.models import module_load
from mlmodels.util import path_norm_dict, path_norm, params_json_load
import json


#### Model URI and Config JSON
model_uri   = "model_tch.torchhub.py"
config_path = path_norm( 'model_tch/torchhub_cnn.json'  )
config_mode = "test"  ### test/prod


#### Model Parameters
hypermodel_pars, model_pars, data_pars, compute_pars, out_pars = params_json_load(config_path, config_mode= config_mode)
print( hypermodel_pars, model_pars, data_pars, compute_pars, out_pars)


#### Setup Model 
module         = module_load( model_uri)
model          = module.Model(model_pars, data_pars, compute_pars) 
`
#### Fit
model, session = module.fit(model, data_pars, compute_pars, out_pars)           #### fit model
metrics_val    = module.fit_metrics(model, data_pars, compute_pars, out_pars)   #### Check fit metrics
print(metrics_val)


#### Inference
ypred          = module.predict(model, session, data_pars, compute_pars, out_pars)   
print(ypred)




```
---

### Using ARMDN Time Series   ([Example notebook](mlmodels/example/model_timeseries_armdn.ipynb), [JSON file](mlmodels/model_keras/armdn.json))



```python
# import library
import mlmodels
from mlmodels.models import module_load
from mlmodels.util import path_norm_dict, path_norm, params_json_load
import json


#### Model URI and Config JSON
model_uri   = "model_keras.ardmn.py"
config_path = path_norm( 'model_keras/ardmn.json'  )
config_mode = "test"  ### test/prod




#### Model Parameters
hypermodel_pars, model_pars, data_pars, compute_pars, out_pars = params_json_load(config_path, config_mode= config_mode)
print( hypermodel_pars, model_pars, data_pars, compute_pars, out_pars)


#### Setup Model 
module         = module_load( model_uri)
model          = module.Model(model_pars, data_pars, compute_pars) 
`
#### Fit
model, session = module.fit(model, data_pars, compute_pars, out_pars)           #### fit model
metrics_val    = module.fit_metrics(model, data_pars, compute_pars, out_pars)   #### Check fit metrics
print(metrics_val)


#### Inference
ypred          = module.predict(model, session, data_pars, compute_pars, out_pars)   
print(ypred)



#### Save/Load
module.save(model, save_pars ={ 'path': out_pars['path'] +"/model/"})

model2 = module.load(load_pars ={ 'path': out_pars['path'] +"/model/"})

```
---




"""



### Packages  ####################################################
packages = ["mlmodels"] + ["mlmodels." + p for p in find_packages("mlmodels")]


### CLI Scripts  #################################################
"""
scripts = [ "mlmodels/models.py",
            "mlmodels/optim.py",
            "mlmodels/cli_mlmodels",     
            ]
"""


### CLI Scripts  #################################################   
entry_points={ 'console_scripts': [
               'ml_models = mlmodels.models:main',
               'ml_optim = mlmodels.optim:main',
               'ml_test = mlmodels.ztest:main'
              ] }


##################################################################   
setup(
    name="mlmodels",
    version=version,
    description="Generic model API, Model Zoo in Tensorflow, Keras, Pytorch, Hyperparamter search",
    keywords='Machine Learning Interface library',
    
    author="Kevin Noel",
    author_email="brookm291@gmail.com",
    url="https://github.com/arita37/mlmodels",
    
    install_requires=install_requires,
    python_requires='>=3.6',
    
    packages=packages,
    
    entry_points= entry_points,
    
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,

    classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: ' +
          'Artificial Intelligence',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: ' +
          'Python Modules',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
      ]
)





################################################################################
################################################################################
"""


https://packaging.python.org/tutorials/packaging-projects/


import io
import os
import subprocess
import sys

from setuptools import setup, find_packages

root = os.path.abspath(os.path.dirname(__file__))


# required packages for NLP Architect
with open('requirements.txt') as fp:
    install_requirements = fp.readlines()

# check if GPU available
p = subprocess.Popen(['command -v nvidia-smi'], stdout=subprocess.PIPE, shell=True)
out = p.communicate()[0].decode('utf8')
gpu_available = len(out) > 0

# Tensorflow version (make sure CPU/MKL/GPU versions exist before changing)
for r in install_requirements:
    if r.startswith('tensorflow=='):
        tf_version = r.split('==')[1]

# default TF is CPU
chosen_tf = 'tensorflow=={}'.format(tf_version)
# check system is linux for MKL/GPU backends
if 'linux' in sys.platform:
    system_type = 'linux'
    tf_be = os.getenv('NLP_ARCHITECT_BE', False)
    if tf_be and 'mkl' == tf_be.lower():
        chosen_tf = 'intel-tensorflow=={}'.format(tf_version)
    elif tf_be and 'gpu' == tf_be.lower() and gpu_available:
        chosen_tf = 'tensorflow-gpu=={}'.format(tf_version)

for r in install_requirements:
    if r.startswith('tensorflow=='):
        install_requirements[install_requirements.index(r)] = chosen_tf

with open('README.md', encoding='utf8') as fp:
    long_desc = fp.read()

with io.open(os.path.join(root, 'nlp_architect', 'version.py'), encoding='utf8') as f:
    version_f = {}
    exec(f.read(), version_f)
    version = version_f['NLP_ARCHITECT_VERSION']

setup(name='nlp-architect',
      version=version,
      description='Intel AI Lab\'s open-source NLP and NLU research library',
      long_description=long_desc,
      long_description_content_type='text/markdown',
      keywords='NLP NLU deep learning natural language processing tensorflow keras dynet',
      author='Intel AI Lab',
      packages=find_packages(exclude=['tests.*', 'tests', '*.tests', '*.tests.*',
                                      'examples.*', 'examples', '*.examples', '*.examples.*']),
      install_requires=install_requirements,
      scripts=['nlp_architect/nlp_architect'],
      include_package_data=True,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: ' +
          'Artificial Intelligence',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: ' +
          'Python Modules',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
      ]
      )



import os
from io import open

from setuptools import find_packages, setup

packages = ['elfi'] + ['elfi.' + p for p in find_packages('elfi')]

# include C++ examples
package_data = {'elfi.examples': ['cpp/Makefile', 'cpp/*.txt', 'cpp/*.cpp']}

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

optionals = {'doc': ['Sphinx'], 'graphviz': ['graphviz>=0.7.1']}

# read version number
__version__ = open('elfi/__init__.py').readlines()[-1].split(' ')[-1].strip().strip("'\"")

setup(
    name='elfi',
    keywords='abc likelihood-free statistics',
    packages=packages,
    package_data=package_data,
    version=__version__,
    author='ELFI authors',
    author_email='elfi-support@hiit.fi',
    url='http://elfi.readthedocs.io',
    install_requires=requirements,
    extras_require=optionals,
    description='ELFI - Engine for Likelihood-free Inference',
    long_description=(open('docs/description.rst').read()),
    license='BSD',
    classifiers=[
        'Programming Language :: Python :: 3.5', 'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Mathematics', 'Operating System :: OS Independent',
        'Development Status :: 4 - Beta', 'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License'
    ],
    zip_safe=False)



"""
