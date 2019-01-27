---
layout: single
title: "Fall 2018"
permalink: /quantLabFall2018/
comments: true
author_profile: false
toc: true
sidebar:
    nav: "docs"
---
### Meeting agenda

### 2018-11-16 (last meeting of 2018)

1. [Fermi Problem](../fermi): A classic...you travel back in time to 1 bya (billion years ago)n with a one liter bottle. You fill the bottle with water from the ocean, and dump it out. Then you return to the present day, and buy a liter of water. How many molecules in your purchased liter are from the liter you poured into the ocean?

2. Brainteaser: you must select a random byte from a data stream of unknown size, but too large to store. How do you do it?

3. Probability problem: You flip a coin 101 times, and a friend then flips the coin 100 times. What is the probability you flipped more heads?

4. This week [in the markets](https://www.bloomberg.com). Watch [the yield curve](https://www.bloomberg.com/news/articles/2018-11-16/don-t-take-your-eyes-off-the-yield-curve).
5. Yield curve bootstrapping recap. For more information, read [Hagan and West](../docs/HaganWest.pdf).
6. Recreational math and computing with numpy. Watch [graphing a times table on a circle](https://www.youtube.com/watch?v=qhbuKbxJsk8).


### 2018-11-09
1. Warmup: You flip a fair coin 100 times. What is the probability you flip an even number of heads? Prove your answer.
2. [Fermi Problem](../fermi): How many tires are sold in the US per year?
3. [Fermi Problem](../fermi): How much does the average taxpayer pay in interest on US Debt? [US Debt Clock](http://www.usdebtclock.org)
4. Discussion of [US Treasury auctions](https://www.treasurydirect.gov/indiv/products/prod_auctions_glance.htm).
5. This week [in the markets](https://www.bloomberg.com).
6. Last time, we learned about pulling US Treasury interest rates into `pandas`. Now, we will use that data to build the instantaneous forward rate curve, and generate the yield curve. Start with [this template](../notebooks/Building a yield curve (short end)-template.ipynb).

### 2018-11-02 No meeting

### 2018-10-26
1. Warmup: You have a coin, and you don’t know if it is fair. How can you use the coin to emulate a fair coin?
2. [Fermi Problem](../fermi): How many US dollar coins would you have to lay on the surface area of Manhattan in order to fully cover it?
3. This week in the markets. [Is it Trump](https://www.bloomberg.com/opinion/articles/2018-10-26/trump-is-bad-for-the-stock-market?srnd=premium)? Or [the Fed](https://www.bloomberg.com/news/articles/2018-10-11/trump-escalates-fed-assault-laments-high-rate-he-s-paying)? [FAANG](https://www.bloomberg.com/news/articles/2018-10-26/forget-about-zuckerberg-and-cook-bailing-us-out-taking-stock?srnd=premium)? How about [China](https://www.bloomberg.com/news/articles/2018-10-26/here-are-the-reasons-china-s-equity-rout-is-getting-even-worse?srnd=premium)?
4. Quantopian uses numerous data sources, including quandl. Quandl has an API that takes advantange of numpy and pandas. Launch jupyter, and open a copy of the [Intro to quandl and iexfinance-template notebook](../notebooks/Intro to quandl and iexfinance-template.ipynb)

### 2018-10-19
1. Introduction to Quantopian. Familiarization with research notebooks and online help.
2. All sample tatistics fromhave sample bias, and we would like to have a window around our statistic with a probability that the actual value of the statistic. As an example, we complete the notebook exercises given in [Noise in sample correlations](https://www.quantopian.com/posts/noise-in-sample-correlations)

### 2018-10-05
1. Homework: Let U be standard uniform. Given n observations of U, what is the distribution of the kth order statistic?
2. Homework: Given X with distribution function F, show that F(X) is uniform
3. Homework: Now that you’ve built a single stock historical simulation in a spreadsheet, build the same thing in Python (problem 2.22 in the primer).
4. Historical simulation of multiple stocks.
5. Monte Carlo portfolio simulation.


### 2018-09-28
- Pick up where we left off on page 6 of [Risk Management Primer](../docs/RiskManagementPrimer.pdf)
- Advertisement for Cubist Systematic Strategies
    - [Machine Learning Researcher Intern](https://careers.point72.com/CSJobDetail?jobName=machine-learning-researcher-intern&jobCode=CSS-0002498&retURL=/CSCareerSearch?filters=_business=cubist_experience=interns%20and%20entry%20level)
    - [Quant Monitoring Specialist](https://careers.point72.com/CSJobDetail?jobName=quant-monitoring-specialist&jobCode=CSS-0002144&retURL=/CSCareerSearch)
    - [Quantitative Researcher Intern](https://careers.point72.com/CSJobDetail?jobName=quantitative-researcher-intern&jobCode=CSS-0000570&retURL=/CSCareerSearch)
    
### 2018-09-05
1. If you haven’t already done so, install vscode (Visual Studio Code) with Anaconda. I couldn’t find a way to incrementally install it, so you can simply download and install Anaconda again. At the end of the install, it will ask you if you want to install Visual Studio Code.

2. OOP with Python using [Complex numbers as an example](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem).

3. Take a look at the [HackerRank Interview prep kit](https://www.hackerrank.com/interview/interview-preparation-kit), and in particular the [Hash Tables: Ransom note exercise](https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps). Watch the Hash Tables video (on the right side of page).

4. Read these articles to build knowledge of the market—I will be asking for summaries. [Emerging markets](https://www.bloomberg.com/opinion/articles/2018-09-03/we-may-be-facing-a-textbook-emerging-market-crisis), [Contagion](https://www.bloomberg.com/opinion/articles/2018-09-05/u-s-equity-bulls-just-say-no-to-contagion?srnd=premium), [Interest rates](https://www.marketwatch.com/story/treasury-yields-steady-ahead-of-pce-inflation-data-2018-08-30), and [cryptocurrencies](https://www.bloomberg.com/news/articles/2018-09-05/bitcoin-drops-3-in-10-minutes-as-cryptocurrencies-join-selloff)
