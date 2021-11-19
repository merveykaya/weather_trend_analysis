# Weather Trends Analysis

Hi ! I'm Merve Yalcinkaya. Here I will tell more about global warming and challenges to stop warming at the globe.


# Getting Started

StackEdit stores your files in your browser, which means all your files are automatically saved locally and are accessible **offline!**

## System Requirements
* Operating System: MacOS Monterey
* Model: Macbook Air M1 Chip

## Prerequisite
*  You need to install [brew](https://brew.sh/)  package manager. 
	* Install [Miniconda](https://formulae.brew.sh/cask/miniconda) package to use `conda` Command Line Interface (CLI).
	* Install [Anaconda](https://formulae.brew.sh/cask/anaconda) package to use Graphical User Interface (GUI).

Open your `iterm` application by a spotlight search shortcut `cmd + space`. Then, type the following commands seperately in each conversation window in terminal.
```bash
cd /path/to/directory
jupyter notebook
```

Use the SQL Workspace below to extract data from the temperatures database, then download the results to a CSV.

There are 3 datasets exists:  
* city_list - This contains a list of cities and countries in the database. Look through them in order to find the city nearest to you.  
* city_data - This contains the average temperatures for each city by year (ºC).  
* global_data - This contains the average global temperatures by year (ºC).

Use these SQL queries to extract:  
```sql
select * from city_data where city like 'Amsterdam%';
select * from global_data;
```