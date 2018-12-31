# Code Your Business And .. Education

The Khan Academy is well known for its extensive library of over 2600
video lessons. It should also be known for its rapidly-growing set of
now 225 exercises — outnumbering stitches on a baseball — with close
to 2 million problems done each day.  To determine when a student has
finished a certain exercise, we award proficiency to a user who has
answered at least 10 problems in a row correctly — known as a streak.

It turns out that the streak model has serious flaws. First, if we define proficiency as your chance of getting the next problem correct being above a certain threshold, then the streak becomes a poor binary classifier. Conversations with the team led me to conceive of applying machine learning to predict the likelihood of getting the next problem correct, and use that as the basis for a new proficiency model.

---

The rest of the post is about this person's attempt to improve Khanacademy's proficiency calculation using various mathematical methods where he compares many models, and finally lands with an   one that can gauge student's success better.

Interesting thing is the thought process followed by the author is the same as any data analyst's in the business world. You could replace the word student with buyer, watching a lecture with a visit, score with conversion (?), and the article could sound like something a colleague could have written. There is data, analysis is applied to the data, and action is taken based on the data.

But since Khanacademy works in education, the contrast to the old system is much, much more painfully obvious. When KA wants to change, improve something, they dont have to wait to "educate teachers", "conforming to standards", worry about "teacher pay". They dont care about legislation, about school hours. They dont care about damn curriculums. They decide on the improvement, use their data, implement the improvement, and at the click of a button millions have access to this new feature.

From business to education to health, all services need to reorient themselves around 3W. Education bureucracy cannot stay out of that derive for change by declaring itself  an exception. 


