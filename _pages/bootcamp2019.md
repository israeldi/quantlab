---
layout: single
title: "Bootcamp 2019"
permalink: /bootcamp2019/
comments: false
author_profile: false
toc: true
sidebar:
    nav: "docs"
---
### Bootcamp agenda

### Day 1
1. **Quant Interview Questions**
- I guessed $3$ natural numbers - $x,y,z$. You can ask me $2$ sums of these numbers with any integer coefficients - $(a,b,c)$. That is, you give me $a, b, \textrm{and } c$ and I tell you the result of the expression $ax+by+cz$. Seeing the answer, you then give me the $2$-nd triplet of $(a,b,c)$ and I will tell you $ax+by+cz$. Give me an algorithm to find $x,y$ and $z$.
 
2. [Market report](https://drive.google.com/open?id=1o8PeSkgVwssWBqNZ2EJE6kacm9znOFfn)

3. **Jane Street Puzzle April 2019**:
  - What is Sudoku? Let's walk through a brief [Intro](https://www.sudokukingdom.com/very-easy-sudoku.php)
  - Check out the [Jane Street puzzle](https://www.janestreet.com/puzzles/current-puzzle/)
  - Download the python file for Sudoku solver [sudoku.py](https://drive.google.com/open?id=1cyvr1cDfU1_zix4gDvbHnors6Soxrk3z), [Solution]()
  - Below you can find a good explanation of this algorithm!
{% include video id="JzONv5kaPJM" provider="youtube" %}

### Day 2


### Day 3
a. warmup: individually, solve interview problem 8.6 (the clock problem). In informal teams, work on interview problem 8.5 (the 7 boxes problem).
b. Python applied to interview questions
  i. As before, we will start with a stubbed notebook, python-interview-notebook-empty.ipynb. Save it in your Quant-python directory.
  ii. Solve interview problems 1.1, 3.1, 3.8, 3.10, 3.11
  iii. commit your work via GitHub Desktop, and sync. Add a link to the notebook from your GitHub home page.


### Day 4
a. warmup: individually, solve interview problem 1.11.
b. In `python-interview-notebook.ipynb`, simulate the two coins problem, plot the distribution of winnings, and compute the mean.
e. warmup: In informal teams, work on interview problem 3.12 (flipping two coins problem).
d. Create a GitHub repo called cv. Add your resume to it, including a pdf version. We will look at two ways to create a link from your U of M site to your resume, using GitHub Pages, and RawGit. The important thing is that whatever method you use, your URL should take you directly to the pdf of your resume, so that we can reliably retrieve your resume via a script.
e. Discuss the Princeton Quant Trading Conference in Chicago on Oct 23rd.
f. Introduction to modeling market risk.


### Day 5
a. warmup: individually, solve interview problem 1.9.
b. warmup: In informal teams, work on interview problem 8.15 (the dark and rainy night, looking for a road).
c. Create python-hackerrank-notebook.ipynb in your Quant-python repo, and solve the balanced brackets problem. Push your changes to your GitHub repo.
Survey: are you interested in attending the Princeton Quant Trading Conference in Chicago on Oct 23rd?
Continuing to modeling market risk.
Create a portfolio of 100 shares of AMZN stock, and compute 5%-quantile VaR.
For the portfolio of 100 shares of AMZN stock, compute 5%-quantile Expected Shortfall (aka average VaR or conditional VaR).
Begin simulation of 3 stocks (AMZN, GOOG, and AAPL).


### Day 6
a. warmup: individually, solve interview problem 3.4. Compare your answer with others.
b. warmup: In informal teams, work on interview problem 3.14 (the Monte Hall problem).
c. Class discussion: Russell 3000 covariance matrix.
d. Back to modeling market risk.
  Simulation of 3 stocks (AMZN, GOOG, and AAPL)
  1. Create a CSV or tab-delimited file similar to your Amazon file, but add  columns for the closing prices of Google and Apple.
  2. In Python, create a PriceSeries class.
  3. In Python, figure out how to read the prices from your file, and create PriceSeries objects for each of the three stocks.
  4. Modify your PriceSeries class so that it also caches the log returns.
  5. Class discussion: How Monte Carlo (simulation of returns) is done using the RiskMetrics model.
  6. Begin building simulation of the 3 stocks in Python.


### Last day of boot camp!
a. The Day 6 work (ThreeStockMonteCarlo) is available for download from GitHub.
b. warmup: individually, solve interview problem 1.7. Compare your answer with others.
c. warmup: In informal teams, work on interview problem 8.12 (37 racehorses).
d. Discussion: what is your best solution to interview problem 8.15 (the dark and rainy night, looking for a road)?
e. Complete 3-stock simulation.
  i. Python: Add log returns to price series.
  ii. Discussion: Multi-factor simulation, and EWMA.
  iii. Python: Create Scenario class that contains weights for returns.
  iv. Python: Create Position class with Price Series, and # shares.
  v. Python: Create Portfolo class with positions.
  vi. Python: Generate 100,000 Scenarios, and simulate PnL on portfolio.