---
layout: single
title: "Winter 2018"
permalink: /quantLabWinter2018/
comments: true
author_profile: false
toc: true
sidebar:
    nav: "docs"
---
### Meeting agenda

### Apr 6, 2018 

1. [Fermi Question](../fermi)

2. SecurityManager, a simple Java8 app. Requires [bonds.txt](../bonds.txt)


### Mar 23, 2018

1. [Fermi Question](../fermi): What number of US dollar coins would you have to lay on the surface area of Manhattan in order to fully cover it?

2. A simple game of cards: problem 8.21 from [Quant Technical Interview Questions](https://pbenson.github.io/docs/quantTechnicalQuestions/quantTechnicalQuestions.pdf).

3. More Java collections: [Maps](https://www.hackerrank.com/challenges/phone-book/problem"), and [HashSets](https://www.hackerrank.com/challenges/java-hashset/problem).

4. Coming up next: Java [interfaces](https://www.hackerrank.com/challenges/java-interface/problem), [generics](https://www.hackerrank.com/challenges/java-generics/problem)

5. Market Review: Trump announced "first of many" [tariffs](https://www.bloomberg.com/news/articles/2018-03-22/keep-an-eye-on-these-assets-as-china-tariff-saga-unfolds), [China responded](https://www.bloomberg.com/news/articles/2018-03-22/trump-orders-50-billion-hit-on-china-goods-amid-trade-war-fears). How will this effect the markets?


### Mar 9, 2018

1. [Fermi Question](../fermi): what is 4 to the 435th (as a power of ten)?

2. Friends flipping coins, problem 3.21 from [Quant Technical Interview Questions](https://pbenson.github.io/docs/quantTechnicalQuestions/quantTechnicalQuestions.pdf). If you need to install Java and Eclipse, see last meeting's instructions.

3. Some important Java collections: Lists. See [HRList](https://github.com/pbenson/Quant-java/tree/master/eclipse-workspace) for source. [Maps](https://www.hackerrank.com/challenges/phone-book/problem), and [HashSets](https://www.hackerrank.com/challenges/java-hashset/problem). Along the way, learn a little bit about Java interfaces.

4. Market Review


### Feb 16, 2018
1. [Fermi Question](../fermi): what is the weight of a bowling ball, measured in drops of water?

2. Introduction to Java and Eclipse.
- You may need to install the [JDK (Java Development Kit)](http://www.oracle.com/technetwork/java/javase/downloads/index.html).
- Install the latest version [Eclipse](https://eclipse.org/downloads/packages/eclipse-ide-java-developers/oxygen2).
- Workflow for beginning of any project: Create Java Project, create package, create first class (e.g. HelloWorld).

3. [HackerRank Java Intro](https://www.hackerrank.com/domains/java/java-introduction) reading via [Scanner](https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/problem).

4. We implement the Alex and Beth Coin flipping problem from last week in both [Python](https://github.com/pbenson/Quant-python) and [Java](https://github.com/pbenson/Quant-java), and compare the implementations.

5. Market Review


### Feb 9, 2018

1. A question from [Fermi Questions](../fermi).

2. Alex and Beth are flipping coins. See problem 3.20 from [Quant interview book](https://pbenson.github.io/docs/quantTechnicalQuestions/quantTechnicalQuestions.pdf).

3. Counting rectangles: [Project Euler problem 85](https://projecteuler.net/problem=85).

4. Market Review


### Feb 2, 2018
1. A question from [Fermi Questions](../fermi).
2. Imagine it's snowing...see problem 13 from the [Quant interview book](https://pbenson.github.io/docs/quantTechnicalQuestions/quantTechnicalQuestions.pdf).
3. Coding warmup: Sometimes, you just need more precision. Try [Project Euler problem 80](https://projecteuler.net/problem=80). But before you code it, put on your Fermi hat, and estimate the answer.
4. A wrap-up on what we wrote last week for [tranched credit indices](https://github.com/pbenson/Quant-python/tree/master/CreditTranches).
5. Market Report. How did [Tesla raise money](https://www.bloomberg.com/news/articles/2018-01-31/when-it-comes-to-tesla-car-bonds-buyers-simply-can-t-get-enough) this past week?


### Jan 26, 2018

1. Brainteasers: How many footballs are needed to fill Michigan Stadium? How many cows are in Mexico? How much of the water from [Archimedes' famous bath](http://archimedespalimpsest.org/images/kaltoon/) is in my coffee? Practice using [Fermi Questions](../fermi).

2. Coding warmup: [Project Euler problem 81](https://projecteuler.net/problem=81). Does this look familiar?

3. We've spent a couple of weeks talking about modeling a set of variables that are jointly normal with identical pairwise correlation, and we built a simulation of it. Let's use it to build a simple tranched credit index. For more depth on tranched credit indices, see this [BIS article](https://www.bis.org/publ/qtrpdf/r_qt0503g.pdf) or this more entertaining [FT report](https://ftalphaville.ft.com/2012/05/16/1002861/recap-and-tranche-primer/) (requires free signup with Alphaville). And here is the code we wrote for [tranched credit indices](https://github.com/pbenson/Quant-python/tree/master/CreditTranches)

4. Market Report. What did Mnuchin and Trump say about the dollar? And is it [time to sell stock](https://www.bloomberg.com/news/articles/2018-01-26/biggest-sell-signal-for-stocks-since-2013-hit-with-record-inflow)?


### Jan 19, 2018

1. Warmup: [Project Euler problem 50](https://projecteuler.net/problem=50). Solution is [here](https://github.com/pbenson/Quant-python/tree/master/ProjectEuler).

2. Recall the problem from last time: We built a simulation of n correlated assets, and via [Monte Carlo simulation in Python](https://github.com/pbenson/Quant-python/tree/master/SharedCorrelation), we found an empirical distribution of the number of assets that had negative return. Why is the number of assets that have positive return uniformly distributed? Try to figure it out on your own. But if you must, solution is [here](../docs/rmj4q05.pdf), starting on page 3.

3. Market Report.


### Jan 5, 2018

1. Wrap up Python implementation of the bag with 3 red, and 3 black marbles (see [previous week](BlackRedMarbleSDP.JPG)). How big can you scale up your solver?

2. Student presentation: Solution to the [minmax correlation problem from Jane Street](JaneStreetCorrelationProblem.JPG)? Solutions presented by Patrick Lu and Jiahua Gu.

3. Consider problem 5.2 from the [Quant Technical Interview Questions](https://pbenson.github.io/docs/quantTechnicalQuestions/quantTechnicalQuestions.pdf). We built a simulation of n correlated assets, and via Monte Carlo simulation in Python, we found an empirical distribution of the number of assets that had negative return. Challenge for next time: explain the distribution for the case where pairwise asset correlation is 0.5.

4. Market Report: Bitcoin continues to be in the news.
