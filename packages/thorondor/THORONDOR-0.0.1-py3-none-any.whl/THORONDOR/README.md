# Presentation of THORONDOR, a program for data analysis and treatment in NEXAFS

Authors : Simonne and Martini

#### The Program is meant to be imported as a python package, if you download it, please save the THORONDOR folder in ...\Anaconda3\Lib\site-packages
The installation command can be found here : https://test.pypi.org/project/THORONDOR/
There are two main classes at the core of THORONDOR:

### The class Dataset
A new instance of the Dataset class will be initialized for each Dataset saved in the data folder. This object is then saved in the list "ClassList", attribute of the second class "GUI".
For each Dataset, all the different dataframes that will be created as well as specific information e.g. $E_0$ the edge jump can be find as attributes of this class. Certain attributes are instanced directly with the class, such as:
* Name of Dataset
* Path of original dataset
* Timestamp

At the end of the data reduction, each Dataset should have at least three different data sets as attributes, saved as `pandas.DataFrame()`:
* df : Original data
* ShiftedDf : If one shifts the energy 
* ReducedDf : If one applies some background reduction or normalization method 
* ReducedDfSplines : If one applied the specific Splines background reduction and normalization method.

A Logbook entry might also be associated, under `Dataset.LogbookEntry`, this is done via the GUI, the logbook should be in the common excel formats.

It is possible to add commentaries for each Dataset by using the `Dataset.Comment()` and to specify some additional inf with the function `Dataset.AdditionalInfo()`.

Each Dataset can be retrieved by using the function Dataset.unpickle() with the path of the saved Class as an argument.

### The class GUI
This  class is a Graphical User Interface (GUI) that is meant to be used to process important amount of XAS datasets, that focus on similar energy range (same nb of points) and absorption edge.
There are two ways of initializing the procedure in a jupyter notebook:
* `GUI = THORONDOR.GUI()`; one will have to write the name of the data folder in which all his raw datasets are saved, in a .txt format.
* `GUI = THORONDOR.GUI.GetClassList(DataFolder = "<yourdatafolder>")` ;if one has already worked on a folder and wishes to retrieve his work.

This class makes extensive use of the ipywidgets and is thus meant to be used with a jupyter notebook. Additional informations are provided in the "ReadMe" tab of the GUI.

All the different attributes of this class can also be exported in a single hdf5 file using the pandas .to_hdf5 methods. They should be accessed using the read_hdf methods from pandas.

The necessary Python packages are : numpy, pandas, matplotlib, glob, errno, os, shutil, ipywidgets, IPython, scipy, datetime, importlib, pickle, lmfit, encee and inspect.

### FlowChart

![FlowChart](https://user-images.githubusercontent.com/51970962/76894984-6e65d180-688f-11ea-9649-cee5aad148ce.png)

### Screenshots of the program

![GUIShowData](https://user-images.githubusercontent.com/51970962/74930247-768c3780-53dd-11ea-9403-111a2fbd3a6d.png)

![GUIReadme](https://user-images.githubusercontent.com/51970962/74930045-1d240880-53dd-11ea-9271-aa2efbee7a3c.png)

![GUILogbook](https://user-images.githubusercontent.com/51970962/74930291-8a379e00-53dd-11ea-8aae-803c227f33f1.png)

![GUIPlot](https://user-images.githubusercontent.com/51970962/74930304-90c61580-53dd-11ea-85b7-467dfd054e06.png)

![GUIReduce](https://user-images.githubusercontent.com/51970962/74930315-97ed2380-53dd-11ea-96fb-6dbb6938ea83.png)

![SplinesReduction](https://user-images.githubusercontent.com/51970962/80730670-254da200-8b0a-11ea-9538-49a2d1a25e32.PNG)

![GUIShift](https://user-images.githubusercontent.com/51970962/74930326-9f143180-53dd-11ea-8ab3-0c7817b8af6d.png)

![GUIFit](https://user-images.githubusercontent.com/51970962/80730788-4e6e3280-8b0a-11ea-8465-6a20fa97a90c.png)


### For users on Jupyter Lab, please follow this thread : https://stackoverflow.com/questions/49542417/how-to-get-ipywidgets-working-in-jupyter-lab