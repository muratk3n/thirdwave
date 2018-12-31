# The Mathematical Hacker

The programming profession is blessed with a number of gifted
essayists. Today I  will pick on [..] my favorites — Eric Raymond,
Paul Graham [..] — because they all seem to disagree about why (and
whether) mathematics is relevant to the practicing programmer. Their
attitudes might be summarized as:

Eric Raymond: Mathematics is unnecessary except in specialized fields
such as 3D graphics or scientific computing.

Paul Graham: Mathematics is a sort of Zen garden from which to draw
inspiration [..].

All of these views, I think, are myopic.

In a limited sense, each view is correct. If you are a systems and network programmer like Raymond, you can do your job just fine without anything more than multiplication and an occasional modulus. Graham is correct that mathematics can be a rich source of metaphors [..]

They seem to agree on one thing: from a workaday perspective, math is essentially useless. Lisp programmers (we are told) should be thankful that mathematics was used to work out the Lambda Calculus, but today mathematics is more a form of personal enlightenment than a tool for getting anything done [..].

One way to read the history of business in the twentieth century is a series of transformations whereby industries that “didn't need math” suddenly found themselves critically depending on it. Statistical quality control reinvented manufacturing; agricultural economics transformed farming; the analysis of variance revolutionized the chemical and pharmaceutical industries; linear programming changed the face of supply-chain management and logistics [..]

What is the relationship of these innovations to computer programming? Consider Eric Raymond's definition of the word hack, the great desideratum and raison d'etre of any self-respecting hacker: An incredibly good, and perhaps very time-consuming, piece of work that produces exactly what is needed. In that sense, applied mathematicians have been “hacking” industry for over a hundred years.

The computer was invented, after all, to solve math problems, not to implement compilers or word processors. The computer-aided solutions to society's problems — in engineering, mining, farming, agriculture, transportation, and defense — have provided a tremendous amount of value to society over the past seventy years. I would hazard a guess in the tens of trillions of dollars, and if you count [..] the surrender of Japan among the accomplishments of numerical computation, then the value has been immeasurable.

Yet these sorts of mathematical “hacks” are rarely mentioned by our great hacker essayists. The reason, I think, is that “hacker literature” tends to be dominated by Lisp programmers, and Lisp programmers tend to be ignorant of applied mathematics. While I am grateful that we have so many well-written essays by Lisp programmers, I think they tend to paint a skewed picture of what computer programming is and should be. One gets the impression reading Raymond, Graham, and Yegge (all self-styled Lisp hackers) that the ultimate goal of programming is to make a program that is more powerful than whatever program preceded it, usually by adding layers of abstraction. Call this the “Lisp school of programming.”

There is another school which has not been very well represented in the literature over the years, but which has undoubtedly produced a greater positive impact on the economy. Call it the “Fortran school of programming,” which I think is well summarized by Dr. Adam Rosenberg, the self-described last buffalo of industrial mathematics. Rather than viewing mathematics as an advanced tool reserved for extremely specialized computer applications, Fortran-school programmers view the
computer as an advanced tool for doing mathematics [..].In contrast to the Fortran tradition (which proudly “sent a man to the moon” and implemented critical infrastructure in banking, communications, and so on), the culture of Lisp is almost willfully ignorant of [the other culture].

To appreciate how ignorance of mathematics is actively perpetuated by Lisp culture, consider the traditional introduction to recursion in any functional-programming text. It comes in a couple of variants: calculate a Fibonacci number, or calculate a  factorial.

The usual textbook solution is recursive: one calculates the number of interest first  by calculating the number before it, and the one before that, and so on, until one reaches the “base case” with a defined solution. It is the classic didactic programming example that demonstrates the supposed utility of recursive methods.

“Advanced” discussions might consider engineering considerations such as tail-call behavior, or the possibility of memoizing results.

But rarely in these discussions will you find relevant mathematical considerations. If the goal is to compute a Fibonacci number or a factorial, the proper solution is not a recursive function, but rather knowledge of mathematics [..] No recursion (or looping) is required because an analytic solution has been available since the 17th century [..].

[N]o recursion is required as long as one knows that a factorial is actually a special case of the gamma function. (The implementation of log-gamma is usually a polynomial approximation which requires constant time to evaluate.)Despite the aesthetic virtues ascribed to functional programming, I find the preceding solutions to be more beautiful than their recursive counterparts. They run in constant (rather than linear) time, and they are easily adapted to work with non-integer inputs. More importantly, they encourage the programmer to ask and investigate the questions: why does the Fibonacci equation involve the square root of five? What does it mean to take a factorial of a fraction? These questions have fascinating answers which are not easily admitted by the recurrence relation alone. 



