# OOSA course practices and assessments

There is a separate directory for each week's work. 

## Week 1

## What's new in folder week1:
Some new .py files ***tasks*** were created based on the course 
Modified the python style of the new .py files
Aseement new script and locate mininum number ***locatemin*** ***tasks***

Week 1 covers

### x.txt
Output from ***writeFile.py*** but it had been already modified

### xycoords
Output of the ****** from fileIO

From the initial git files (some of them are modified a bit as to test different codes):
### data fileIO
Contains a text file with some sample data to practice reading with the fileIO code.
### sort
Contains an example solution for a simple sort algorithm. Note that there are multiple sort solutions, such as bubble sort, and then many more complex and efficient algorithms.


## Week 2

Week 2 covers

***Aspects***
* Using the command line to make programmable programs
* Objects and classes

***Algorithm***
* Binary search: Loop and recursion


### main

Contains an example of the main block in order to ease importing code in to other programs



### command\_line

Contains two example python files, which can be used to alter the behaviour of a program at run time. This allows you to create a single python program and then reuse it with different input files, options etc.

    commandExample.py: Minimum workable example of a command line
    commandLineIllus.py: Illustrates the common command

The options for commandLineIllus.py are:

    -h, --help            show this help message and exit
    --input INNAME        Input filename Default=test.txt
    --lat LAT             Latitude in degrees Default = 5
    --max_vcf MAXVCF      Maximum VCF value to use Default = 100
    --useSnow             Use snow switch Default = False
    -p [POW_BEAM_LIST ...], --power_beams [POW_BEAM_LIST ...] Track numbers of power beams Default = 5 and 6



### objects

Includes a script with a simple example of an object; a grouping of data and functions.


### data

Contains some text data files for use in this week's exercises.



### docu\_strings

Contains a piece of code demonstrating the suggested use of document string comments.


### binary\_search

Contains a suggested answer for week 2's algorithm. A suggested method using both looping and recursion is given.

    binarySearches.py: contains suggested answers for binary search by loop and recursion
    finishedQuartiles.py: uses the above to find quartiles in a sorted dataset
    searchObject.py: begins an object for sorting data
    makeData.py: makes data for testing algorithms
    randomWages.py: generates random wage data for testing algorithms


# Dependencies

The code in these repositories make use of the following packages and is all in python3:

    numpy
    matplotlib.pylot
    h5py
    pyproj
    gdal
    rasterio

