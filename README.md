# HATLab_REU

A collection of Python scripts that I coded during my Clemson University Humans and Technology Lab Undergrad Research Experience

## Nutrition Data Scraping Project

### Overview

The following effort was part of a greater project to investigate if there had been a notable change in eating/dieting behavior due to the COVID-19 Pandemic. This was a project where I was the lead, and one of my roles was to develop a method of gaining caloric data from text data scraped from the MyFitnessPal Discussion Forum, **What We're Eating**.

### Code and Resources Used

**Python Version:** 3.6-3.8

**Packages:** BeautifulSoup, request, csv, json, itertools, nltk, pandas, numpy, sklearn 

**MyFitnessPal *What We're Eating* Discussion Board:** https://community.myfitnesspal.com/en/discussion/10703170/what-were-eating/p1

### Web Scraping

First, I wrote a script to scrape the Username, Post Date, and the Post itself from the MyFitnessPal Discussion board, [**What We're Eating**](https://community.myfitnesspal.com/en/discussion/10703170/what-were-eating/p1). 

![alt text](https://github.com/MarcelinoV/HATLab_REU/blob/master/Images/web_scrape.JPG "Part 1: Web-Scraper")

This is the resulting data set:

![alt text](https://github.com/MarcelinoV/HATLab_REU/blob/master/Images/mfp_34.JPG "Part 1: Data")

### NLP - Text Processing

Then, I processed the post column in the scraped data set through a [NLP Pipeline](https://github.com/MarcelinoV/HATLab_REU/blob/master/Data_Scraping_Project/Web_Scraper/scraper1.py). I used the **NLTK** library to process the text data into a more filtered format. The following is some of the top words used in the text data with their descriptive statistics:

![alt text](https://github.com/MarcelinoV/HATLab_REU/blob/master/Images/top_20_words_stats.JPG "Part 2: Top Features Snippet")

### Food-to-Calorie Converter



### Productionization Ideas
