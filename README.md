# HATLab_REU

A collection of Python scripts that I coded during my Clemson University Humans and Technology Lab Undergrad Research Experience.

## Nutrition Data Scraping Project

### Overview

The following effort was part of a greater project to investigate if there had been a notable change in eating/dieting behavior due to the COVID-19 Pandemic. This was a project where I was the lead, and one of my roles was to develop a method of gaining caloric data from text data scraped from the MyFitnessPal Discussion Forum, **What We're Eating**.

### Code and Resources Used

**Python Version:** 3.6-3.8

**Packages:** BeautifulSoup, requests, csv, json, itertools, nltk, pandas, numpy, sklearn 

**MyFitnessPal *What We're Eating* Discussion Board:** https://community.myfitnesspal.com/en/discussion/10703170/what-were-eating/p1

**Nutritionix API:** https://developer.nutritionix.com/

### Web Scraping

First, I wrote a script to scrape the Username, Post Date, and the Post itself from the MyFitnessPal Discussion board, [**What We're Eating**](https://community.myfitnesspal.com/en/discussion/10703170/what-were-eating/p1). 

![alt text](https://github.com/MarcelinoV/HATLab_REU/blob/master/Images/web_scrape.JPG "Part 1: Code for Web-Scraper")

This is the resulting data set:

![alt text](https://github.com/MarcelinoV/HATLab_REU/blob/master/Images/mfp_34.JPG "Part 1: Data")

### NLP - Text Processing

Then, I processed the post column in the scraped data set through a [NLP Pipeline](https://github.com/MarcelinoV/HATLab_REU/blob/master/Data_Scraping_Project/Web_Scraper/scraper1.py). I used the **NLTK** library to process the text data into a more filtered format. The following is some of the top words used in the text data with their descriptive statistics:

![alt text](https://github.com/MarcelinoV/HATLab_REU/blob/master/Images/top_20_words_stats.JPG "Part 2: Top Features Snippet")

This is the resulting data set:

![alt text](https://github.com/MarcelinoV/HATLab_REU/blob/master/Images/mfp_34_proc.JPG "Part 2: Data")

### Food-to-Calorie Converter

Lastly, I used the Nutritionix API's *Natural Language for Nutrients* endpoint to create a Food-to-Calorie converter for our datasets. The idea was to: 

1. Create a word bank (set) of food words
2. loop through every word in the text data per row/user
3. Check if that word is in the food bank (i.e., if that word is a food). If it is not, skip it.
4. Use the Nutritionix API to retrieve calorie information about the detected food and store it in a list. This list will be the new calorie column.
5. Once loop is finished, attach list to new dataset.

![alt text](https://github.com/MarcelinoV/HATLab_REU/blob/master/Images/food_to_cal.JPG "Part 3: Code for Food-to_Calorie Converter")

Here is the resulting data set:

![alt text](https://github.com/MarcelinoV/HATLab_REU/blob/master/Images/mfp_34_cal.JPG "Part 3: Data")

### Productionization Ideas

One idea would be to build Flask App where user can enter text data to find the calorie summation of the foods within the text. This would also include features for processing text data or scraping more data from a page of the What We're Eating forum.
