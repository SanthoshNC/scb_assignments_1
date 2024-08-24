## Execution Step:

`python.exe .\01_scb_assignment.py` - For Windows Machines

`python 01_scb_assignment.py` - For Linux / Mac Machines

#### Given this JSON as a sample, how will you write a short script/program to process this json and store into databases
> Done. I commited the file named `01_scb_assignment.py` with the code

#### Explain selection of coding language and DB of your choice
> I selected `Python` & `MongoDB` because the data which we are using here in based out of JSON. Thus MongoDB will support these kind of unstructured data easily and I am having prior experience in writing the automation scripts using Python.

#### Given that its large set of data, how will you ensure that no records are missed when writing into the DB
> For this, I used the operation called `bulk_write` from MongoDB which will ensure the insertion of bulk records / large set of data and also I added the code to print the count of inserted records for the confirmation.

#### In the case of duplicate entries, how will you handle them?
> In this provided JSON file, there is no definite unique field to serve as a logical primary key. MongoDB automatically generated the field called `_id` to serve as the primary key. As per the given usecase, I picked `name` as the primary key and added the logic to validate the scenarios:
>  - if the name field is missing or has a None value
>  - if the first element of the name list is missing, empty, or invalid

#### Supporting Screenshots:

Python Execution:

![image](https://github.com/user-attachments/assets/1802722f-228b-4dda-b5a3-ee855993b76d)

MongoDB Compass Screenshot:

![image](https://github.com/user-attachments/assets/214969e2-ef9b-4b15-8df9-1bde42d677b1)
