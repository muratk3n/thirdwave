# Analytical Shortcuts

A lot of mathematical modeling is really about being smart about the algebraic statements, their transformations so that we do not have to compute everything.

Let's take calculating the slope of x^2 at point x=5.

We could use the brute force approach, and *start coding* right away, just *do it*, we'd come up with a numerical solution like this: We pick a step size for x, and calculate x^2 before and after steps, then get the difference and divide by step size (for the slope).

( ((5+0.01)**2) - 5**2 ) / 0.01

This gives 10.01. Right there however, we have some questions. What is the right step size? Even if we know an approximate good step size, let's count the operations the computer had to use: one addition, two exponentiation, and one division. 4 operations in total.

But Calculus gave us the derivative. The derivative works algebraically. Under the hood, it was formulated using limits, the black art of infinity; and that gave us the algebraic transformation we enjoy today. It was an algebraic shortcut, not a numerical one. And the derivative of x^2 is 2x. Let's calculate it:

2*5 = 10

In total: One operation. That is what using straight algebra gives us. Not only it is more accurate, it saves us computation time. In their modeling efforts modelers jump through many hoops, simplify, transform, hoping that with the right move, that'll make swaths of computational tasks unnecessary, and the result more accurate.

The Fourier Transform shown in the previous Wired article uses that kind of sophisticated algebra-fu. In order to reach that final statement, the inventor used many algebraic tricks such as integration, the knowledge of how cosine and sine behaves under integration so that he could reach that final, clean, concise statement. Some of these moves are ingenious, some are downright devious. G. H. Hardy was right. "[There is no other] subject in which truth plays such odd pranks. [Math] has the most elaborate and the most fascinating technique, and gives unrivalled openings for the display of sheer professional skill".








