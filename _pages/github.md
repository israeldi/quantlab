---
layout: single
title: "Github"
permalink: /github/
comments: false
author_profile: false
toc: true
sidebar:
    nav: "docs"
---
### What GitHub is for

GitHub is web-hosted source code repository that uses git. Think of it as a file system, with the ability to retrieve past versions of files. You work on local versions of the files. When you want to keep a version of files you've changed, you commit your changes, and the changes are stored in a local databse. When you want your committed changes to be stored on the web, you sync with GitHub.

### How we use GitHub

#### Writing code based on an existing repo

Most of the time we are using GitHub to support code development. There are several ways you can get this code:

### Forking and cloning
If you intend to submit your changes for inclusion in the master copy:

1. From the home page of the project you intend to fork (e.g.[umich-quant](https://github.com/pbenson/umich-quant)), click the fork button in the upper right. This creates a linked copy of the project in your personal repository.

2. Using the GitHub Desktop client, or from the home page of your newly forked repo, clone the forked repo. Now you can start coding.

3. When you are ready to submit your changes, first commit and sync. Then do a pull request from GitHub Desktop.

4. If you change your mind, and decide you don't want your changes, you can delete your local (cloned) repo, and from the website, delete the forked repo.

### Directly cloning
If you just want to get a complete copy of the code, and don't intend to submit changes to the the original repo via a pull request, then you can just directly clone the repo. From the home page of the project you intend to fork (e.g.[umich-quant](https://github.com/pbenson/umich-quant)), click the clone button in the upper right. This will direct you to GitHub Desktop.

### Copying and pasting
Often we may only be working with a couple of files. If you only want to use those files, you can copy and paste from the original repo (e.g. [umich-quant](https://github.com/pbenson/umich-quant)).

Website development

We use GitHub for maintaining personal websites (e.g. [pbenson.github.io](http://pbenson.github.io)). These websites always have URLs of the form githubusername.github.io.

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

