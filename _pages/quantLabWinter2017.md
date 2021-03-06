---
layout: single
title: "Winter 2017"
permalink: /quantLabWinter2017/
comments: false
author_profile: false
toc: true
sidebar:
    nav: "docs"
---
### Meeting agenda

### March 31, 2017

1. Update as needed from [GitHub](../github). We will create a method called `writeSimulation` that can dump any number of market price simulations into a file.

2. Question 3.11 from [Quant interview book](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).

3. We'll finish with practice problems from [Project Euler](https://projecteuler.net/sign_in).


### March 24, 2017

1. Spent some time getting everybody's code base synced up via [umich-quant on GitHub](https://github.com/pbenson/umich-quant).

2. We added the Market class. A market consists of the risk factors to be simulated, with weighted returns from a specified period. A simulation of the market is generated by taking the inner product of each risk factor's returns with a market noise vector.


### March 17, 2017

1. We will complete HackerRank's [Cracking the Coding Interview](https://www.hackerrank.com/domains/tutorials/cracking-the-coding-interview): [Heaps: Find the Running Median](https://www.hackerrank.com/challenges/ctci-find-the-running-median), by implementing BaseHeap and MaxHeap, then MedianHeap. Source to date is available [on GitHub](https://github.com/pbenson/umich-quant/tree/master/python/HackerRank/Running%20Median%20Heap).

2. Update your fork of [Python implementation of multi-factor Monte Carlo](https://github.com/pbenson/umich-quant/tree/master/python/MFMC). If necessary, [download historical S&P data](https://quantquote.com/historical-stock-data) from QuantQuote, on the Free Data tab.

3. Questions 3.10 from [Quant interview book](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).


### March 10, 2017

1. An easy warmup from HackerRank: [Array Left Rotation](https://www.hackerrank.com/challenges/array-left-rotation)

2. Began HackerRank's [Cracking the Coding Interview](https://www.hackerrank.com/domains/tutorials/cracking-the-coding-interview): [Heaps: Find the Running Median](https://www.hackerrank.com/challenges/ctci-find-the-running-median). This is a very nice coding exercise: not only do you learn/review heap data structures, but it is an excellent example of polymorphism via both composition and inheritance. We got the MinHeap up and running. Next week will write BaseHeap and MaxHeap, then MedianHeap.


### Feb 24, 2017

1. Via GitHub, get the latest version of our [Python implementation of multi-factor Monte Carlo](https://github.com/pbenson/umich-quant/tree/master/python/MFMC). If necessary, [download historical S&P data](https://quantquote.com/historical-stock-data) from QuantQuote, on the Free Data tab.

2. We will add MarketUniverse and Market classes, implement simulation.

3. From HackerRank's [Cracking the Coding Interview](https://www.hackerrank.com/domains/tutorials/cracking-the-coding-interview): [Trees](https://www.hackerrank.com/challenges/ctci-is-binary-search-tree), [Ransom Notes](https://www.hackerrank.com/challenges/ctci-ransom-note), and [Contacts](https://www.hackerrank.com/challenges/ctci-contacts). If you want to better understand hash tables, watch the video that accompanies Random Notes.

4. Questions 1.10, 8.1, and 8.2 from [Quant interview book](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).


### Feb 17, 2017

1. Continue implementation of Multifactor Monte Carlo in Python.

2. Any questions about [technical interview book](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf)?


### Feb 10, 2017
To prepare:

1. Review updates to [technical interview book](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf).

2. [Install pandas](https://www.jetbrains.com/help/pycharm/2016.3/installing-uninstalling-and-upgrading-packages.html) in PyCharm if necessary.

3. [Download historical S&P data](https://quantquote.com/historical-stock-data) from QuantQuote, on the Free Data tab. Discovered via [Caltech Quantitative Finance Group](http://quant.caltech.edu/historical-stock-data.html), which has some interesting information.

4. Begin implementation of Multifactor Monte Carlo in Python.

5. One-on-one discussions to determine what you want to get from your time in the Michigan Quant Lab.
    
### January 27, 2017
To prepare:
    
1. Install [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/). We’ll be doing some Python in an IDE that has better debugging support than Jupyter.

2. Solve the BinaryTree problem from the [technical interview book](../files/quantTechnicalQuestions/quantTechnicalQuestions.pdf). You may use C++ or Python or both.

3. Do LeetCode problems 2 and 20 (some of you have already done #20).

4. Be able to explain why the sum of IES is equal to ES.

5. We discovered that our C++ code for Monte Carlo does not react gracefully to an invalid name for a MarketFactor ("APL" is unknown). A better way to deal with this is through [exceptions](http://stackoverflow.com/questions/8480640/how-to-throw-a-c-exception).

6. Carlo Acerbi of MSCI presented on [Backtesting expected shortfall](../files/Readings/GeneralPropertiesOfBacktestableStatistics.pdf).