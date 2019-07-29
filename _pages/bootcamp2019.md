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

<style type="text/css">
    ol { list-style-type: upper-alpha; }
</style>

### Bootcamp agenda

#### Day 1 
(2 hours) Technology Prep:
Cloud Storages:
1. Google Drive
  - Unlimited Memory
  - Access to account even after graduation
  - Saves Memory on yoour Laptop/Desktop
  - Access from anywhere
  - File version history
2. OneDrive
  - Only up to 1 terabyte
  - Not as good as Google Drive
3. Dropbox
4. Box
5. Github

Office 365 account
- Comes free as a student
- Access to Microsoft Office 2016
- Up to 1 terabyte memory

Other Useful apps:
- UMVPN
- LastPass

Statistical Software:
1. Rstudio
  - Open source
  - Constantly managed
  - No need for UM credentials
2. Matlab
  - Full access while you are a student
3. Stata
4. SAS

- Below you can find a good explanation of this algorithm!
{% include video id="JzONv5kaPJM" provider="youtube" %}

#### Day 2
1. Option Pricing Discrete time
2. Binomial Tree Model

#### Day 3
1. Option Pricing Continuous Time Black Scholes
2. Python with stochastic processes brownian motion
1. warmup: individually, solve [interview problem 8.6 (the clock problem)](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf). In informal teams, work on [interview problem 8.5 (the 7 boxes problem)](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).
2. Python applied to interview questions
    - As before, we will start with a stubbed notebook, python-interview-notebook-empty.ipynb. Save it in your Quant-python directory.
    - Solve interview problems [1.1, 3.1, 3.8, 3.10, 3.11](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf)
    - commit your work via GitHub Desktop, and sync. Add a link to the notebook from your GitHub home page.


#### Day 4
1. Rstudio, Matlab
2. Markdown, building a website
3. Interview tips

1. warmup: individually, solve interview problem [1.11](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).
2. In `python-interview-notebook.ipynb`, simulate the two coins problem, plot the distribution of winnings, and compute the mean.
3. warmup: In informal teams, work on [interview problem 3.12 (flipping two coins problem)](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).
4. Create a GitHub repo called cv. Add your resume to it, including a pdf version. We will look at two ways to create a link from your U of M site to your resume, using GitHub Pages, and RawGit. The important thing is that whatever method you use, your URL should take you directly to the pdf of your resume, so that we can reliably retrieve your resume via a script.
5. Discuss the Princeton Quant Trading Conference in Chicago on Oct 23rd.
6. Introduction to modeling market risk.


#### Day 5
1. Company Reviews
2. Vetting companies, and reviewing a Handshake/job fair company 
1. warmup: individually, solve interview problem 1.9.
2. warmup: In informal teams, work on interview problem 8.15 (the dark and rainy night, looking for a road).
3. Create python-hackerrank-notebook.ipynb in your Quant-python repo, and solve the balanced brackets problem. Push your changes to your GitHub repo.
4. Survey: are you interested in attending the Princeton Quant Trading Conference in Chicago on Oct 23rd?
5. Continuing to modeling market risk.
    - Create a portfolio of 100 shares of AMZN stock, and compute 5%-quantile VaR.
    - For the portfolio of 100 shares of AMZN stock, compute 5%-quantile Expected Shortfall (aka average VaR or conditional VaR).
    - Begin simulation of 3 stocks (AMZN, GOOG, and AAPL).


#### Day 6
1. Job Applications

1. warmup: individually, solve [interview problem 3.4](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf). Compare your answer with others.
1. warmup: In informal teams, work on [interview problem 3.14 (the Monte Hall problem)](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).
3. Class discussion: Russell 3000 covariance matrix.
4. Back to modeling market risk.
  Simulation of 3 stocks (AMZN, GOOG, and AAPL)
    - Create a CSV or tab-delimited file similar to your Amazon file, but add  columns for the closing prices of Google and Apple.
    - In Python, create a PriceSeries class.
    - In Python, figure out how to read the prices from your file, and create PriceSeries objects for each of the three stocks.
    - Modify your PriceSeries class so that it also caches the log returns.
    - Class discussion: How Monte Carlo (simulation of returns) is done using the RiskMetrics model.
    - Begin building simulation of the 3 stocks in Python.

1. The Day 6 work (ThreeStockMonteCarlo) is available for download from GitHub.
2. warmup: [individually, solve interview problem 1.7](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf). Compare your answer with others.
3. warmup: In informal teams, work on interview problem 8.12 (37 racehorses).
4. Discussion: what is your best solution to [interview problem 8.15 (the dark and rainy night, looking for a road)](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf)?
5. Complete 3-stock simulation.
  - Python: Add log returns to price series.
  - Discussion: Multi-factor simulation, and EWMA.
  - Python: Create Scenario class that contains weights for returns.
  - Python: Create Position class with Price Series, and # shares.
  - Python: Create Portfolo class with positions.
  - Python: Generate 100,000 Scenarios, and simulate PnL on portfolio.