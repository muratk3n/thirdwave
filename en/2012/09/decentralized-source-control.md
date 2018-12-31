# Decentralized Source Control

Previous article used some jargon that might need some explaining.

A patch is a simple text file that just contains the "difference" of one source tree (call it a directory) with another. Say I download the Linux kernel put it under a linux directory, and make a copy call it mylinux directory, make some changes under this directory (fixing a bug maybe). When I am done, using a simple tool I can compare both directories, and generate a patch file. This single file will contain all my changes. Then, I can send this file to the Linux maintainers, post it online etc, and this file, once it is "applied" to the old tree, it will bring all my changes to it.

As it's obvious, this is decentralized, asynchronous bug fixing, testing, and code improvement.

But notice there are still centralized gatekeepers. Some of that is necessary of course, but partly this behaviour is also enforced by the old-style source control tools of the past (err - old, like from 10 years ago). Source code is kept in repositories, and in the past (!) these repositories worked in client / server mode, which encourages few commiters, and read-only access to the rest (that's why a patch file was sent you see).

Newer tools like Git and Github decentralize things even further.

There isnt even a centralized repository anymore. Everyone have their own repositories on their own machines, and the overall ecosystem [1] treats each repository as a first-class citizen. When you make a change, you change your repository, when you are done, you don't send a patch, you make a pull request. Your repository is now an actor in the infosphere.

Surely there are ppl who know more about the kernel than you do, so those people will get more pull requests, their changes will be watched more closely and pulled by others even more. But technically, there is noone stopping you from continuing your own line while still remaining as first-class citizen in the infosphere.

Who created Git? Well, the author is none other than Mr. Linus Torvalds himself.

---

[1] I purposely avoided the word "system" here. The ecosystem, the overall behaviour of this new infosphere emerges from what Git allows on individual and peer-to-peer level.






