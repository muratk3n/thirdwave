# Github Pages for Math and Code

For any repo on Github, go to Settings, enable Github Pages for that
repo. Any markdsown under that repo will be published to
https://username.github.io/repo, where test.md will be accessed as
test.html. You can mark code with

\`\`\`python

code goes here

\`\`\`

and it will be colored appropriately. 

For MathJax, changes r explained [here](https://github.com/cjerdonek/gh-pages-theme-slate).
Add a`/_layouts/default.html` in root dir, copy contents of
[this](https://github.com/pages-themes/slate/blob/master/_layouts/default.html),
for MathJax add

```
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {inlineMath: [["$","$"],["\\(","\\)"]]}
  });
</script>
<script type="text/javascript"
   src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS_HTML-full">
</script>
```

in the meta. Now between `$$` or inline `$`  you can use math.

As easy as $\pi$.
