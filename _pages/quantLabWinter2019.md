---
layout: single
title: "Michigan Quant Lab"
permalink: /quantLabWinter2019/
comments: true
author_profile: false
toc: true
sidebar:
    nav: "docs"
---
For Winter 2019, we will meet on Fridays, 10-11:20am in 110 Weiser Hall.

### Meeting agenda

### 2019-04-19
1. **Quant Interview Questions**
- I guessed $3$ natural numbers - $x,y,z$. You can ask me $2$ sums of these numbers with any integer coefficients - $(a,b,c)$. That is, you give me $a, b, \textrm{and } c$ and I tell you the result of the expression $ax+by+cz$. Seeing the answer, you then give me the $2$-nd triplet of $(a,b,c)$ and I will tell you $ax+by+cz$. Give me an algorithm to find $x,y$ and $z$.
 
2. [Market report](https://drive.google.com/open?id=1o8PeSkgVwssWBqNZ2EJE6kacm9znOFfn)

3. **Jane Street Puzzle April 2019**:
  - What is Sudoku? Let's walk through a brief [Sudoku Intro](https://www.sudokukingdom.com/very-easy-sudoku.php)
  - Check out the [Jane Street puzzle](https://www.janestreet.com/puzzles/current-puzzle/)
  - Download the python file for Sudoku solver [sudoku.py](https://drive.google.com/open?id=1cyvr1cDfU1_zix4gDvbHnors6Soxrk3z), [Sudoku Solution]()
  - Below you can find a good explanation of this algorithm!
{% include video id="JzONv5kaPJM" provider="youtube" %}


### 2019-04-05
1. **Quant Interview Questions**
- Let $X$ and $Y$ be two standard independent normal variables, i.e., $X \sim N(0,1)$, $Y \sim N(0,1)$ and $\rho(X,Y)=-0.72$. Calculate $E[3X+Y \vert X-Y=1]$ 
- Suppose the current price of a stock 100. The price has probability 70% of increasing to 110 and probability 30% of declining to 90 in one year. Assume the risk-free rate is 5%. Calculate the value of a call option struck at 100 that matures in one year to four decimal places. 
- There are $3$ random variables $X, Y$ and $Z$. The correlation between $X$ and $Y$ is $0.8$ and correlation between $X$ and $Z$ is $0.5$. Calculate the minimum correlation between $Y$ and $Z$, to four decimal places.
 
2. [Market report](https://drive.google.com/file/d/0B1TpyFCyvQuGX3BHRnNkNS0tNWFIWEJiRHRCQXY4R3lfNkF3/view?usp=sharing)

3. **Data Incubator Questions (Section 2)**:
  - Download the jupyter notebook [Data Incubator 2](https://nbviewer.jupyter.org/github/israeldi/friday-workshop/blob/master/files/Data%20Incubator/data_incubator_challenge.ipynb) and answer the questions accordingly. [Solution 2]()
  

### 2019-03-29
1. **Quant Interview Questions**
- What is the probability of a flush in Poker (i.e. All $5$ cards have the same suit)?
- A company hosts a dinner for mothers with at least one son. If Mrs. Tang  has two children, what is the probability that she has two boys?
- There are 20 balls numbered 1-20. Suppose we draw 5 of them (with replacement). ***1.*** What is the probability that all $5$ balls are in strictly increasing order (i.e. $5, 7, 14, 16, 19$)? ***2.*** What about the probability that all $5$ balls are in non-decreasing order? **Note:** This problem is more difficult. For a hint, consider the sequences with $2$ balls that are the same and count how many ways this can happen. Then proceed to calculate the number of ways you can have $3$ balls all the same and so on.

2. [Market report](https://drive.google.com/open?id=1Epj5Wh4SgM3Qh0xw1Pm2R20XjvbewRl9)

3. **Data Incubator Questions (Section 1)**:
  - Download the jupyter notebook [Data Incubator 1](https://nbviewer.jupyter.org/github/israeldi/friday-workshop/blob/master/files/Data%20Incubator/data_incubator_challenge.ipynb) and answer the questions accordingly. [Solution 1](https://nbviewer.jupyter.org/github/israeldi/friday-workshop/blob/master/files/Data%20Incubator/Section%201%20-%20The%20New%20York%20City%20Fire%20Department%20Solutions.ipynb)


### 2019-03-22
1. **Quant Interview Questions**
- Assume Black-Scholes model. Suppose the stock price $S_0 = 100$. The interest rate is $5$% per year. Consider a one-year European call option struck at-the-money. If the volatility is $\sigma = 0$, what is the call worth? What is its replicating strategy?
- Assume a Black-Scholes with no dividends. Consider a standard European call struck at-the-money with one year to maturity. If the interest rate is $r = 0.06$, is the option's delta greater or less than $0.5$? What does it depend on?
- Two standard options have exactly the same features, except that one has long maturity, and the other has short maturity. Which one has the higher gamma?

2. [Market report](https://drive.google.com/open?id=1lxRv4fUasbsgDnAK3cre2_3LtoSLaOJX)

3. Finish SQL exercises from last week:
  - SQL lecture [presentation](https://jbhender.github.io/Stats506/F18/Intro_to_SQL.html) from Stats 506
  - [SQL Exercises](https://drive.google.com/file/d/17wOqwUBZIrp_CuQEEcnGBUI8gP7nAlwB/view?usp=sharing), [SQL Solutions](https://drive.google.com/open?id=1uk8tcs-4t2zkifx7v9cVszXZTkKTwqlU)


### 2019-03-15
1. **Brainteaser**
- How can I get the answer $24$ by only using the numbers $8, 8, 3$ and $3$. You can use add, subtract, multiply, divide, and parentheses.

2. **Quant Interview Questions**
- Compute $E[e^{W_t}]$ for Brownian Motion $W_t$ when $t = 2$
- Compute $Var[(W_t - W_s)^2]$ for Brownian Motion $W_t$.
- Let $X_t$ be the price of a share of IBM stock, $t$ years from the present. Assume that $X_t$ follows a geometric Brownian motion with parameters, $r = 0.05$, $\sigma = 0.3$, and $X_0 = 100$. Find $P(X_t < 50)$ one year from now?

3. **Introduction to SQL**
  - [SQL lecture](https://jbhender.github.io/Stats506/F18/Intro_to_SQL.html) from Stats 506
  - [SQL Exercises](https://drive.google.com/file/d/17wOqwUBZIrp_CuQEEcnGBUI8gP7nAlwB/view?usp=sharing), [SQL Solutions](https://drive.google.com/open?id=1uk8tcs-4t2zkifx7v9cVszXZTkKTwqlU)

### 2019-02-22
1. Warmup problem(s):
A drunk man is at the $36$th meter of a $100$ meter long bridge. He has equal chance of staggering forward or backward $1$ meter each step. 
- What is the probability that he will make it to the end of the bridge ($100$th meter) before the beginning ($0$th meter)? 
- What is the expected number of steps he takes to either the beginning or the end of the bridge?

2. Pick up our discussion of the max subarray problem. Also look at other variates. Download the notebook [here](https://nbviewer.jupyter.org/github/dlu-umich/dlu-umich.github.io/blob/master/friday-workshop/Basic%20Data%20Structure%20%26%20Algo.ipynb).

### 2019-02-15
1. Warmup problem(s):
- **Chocolate Bars** : There is a $6$x$8$ rectangular chocolate bar made up of small $1$x$1$ bits. We want to break it into the $48$ bits. We can break one piece of chocolate horizontally or vertically, but cannot break two pieces together! What is the minimum number of breaks required?
- **Square Infection** : An infection spreads among the squares of an $n\times n$ checkerboard in the following manner. If a square has two or more infected neighbors, it becomes infected itself. (Each square has at most $4$ neighbors only!). Prove that you cannot infect the whole board if you begin with fewer than $n$ infected squares.

2. [Market report](https://drive.google.com/open?id=1TQY6seONGz4L1ALpk2x3g5QOm_WrDY_5)

3. Revisit basic data structures in Python and take a look at [algorithm problems](https://nbviewer.jupyter.org/github/dlu-umich/dlu-umich.github.io/blob/master/friday-workshop/Basic%20Data%20Structure%20%26%20Algo.ipynb): 
- **Two Sum problem** : see how selecting a good data structure help with efficiency; 
- **Maximum Sum Subarray** : develop an algo to model maximum drawdown for *AAPL*.

### 2019-02-08
1. Warmup questions:
- A & B are alternately picking balls from a bag without replacement. The bag has $k$ black balls and 1 red ball. Winner is the one who picks the red ball. Who is more likely to win, the on who starts first, or second?
- Given $X, Y, Z$ are $i.i.d.$, which is expected to be larger, $X*Y$ or $Z^2$? What is the case when they can be equal? 

2. Market Report. Is dollar ['Best of a bad bunch'](https://www.bloomberg.com/news/articles/2019-02-07/global-rate-shift-upends-wall-street-s-weaker-dollar-consensus?srnd=fixed-income)?

3. Pick up where we left with [Red & Black Marble problem](https://nbviewer.jupyter.org/github/dlu-umich/dlu-umich.github.io/blob/master/friday-workshop/RedBlackMarble-DP.ipynb).
- Recursion with cache
- Tree node as a class object
- With $n$ red/black balls, how will the initial payoff of the game grow? Any good approximation? Think about why.

### 2019-01-25

1. Warmup problem(s):
- You can roll a die up to 3 times. After each roll, you can either keep the number facing up or forgo the number and keep rolling. At the end of the 3rd roll, you will have to take the number facing up. What is it worth to play the game?

2. Python problem: There are 4 red and 4 black marbles in a bag. Draw one at time. If you have drawn more black than red, winnings are the number of black marbles in excess of red. Otherwise, you get nothing. Quit at any time.
    - Solve by hand. What is your optimal strategy?
    - Implement in Python. Verify if it matches your calculation by hand. Download the jupyter notebook [here](https://nbviewer.jupyter.org/github/dlu-umich/dlu-umich.github.io/blob/master/friday-workshop/RedBlackMarble-DP.ipynb).
    - Solve with 20 red and 20 black marbles. Does your program work? If not, what can you do about it? What is the computational complexity of your solution?
    - What if there are 1000 red and 1000 black marbles?
    - What if there are 1 million red and 1 million black marbles?


### 2019-01-11
1. Warmup problem(s):
- Solve a simple pair of equations efficiently...
- Can you cover a 10x10 board with 1x4 tiles?

2. [MSCI Internship](../jobs/MSCIQuantitativeModelValidationSummerInternship.pdf) discussion with Patrick (Di) Lu

3. Good luck to the [Bloomberg Trading Challenge](https://www.bloomberg.com/careers/blog/one-idea-engaged-250-student-teams-first-ever-bloomberg-trading-challenge/) teams:
- Prerna, Xinye, Yutian, Hui
- Rick, Israel, Jiayi, Jack, Yifei

4. IAQF competition (team entry due Friday, Jan 11th, 2019). Problem will be announced Jan 14th, 2019.
- [Competition description](../competitions/iaqf/IAQFAnnualAcademicCompetition.pdf)
- 2016 Problem: [Impact of changing oil prices](../competitions/iaqf/IAQFCompetitionProblem2016.pdf)
- 2017 Problem: [Impact of rising interest rates](../competitions/iaqf/IAQFCompetitionProblem2017.pdf)
- 2018 Problem: [Momentum vs option strategies](../competitions/iaqf/IAQFCompetitionProblem2018.pdf)
- 2019 Problem: What do you think it could be? Think-pair-share.
- [Winning papers](https://www.iaqf.org/news/news_detail/49)
5. There is a [Quantopian contest](https://www.quantopian.com/contest/university-quant-finance-competition) starting Jan 31st.
6. There are 4 red and 4 black marbles in a bag. Draw one at time. If you have drawn more black than red, winnings are the number of black marbles in excess of red. Otherwise, you get nothing. Quit at any time. What is your optimal strategy?

{% if page.comments %}
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://israeldi.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
{% endif %}
