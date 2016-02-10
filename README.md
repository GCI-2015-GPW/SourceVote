# SourceVote

## Overview

SourceVote is a platform for voting on the best open source projects to gather collaborators. The goal is to allow smaller projects
to be discovered among the midst of large, popular projects. The popular projects tend to be more professional looking, which is an
incentive to develop a large project, making it larger, while the smaller, perhaps more useful projects can stagnate and waste away.
Ignored by the large community that might benefit from them.

## General Concept

To promote the best projects, we have developed a new system of ranking, based on the actual content that drives a programming project. 
The code and the documentation. Committing to a project is a way to increase the score of your project. To drive up smaller projects with
a growing community, the commits have a logerithmic effect. That is, the more commits a project has (say, the Linux kernel) the less it's
ranking will improve in score after more commits.

Obivously badly behaving projects, existing to fake commits will be reported and removed. 

Is a commit worth the same amount? Or what about stupid one work variable name fixes or single character fixes?

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
