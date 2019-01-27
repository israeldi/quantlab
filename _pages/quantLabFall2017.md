---
layout: single
title: "Fall 2017"
permalink: /quantLabFall2017/
comments: true
author_profile: false
toc: true
sidebar:
    nav: "docs"
---
### Meeting agenda

### Dec 1, 2017

1. Show that 1 is the only number in the sequence {1, 11, 111, 1111, ....} that is a perfect square.

2. Have you seen the minmax correlation problem from Jane Street? Looking for someone to present a solution in first January meeting.

3. Recall the problem of the bag with 3 red, and 3 black marbles (see previous week). Implement in Python. What's the strategy if there are 26 red, and 26 black (e.g. like a deck of cards)? What is there are 10,000 red?

4. Market Report: Bitcoin history, Bitcoin bubble. Is Blockchain the real story? Ongoing transformation of retail to online—where will the warehouse space come from? The US may not be able to produce as much oil as we thought. Why?


### Nov 17, 2017

1. Complete Running Median problem.

2. There is a bag with 3 red, and 3 black marbles. You draw marbles without replacement, winning a dollar if it is red, paying a dollar if black. What's your strategy?

3. Market Report: Bitcoin volatility, Bitcoin as crisis currency, Bitcoin for Square. Norway divesting oil equities.


### Nov 10, 2017

1. Continue implementation of heap in Python, and apply it to the Running Median problem.


### Nov 3, 2017

1. Getting the right data structure: Review problem (6.14) from Quant interview book.

2. What's a heap, and why do we care? We implement one in Python, and apply it to the Running Median problem.

3. Market Report: What went on at the Fed this week ? Search Yellen and Powell. What does Blankfein think about tax cuts, and why?


### Oct 27, 2017

1. Market Report: What happened with Alphabet, Amazon, and Microsoft on Thursday? What are stress tests, who cares about them, and what did a US Treasury report just recommend?

2. Two bags of marbles: Problem (8.20) from Quant interview book.

3. What would be the price of 9 year US Treasury bond with 9% coupons? We'll figure it out using zero coupon data from Quandl. Bonus: what's a perpetuity, and how would you price one?


### Oct 20, 2017

1. Market Report: Where’s the the Dow? What’s been happening to it over the past week, month, year? SP500? NASDAQ? FTSE 100? Nikkei 225? What happened to ToysRUs CDS spreads last month?

2. Discuss airplane boarding problem (8.18) from Quant interview book.

3. Monte Carlo Simulation: clone the latest code. Discuss the summability of IES (incremental expected shortfall).

4. Coherent risk measures, subadditivity, and an example of the failure of VaR to be subadditive.


### Oct 6, 2017

1. Warmup: Project Euler problems 46 and 47.

2. What's a heap?

3. Monte Carlo Simulation: clone the latest code. Calculating VaR at various quantiles shouldn't require re-sorting the PnL. We learn about lazy initialization. We apply the same thing to ES. Time permitting, we compute portfolio risk.


### Sep 29, 2017

1. Review last week's brainteaser on checkerboards, dominoes, and trominoes.

2. Coding exercise: Project Euler problems 30 and 35.

3. We will continue studying portfolio risk next week. At 9:50am, we will head over to the Tozzi Lab (Ross, room R0400) for Kai Petainen's Intro to FactSet and Bloomberg workshop, from 10am to noon. This is part of Kai's Fall series of workshops.


### Sep 22, 2017

1. Warmup: Project Euler problems 20 and 25.

2. Given the order statistics of a sample of size 10, what are the quantiles associated with each statistic? In particular, the first, and the last? We discuss some approaches to this.

3. Monte Carlo Simulation: clone the latest code. Calculating VaR at various quantiles shouldn't require re-sorting the PnL. We learn about lazy initialization. We compute expected shortfall, aka AVaR (average VaR), aka CVaR (conditional VaR).

4. Brainteaser: Checkerboards, dominoes, and trominoes.


### Sep 15, 2017

1. Monte Carlo Simulation: clone the latest code. We altered the Position object in a Portfolio keep track of its PnL, and we can calculate VaR of the position.
