---
layout: single
title: "Bootcamp 2019 - Welcome!"
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

## Bootcamp agenda

### Day 1 (2 hours) Technology Bootcamp:
Here are my highly-recommended Desktop Applications for students.

#### Cloud Storages:
Cloud Storages give you the ability to access and sync your files from anywhere. This is extremely convenient if you experience problems with youor own device. 
1. Download [Google Drive](https://www.google.com/drive/download/) (Drive File Stream)
  - Unlimited Memory
  - Access to google drive account even after graduation
  - Saves Memory on yoour Laptop/Desktop
  - Access from anywhere
  - File version history
2. Download [OneDrive](https://onedrive.live.com/about/en-US/download/) (Ok option, but not recommended in the long-run).
  - Only up to 1 terabyte of Memory
  - Not as good as Google Drive
  - Pairs well with Microsoft Office
3. Others: Dropbox, Box
5. Github

#### Office 365:
Download [Office 365](https://www.microsoft.com/en-us/education/products/office)
- Comes free as a umich student and still have access after graduation
- Access to all Microsoft Office 2016 apps such as Word, Excel, Powerpoint, etc...
- Can download Office on up to 5 devices

#### Other Useful apps:
- Download [UM-VPN](https://its.umich.edu/enterprise/wifi-networks/vpn/getting-started)
- Download [LastPass](https://lastpass.com/misc_download2.php) Password Manager
- GoodNotes or Notability
- Adobe Acrobat Pro DC (PDF reader)

#### Statistical Software:
1. Download [Rstudio](https://www.rstudio.com/products/rstudio/download/)
  - Open source
  - Constantly managed
  - No need for UM credentials
2. Download [Matlab](https://www.mathworks.com/academia/tah-portal/university-of-michigan-820543.html)
  - Full access while you are a student
3. Download [Stata](https://www.stata.com/order/new/edu/gradplans/student-pricing/)
  - Get student pricing for Stata, 6 months for $48
4. Download [SAS](https://www.sas.com/en_us/software/university-edition/download-software.html)
  - SAS University Edition
  
#### iPad Apps
- GoodNotes or Notability
- LastPass
- Google Drive
- All the Microsoft Office Apps
- Handshake
- Canvas App

#### Handshake
Great for finding Job Opportunities exclusive to U of M students. 
- Create [Handshake](https://joinhandshake.com) account
  
#### Build Website
Visit [Website Tutorial](../web_kit/) from Quant Lab. 

### Day 2 (6 hours)
1. Option Pricing Discrete time
2. Binomial Tree Model

### Day 3 (5.5 hours)
1. Option Pricing Continuous Time Black Scholes
2. Python with stochastic processes brownian motion
3. **Interview Questions**
  - Warm-up: individually, solve [interview problem 8.6 (the clock problem)](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf). 
  - Warm-up: In informal teams, work on [interview problem 8.5 (the 7 boxes problem)](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).
2. Python applied to interview questions
    - As before, we will start with a stubbed notebook, `python-interview-notebook-empty.ipynb`. Save it in your Quant-python directory.
    - Solve interview problems [1.1, 3.1, 3.8, 3.10, 3.11](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf)
    - Commit your work via GitHub Desktop, and sync. Add a link to the notebook from your GitHub home page.


### Day 4 (5 hours)
1. Rstudio, Matlab
2. Interview tips
3. **Interview-Questions**
  - Warm-up: individually, solve interview problem [1.11](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).
  - Warm-up: In informal teams, work on [interview problem 3.12 (flipping two coins problem)](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).
4. In `python-interview-notebook.ipynb`, simulate the two coins problem, plot the distribution of winnings, and compute the mean.
5. Discuss the [Princeton Quant Trading Conference](http://princetonquanttrading.org) in Chicago on November 2nd.
6. Introduction to modeling market risk.


### Day 5 (4.5 hours)
1. Company Reviews
2. Vetting companies, and reviewing a Handshake/job fair company 
3. **Interview Questions**
  - Warm-up: individually, solve [interview problem 1.9](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).
  - Warm-up: In informal teams, work on [interview problem 8.15](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf) (the dark and rainy night, looking for a road).
4. Create `python-hackerrank-notebook.ipynb` in your Quant-python repo, and solve the balanced brackets problem. Push your changes to your GitHub repo.
5. Continuing to modeling market risk.
  - Create a portfolio of 100 shares of AMZN stock, and compute 5%-quantile VaR.
  - For the portfolio of 100 shares of AMZN stock, compute 5%-quantile Expected Shortfall (aka Average VaR or Conditional VaR).
  - Begin simulation of 3 stocks (AMZN, GOOG, and AAPL).


### Day 6 (3 hours)
1. Apply to at least one company of your choice on Handshake
2. **Interview Questions**
  - Warm-up: individually, solve [interview problem 3.4](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf). Compare your answer with others.
  - Warm-up: In informal teams, work on [interview problem 8.12 (37 racehorses)](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).
  - Warm-up: [individually, solve interview problem 1.7](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf). Compare your answer with others.
4. Complete 3-stock simulation.
3. Class discussion: Russell 3000 covariance matrix.
4. Back to modeling market risk.

**Part 1**
  - Simulation of 3 stocks (AMZN, GOOG, and AAPL) available for download from GitHub.
  - Create a CSV or tab-delimited file similar to your Amazon file, but add  columns for the closing prices of Google and Apple.
  - In Python, create a PriceSeries class.
  - In Python, figure out how to read the prices from your file, and create PriceSeries objects for each of the three stocks.
  - Modify your PriceSeries class so that it also caches the log returns.
  - Class discussion: How Monte Carlo (simulation of returns) is done using the RiskMetrics model.
  - Begin building simulation of the 3 stocks in Python.

**Part 2**
  - Python: Add log returns to price series.
  - Discussion: Multi-factor simulation, and EWMA.
  - Python: Create Scenario class that contains weights for returns.
  - Python: Create Position class with Price Series, and # shares.
  - Python: Create Portfolo class with positions.
  - Python: Generate 100,000 Scenarios, and simulate PnL on portfolio.