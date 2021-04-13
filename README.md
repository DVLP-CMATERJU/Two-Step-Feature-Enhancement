# Two-Step-Feature-Selection

Official Python Implementation of the paper titled "Cervical Cytology Classification Using PCA & GWO Enhanced Deep Features Selection"

## Requirements

To install the required dependencies run the following using the Command Prompt:

`pip install -r requirements.txt`

# Implementing the code for Cervical Cytology data

Extract the deep features from the cervical cytlogy data and save the features in a csv file (without headers) where the last column contains the original labels of the data.

```

.
+-- fitnessFUNs.py
+-- GWO.py
+-- main.py
+-- resnet50.csv
+-- vgg16.csv
+-- selector.py
+-- solution.py
+-- transfer_functions_benchmark.py

```

Run the following code for the feature set optimization:

`python main.py --num_csv 2`

Set `num_csv` to the number of features csv files you have. You will be asked to enter the names of the csv files upon executing the above code. Execute `python main.py -h` to get the details of all the available arguments.

## Citation

If this repository helps you in your research in any way, please cite our paper:

```
@article{saha2021breast,
  title={Cervical Cytology Classification Using PCA \& GWO Enhanced Deep Features Selection}
  author={Basak, Hritam and Kundu, Rohit and Das, Nibaran}
}
```
