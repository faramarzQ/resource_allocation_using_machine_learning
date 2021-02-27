# Cloud_assisted_resource_allocation_using_machine_learning
A Resource allocation application using Machine learning technique Assisted by Cloud Computing implemented in Python

## 1 ***Introduction***
an application i've created based on the following paper:
"A Machine Learning Framework for Resource Allocation Assisted by Cloud Computing" which is introducing a framework to do
resource allocation using Machine learning techniques and assist cloud computing for doing the job. for more details refer to the Article. And be aware that this application is a small scale one, probably just a simulator of the real world application.

## 2 ***Data***
### 2.1 Description
as the system uses Machine learning to allocate the proper resources, we need data. But finding a prepared and clean data
for doing such thing in small scale is not much possible(unless you use Data provided by AWS or Google on massive Data centers).
So i created my own Data. The Data Creator module (Seeder module in /Cloud/storage) uses a predefined template(/Cloud/storage/data/seeder_data_template.csv) to create data. description of attributes, classes, values and ... are in the /Cloud/storage/data/data_description.txt file.

### 2.2 process
First the seeder module reads the seeder_data_template.csv file and creates a data based on it in /Cloud/storage/data/dat.csv file.
Attributes, classes and values are manipulatable but needs coding also.

### 2.3 Execution
To execute the seeder and create the data, run `python3 Cloud/storage/seeder.py`. change the '/' to '\\' in case you are using a non-unix based system.
the command outputs the data.csv file
