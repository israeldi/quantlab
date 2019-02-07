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
For Winter 2019, we will meet on Fridays, 10am-11:20pm in 110 Weiser Hall.

### Meeting agenda

### 2019-02-09
1. Warmup questions:
- A & B are alternately picking balls from a bag without replacement. The bag has k black balls and 1 red ball. Winner is the one who picks the red ball. Who is more likely to win, the on who starts first, or second?
- Given X, Y, Z are i.i.d., which is expected to be larger, X*Y or Z^2? What is the case they can be equal? 

2. Market Report. Is dollar ['Best of a bad bunch'](https://www.bloomberg.com/news/articles/2019-02-07/global-rate-shift-upends-wall-street-s-weaker-dollar-consensus?srnd=fixed-income)?

3. Pick up where we left with [Red & Black Marble problem](https://nbviewer.jupyter.org/github/dlu-umich/dlu-umich.github.io/blob/master/friday-workshop/RedBlackMarble-DP.ipynb).
- Recursion with cache
- Tree node as a class object
- With n red/black balls, how will the initial payoff of the game grow? Any good approximation? Think about why.

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
