# Hello, and welcome to the first lesson of Statistics!

Today, we're going to start
* exploring collected data
* decide whether it's **categorial** or **quantitative**
* checking out some basic types of graphs, specifically bar and pie charts
* noticing and fixing misleading graphs and charts

We'll get to the specifics of the actual data collection in unit 4, but for now, lets say we already have all the data collected.
***
In our example today, we're curious whether your favorite elective class is associated with your favorite core class.

>We asked a group of students "What is your favorite class?", but then ended up forgetting to record the number that said physical education.

| Art | Music | P.E. | Foreign Language | Technology |
|------|------|------|------|------|
|6|9||4|4|

The "individuals" of a survey is just another name for our categories, classes, or independent variables.
In this situation, our individuals would be the elective classes that we got in response. These would be Art, Music, P.E., Foreign Language, and Technology.
Because we aren't measuring any numbers in the responses for our categories, this data would be considered __"categorical"__.

On the other end of the survey, the variable that we measured here is the **number** of people that gave us certain responses, which we wrote here as our second column of data. Because this is counted up and measured through values, it's considered a __"quantitative"__ variable.

***
Now, say that we remember that 30% of students chose music as their favorite elective class. We can figure out how many students overall were sampled.

Because it says that **9** students chose music, and that's **30%** of the total, we can just divide 9 by 0.3, and get a total sample size of 30.
***
Because we now know the total sample size, we can subtract all the written responses from the total.

`30-6-9-4-4`, which equals 7, so we know that 7 students responded saying P.E. is their favorite elective class.
***
Now that we know everything, we can start drawing some graphs that represent our data.

Since we have 2 variables, of different types of variables, we can use bar graphs and pie charts to display our data (among others). 

### *Bar graphs are best used for showing the value of a second variable for each categorical variable*.

### *Pie charts are best used for showing relative frequency of a quantitative variable over different categorical variables*.
***
## Now, we can start relating the elective class data with the core class data
Because we asked each student about their favorite core class as well as their favorite elective, we can make a table of all of the data.

If we place the categorial variables on either side, and then the quantitative data in the cells, we've made a two-way table. The completed table should include the totals of each row, each column, and overall.

||Math|English|Total|
|------|------|------|------|
|Art|2|4|**6**|
|Music|5|4|**9**|
|P.E.|4|3|**7**|
|Lang.|1|3|**4**|
|Tech.|4|0|**4**|
|**Total**|**16**|**14**|***30***|

From here, you can start doing operations on the data, such as finding the proportion that chose Math:

$\frac{Math\ Total}{Overall\ Total} = \frac{16}{30} = 0.5\overline3 = 53.\overline3\%$

or the proportion of students that chose Art:

$\frac{Art\ Total}{Overall\ Total} = \frac{6}{30} = 0.2 = 20\%$

or the proportion of students that chose math given that they also chose P.E.

$\frac{Math\ and\ P.E.}{P.E.\ Total} = \frac{4}{7} = 0.\overline{571428} = 57.\overline{142857}\%$

We cover these operations and the use of two-way tables more in Unit 5 (probability)

## Misleading Graphs and Charts

Sometimes, whether intentionally or unintentionally, someone can set up a graph incorrectly. This might cause confusion, or mislead the viewer into believing something else, without it technically displaying incorrect data.


For instance, a graph might use an unfair comparison, such as comparing the amount of electricity usage of the United States in 2024 (4,110,422 thousand MWh (Megawatt-hours) [according to the U.S. Energy Information Administration](https://www.eia.gov/electricity/annual/html/epa_02_02.html)) with the proposed electricity usage of the Stratos data center in Box Elder County, Utah (78,894 thousand MWh (Megawatt-hours), assuming 24/7 consumption [(utahcleanenergy.org)](https://utahcleanenergy.org/estimated-emissions-and-water-consumption-from-the-proposed-stratos-data-center/)).

This chart makes the data center's power usage appear completely negligable, because the bar for the data center is so small compared to the power usage of the United States.

To fix this graph, we can change the unfair comparison:

* Instead of comparing it to the power consumption of the entire United States, we should compare it to Utah's power consumption specifically in 2024 (all sectors). This would give us a power consumption of **34,688 MkWh** (Million Kilowatt-hours) ([U.S. Energy Information Administration](https://www.eia.gov/state/seds/sep_use/tx/pdf/use_tx_UT.pdf))
* Further, if this doesn't already make the point of the graph extremely clear, we can compare it to the industrial power usage across the state of Utah in 2024. This would give us a power consumption of **8,681 MkWh** (Million Kilowatt-hours) ([U.S. Energy Information Administration](https://www.eia.gov/state/seds/sep_use/ind/pdf/use_ind_UT.pdf))

Overall, to avoid misleading graphs, make sure to follow the following rules:

1. A good graph must compare things that should be compared
    * Don't compare unreasonable and completely unrelated datapoints
2. All vertical axes must start at 0
    * Small differences seem large when the scale doesn't start at 0
3. Be careful using images to replace the bars in a bar graph, or the slices in a pie chart
    * This can cause confusion and ambiguity as to where the bar/slice ends and becomes another



# Abstract
### Quantitative Variables
> Takes on numerical values for a measured or counted quantity

Examples:
* Average speed on a road trip
* Members in a family
* GPA
* Doors in house

### Categorical Variables
> Takes on values that are category names or group labels

Examples:
* Birth country
* Oldest sibiling's gender
* Profession
* Favorite class

### Two-way tables
||Variable 1, option x|Variable 1, option y|Total|
|------|------|------|------|
|Variable 2, option A|X and A|Y and A|**Total of A**|
|Variable 2, option B|X and B|Y and B|**Total of B**|
|**Total**|**Total of X**|**Total of Y**|***Total of all categories***|

### Misleading Graphs

Make sure that every graph meets the requirements of being a good graph:

1. Compare the right things
2. All vertical axes must start at 0
3. Be careful using images