[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/cervical-cytology-classification-using-pca/image-classification-on-sipakmed)](https://paperswithcode.com/sota/image-classification-on-sipakmed?p=cervical-cytology-classification-using-pca)

# Cervical Cytology Classification Using PCA & GWO Enhanced Deep Features Selection

Official Python Implementation of the paper titled "Cervical Cytology Classification Using PCA & GWO Enhanced Deep Features Selection"

## Requirements

To install the required dependencies run the following using the Command Prompt:

`pip install -r requirements.txt`

# Implementing the code for Cervical Cytology data

Similarly the script can be modified for extracting features from other models.

Structure the directory as follows:

```

.
+-- data
|   +-- .
|   +-- train
|   +-- val
+-- extract_features.py
+-- fitnessFUNs.py
+-- GWO.py
+-- main.py
+-- resnet50.csv
+-- selector.py
+-- solution.py
+-- transfer_functions_benchmark.py

```

To extract ResNet-50 features run the following script:

`python extract_features.py`

Run the following code for the feature set optimization:

`python main.py --num_csv 2`

Set `num_csv` to the number of features csv files you have. You will be asked to enter the names of the csv files upon executing the above code. Execute `python main.py -h` to get the details of all the available arguments.

## Citation

If this repository helps you in your research in any way, please cite our paper:

```
@article{basak2021cervical,
      title={Cervical Cytology Classification Using PCA & GWO Enhanced Deep Features Selection}, 
      author={Hritam Basak and Rohit Kundu and Sukanta Chakraborty and Nibaran Das},
      year={2021},
      eprint={2106.04919},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
