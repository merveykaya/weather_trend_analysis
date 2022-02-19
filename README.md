# Weather Trends Analysis
## Summary
In this project, you will analyze local and global temperature data and compare the temperature trends where you live to overall global temperature trends.

## Instructions
* Your goal will be to create a visualization and prepare a write up describing the similarities and differences between global temperature trends and temperature trends in the closest big city to where you live. To do this, you’ll follow the steps below:

* Extract the data from the database. There's a workspace in the previous section that is connected to a database. You’ll need to export the temperature data for the world as well as for the closest big city to where you live. You can find a list of cities and countries in the city_list table. To interact with the database, you'll need to write a SQL query.
* Write a SQL query to extract the city level data. Export to CSV.
* Write a SQL query to extract the global data. Export to CSV.
* Open up the CSV in whatever tool you feel most comfortable using. We suggest using Excel or Google sheets, but you are welcome to use another tool, such as Python or R. -- I used Python.
* Create a line chart that compares your city’s temperatures with the global temperatures. Make sure to plot the moving average rather than the yearly averages in order to smooth out the lines, making trends more observable (the last concept in the previous lesson goes over how to do this in a spreadsheet).
* Make observations about the similarities and differences between the world averages and your city’s averages, as well as overall trends. Here are some questions to get you started.
> Is your city hotter or cooler on average compared to the global average? Has the difference been consistent over time?
> “How do the changes in your city’s temperatures over time compare to the changes in the global average?”
> What does the overall trend look like? Is the world getting hotter or cooler? Has the trend been consistent over the last few hundred years?

# Getting Started

StackEdit stores your files in your browser, which means all your files are automatically saved locally and are accessible **offline!**

## System Requirements
* Operating System: MacOS Monterey

## Prerequisite
*  You need to install [brew](https://brew.sh/)  package manager. 
	* Install [Miniconda](https://formulae.brew.sh/cask/miniconda) package to use `conda` Command Line Interface (CLI).
	* Install [Anaconda](https://formulae.brew.sh/cask/anaconda) package to use Graphical User Interface (GUI).

Open your `iterm` application by a spotlight search shortcut `cmd + space`. Then, type the following commands seperately in each conversation window in terminal.
```bash
cd /path/to/directory
jupyter notebook
```
