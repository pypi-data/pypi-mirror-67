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



##### Version  #######################################################################
# from setup import version, entry_points


print("start Doc")








######################################################################################
#with open("README.md", "r") as fh:
#    long_description = fh.read()


des =  """

```

ml_models --do                    
    "testall"     :  test all modules inside model_tf
    "test"        :  test a certain module inside model_tf


    "model_list"  :  #list all models in the repo          
    "fit"         :  wrap fit generic m    ethod
    "predict"     :  predict  using a pre-trained model and some data
    "generate_config"  :  generate config file from code source


ml_optim --do
  "test"      :  Test the hyperparameter optimization for a specific model
  "test_all"  :  TODO, Test all
  "search"    :  search for the best hyperparameters of a specific model

```


"""



### Packages  ####################################################
packages = ["mlmodels"] + ["mlmodels." + p for p in find_packages("mlmodels")]




####################################################################################################
def os_package_root_path(add_path="",n=0):
  from pathlib import Path
  add_path = os.path.join(Path(__file__).parent.absolute(), add_path)
  # print("os_package_root_path,check", add_path)
  return add_path


def get_recursive_files(folderPath, ext='/*model*/*.py'):
  import glob
  files = glob.glob( folderPath + ext, recursive=True) 
  return files




# Get all the model.py into folder  
folder = None
folder = os_package_root_path() if folder is None else folder
# print(folder)
module_names = get_recursive_files(folder, r'/*model*//*model*/*.py' )                       


des2 = """
```
Model list 


"""
for t in module_names :
    t = t.replace(folder, "").replace("\\", ".")

    if "__init__.py" in t  :
      des2 = des2  + "\n\n"
    else  :    
      if  not 'util' in  t and not 'preprocess' in t :
        des2 = des2 + str(t) + "\n" 

des2 = des2 + """
```

"""

   






################ Print on file
with open("README_model_list.md", mode="w") as f :
  f.writelines(des)
  f.writelines(des2)

