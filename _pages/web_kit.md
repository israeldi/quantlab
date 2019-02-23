---
layout: single
title: "Tutorial for Building your Own Site"
permalink: /web_kit/
comments: true
author_profile: false
toc: true
sidebar:
    nav: "docs"
---
### 1. Download These Files

- Link to [Repo](https://github.com/israeldi/Web_Kit)

### 2. Create your Github Page

- Follow the instructions on this [Github Guide](https://guides.github.com/features/pages/) for creating your webpage.
- Don't worry about a theme. The files we downloaded from the repo will take care of this.

### 3. Add Repo to Github Desktop (Recommended)
- [Download Github Desktop](https://desktop.github.com)
- Add your newly created github repository to Github Desktop

<figure>
  <img src="{{ '/assets/images/GitDesktop.gif' | relative_url }}" alt="adding repo to GitHub Desktop">
</figure>

### 4. Edit the `_config.yml` file
The main fields to change here are:

- ***minimal_mistakes_skin*** : This will change the color of your homepage. You have many theme options such as: "default", "air", "aqua", "contrast", "dark", "dirt", "neon", "mint", "plum", "sunrise"
- title, name, description, url, repository
- ***Site Author Section***
  - name, avatar, bio, location.
**Note:** to change your "avatar" (profile picture), this is located in the assets folder.

<figure>
  <img src="{{ '/assets/images/changeProfilePic.gif' | relative_url }}" alt="Change Profile Picture">
</figure>

### 5. Edit Your About Page
Now we can edit the contents of your page. Find the `about.md` file insde of 
the `_pages` folder. Fill this with all sorts of Markdown Language, which is exactly
the same syntax you use to edit your Jupyter Notebooks. 

<figure>
  <img src="{{ '/assets/images/editPage.gif' | relative_url }}" alt="Change Profile Picture">
</figure>

### 6. Edit Your Site's Navigation Bar
- In this case find and edit the `naviation.yml` file inside of `_data` folder.

### 7. Sample Websites
Check out these website profiles using this theme!

- [Michael Rose](https://mmistakes.github.io/minimal-mistakes/about/#) (Theme Author)
- [Israel Diego](https://israeldi.github.io) - My Webpage
- [Li Zeng](https://zenglix.github.io/About/)
- [Rafael Benevides](http://rafabene.com/about/)

### Additional

For More information and additional tips and tricks, go to [author's website](https://mmistakes.github.io/minimal-mistakes/docs/configuration/#).

