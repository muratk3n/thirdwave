# Learning to Drive

Great [article](http://deepdriving.cs.princeton.edu/paper.pdf) on
teaching machines how to drive. With the advent of deep learning, the
first idea on teaching machines how to drive using pure vision was
supplying it data on controls (steering, break, acceleration) and
images of the outside world, in pairs. Feed it gazillions of such
data, the program will learn the relation between them and learn how
to drive. The article makes the case that might not be the best way to
learn. Image X is fed in, car (in the training data) makes right
turn. A similar image Y is fed in, car makes a left turn. What should
the machine learn in this case?

The root of the problem has to do with the idea of a function. Functions are computation - we use them all the time, to decide, to compute anything and everything. 2+2 = 4. I see something, it has wings, it flies, it's a bird.

But as scientists, modelers, we don't see all of these functions as nature keeps them hidden, so we cannot encode them easily on a machine. But DL gave us a way to approximate these functions, reverse-engineer them from data. The problem is, with the driving example mentioned, there might not be a direct function between controls and outside images. If the root of science is math, and the root of math is number theory / sets, a function is a mapping from one set to another, a one-to-one or many-to-one mapping. If image X results in left steering, similar image Y in right steering, there is no function there. 2 + 2 cannot give you 4 and 14 at the same time (3=1 being 4 is okay though). DL cannot approximate such data coming from such process, that is not a function.

I like the solution employed by the researchers - they learn distances to other cars from images, something less prone to confusing signals.

And [here](https://www.youtube.com/watch?v=cYl6DIxvnzM) is your moment of Zen...






