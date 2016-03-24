<p align="center">
  <img src="http://i.imgur.com/UJZYOnR.png" width="400px" alt="Source Vote logo"/>
</p>

## Overview

SourceVote is a platform for voting on the best open source projects to gather collaborators. The goal is to allow smaller projects
to be discovered among the midst of large, popular projects. The popular projects tend to be more professional looking, which is an
incentive to develop a large project, making it larger, while the smaller, perhaps more useful projects can stagnate and waste away.
Ignored by the large community that might benefit from them.

## General Concept

To promote the best projects, we have developed a new system of ranking, based on the actual content that drives a programming project. 
The code and the documentation. There will be a vote casting system based on which a project will be selected as a top-priority project
every two-weeks. Such a project would be featured throughout the website to gather contributors. Committing to a project is a way to 
increase the score of your project. To drive up smaller projects witha growing community, the commits have a logarithmic effect. That is, 
the more commits a project has (say, the Linux kernel) the less it's ranking will improve in score after more commits.

Bad projects existing through fake would be reported and removed.

Are all commits worth the same? What about a commit with a minor change like correcting a typo?

Well similarly to the projects with high commit counts, a commit changing many lines will be worth more, especially if
the rate of commits goes up after a large commit. This invites large changes, which might hold back smaller features to
show that a stagnent project, might actually just be waiting on someone to finish a piece, and doesn't punish the projects
for putting new features in that take a long time.

Beyond this simple ranking algorithm, a project depends on it's image and publicity. Thats why the ranking pages will be like Patreon
or Kickstarter, allowing projects to post updates, blog entries, videos and changelogs to keep the community informed. Regular users
can follow a project to keep track of what's happening with their favorite projects and see the scores change.

With a project page, the site can post what kind of contributors they're looking for, what features are important, and possibly progress on
those features. Then developers, artists, designers, documentors, and all kinds of makers who are looking for projects to work on can
connect with a project they love, even if it's not all over the internet already. Just like a job listing, only a lot more fun.

## Technologies
Website is writen in..
- Python/Django
- MySql
- AngularJS

[![Gitter](https://badges.gitter.im/GCI-2015-GPW/SourceVote.svg)](https://gitter.im/GCI-2015-GPW/SourceVote)
