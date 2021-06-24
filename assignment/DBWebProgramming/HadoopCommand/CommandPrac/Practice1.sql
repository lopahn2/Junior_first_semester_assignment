#%% Importing Relational Data with Sqoop 
#Practice: Import Data

## list the table impormations in DB
Sqoop list-tables --connect jdbc:mysql://localhost/loudacre --username training --password training

## Import table into DB
Sqoop import --connect jdbc:mysql://localhost/loudacre --username training --password training --table accounts --target-dir /loudacre/accounts

## Check imported data files in HDFS
hdfs dfs -ls /loudacre/accounts

## Where incremental data set, Find top 5 elements in table
hdfs dfs -tail /loudacre/accounts/part-m-00003

## list the contents of accounts
