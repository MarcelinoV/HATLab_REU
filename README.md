# HATLab_REU

A collection of Python scripts that I coded during my Clemson University Humans and Technology Lab Undergrad Research Experience

## Nutrition Data Scraping Project

### Overview

The following effort was part of a greater project to investigate if there had been a notable change in eating/dieting behavior due to the COVID-19 Pandemic. This was a project where I was the lead, and one of my roles was to develop a method of gaining caloric data from text data scraped from the MyFitnessPal Discussion Forum, **What We're Eating**.

### Code and Resources Used

**Python Version:** 3.6-3.8

**Packages:** BeautifulSoup, request, csv, json, itertools, nltk, pandas, numpy, sklearn 

**TwitterScraper Page:** https://github.com/taspinar/twitterscraper

**K-Means Clustering:** Making Sense of Text Data Using Unsupervised Learning: https://towardsdatascience.com/k-means-clustering-8e1e64c1561c

**Text Data Cleaning in Python | How to clean text data in python:** https://www.youtube.com/watch?v=KhXU7KOxQcg&t=4s

### Web Scraping

First, I wrote a script to scrape the Username, Post Date, and the Post itself from the MyFitnessPal Discussion board, [**What We're Eating**](https://community.myfitnesspal.com/en/discussion/10703170/what-were-eating/p1). 

![alt text](https://github.com/MarcelinoV/HATLab_REU/blob/master/Images/web_scrape.JPG "Part 1: Web-Scraper")

This is the resulting data set:

![alt text](https://github.com/MarcelinoV/HATLab_REU/blob/master/Images/mfp_34.JPG "Part 1: Data")

### NLP - Text Processing

Then, I processed the post column in the scraped data set through a [NLP Pipeline](https://github.com/MarcelinoV/HATLab_REU/blob/master/Data_Scraping_Project/Web_Scraper/scraper1.py). I used 

### Food-to-Calorie Converter

### Productionization Ideas
