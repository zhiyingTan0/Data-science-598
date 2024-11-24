# COMP 598 Homework 1 – Mini Data Science Project

**Fall 2020**  
**Assigned**: September 10, 2020  
**Due**: September 18, 2020 @ 11:59 PM  

---

## Overview  

This is an **individual assignment**. Each student must complete the work independently. The goal of this assignment is to practice the data-handling phases of a mini data science project, as discussed in Unit 1 lectures. You are free to use any tools or programming languages for the tasks.

### Project Description  

Analyze tweets produced by Russian trolls during the 2016 US election. The tweets were published by [538](https://github.com/fivethirtyeight/russian-troll-tweets). This project focuses on assessing the frequency of troll tweets that mention "Trump."

---

## Steps  

### 1. **Data Collection**  

- **Download the Data**: Use the first file: [IRAhandle_tweets_1.csv](https://github.com/fivethirtyeight/russian-troll-tweets/raw/master/IRAhandle_tweets_1.csv).  
- **Filter the Data**:  
  - Use only the first **10,000 tweets**.  
  - Keep tweets that:  
    - Are in **English** (language column specifies this).  
    - Do **not** contain a question (tweets with a "?" character are excluded).  
- **Save the Filtered Data**: Create a new file in **TSV (tab-separated values)** format with the filtered tweets.

---

### 2. **Data Annotation**  

- **Add a New Feature**:  
  - Create a column `trump_mention` (Boolean, "T"/"F").  
  - A tweet mentions "Trump" if it contains the word **"Trump"** (case-sensitive).  
- **Save the Annotated Data**: Generate a new version of the dataset with this additional feature.

---

### 3. **Analysis**  

- **Compute Statistics**:  
  - Calculate the percentage of tweets that mention "Trump."  
- **Identify Counting Errors**:  
  - Analyze the annotated data to identify and explain any counting issues that result in tweets being counted more than once.

---

## Submission Instructions  

### Required Files  

1. **README.md (5 pts)**  
   - In **3 sentences or less**, explain the source of the counting problem.  

2. **dataset.tsv (20 pts)**  
   - Output from the Data Annotation phase.  
   - **Format**: Tab-separated values, UTF-8.  
   - The first line should be a **header**.  
   - Columns (in this order):  
     - `tweet_id`, `publish_date`, `content`, `trump_mention`.  
   - Tweets should maintain their original order from the source file.  

3. **results.tsv (5 pts)**  
   - **Format**: Tab-separated values.  
   - The first line should be a header with columns:  
     - `result`, `value`.  
   - The second line should provide the result for `frac-trump-mentions`. Truncate the result to **3 decimal places** if necessary.

---

### Notes  

- **Partial Credit**: You may include your code for partial credit. Ensure the code is readable in a standard text editor. Code readability and partial credit are correlated.  
- **Grading Breakdown**:  
  - **dataset.tsv**:  
    - File format (5 pts).  
    - Header line (3 pts).  
    - Correct columns and order (12 pts).  
  - **results.tsv**: 5 pts.  
  - **README.md**: 5 pts.  
