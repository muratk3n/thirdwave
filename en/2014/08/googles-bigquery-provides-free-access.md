# Google’s BigQuery Provides Free Access to GDELT

We blogged about GDELT before. This is awesome news.  Hats off to
Google.

Another post about more details of technology. Anyone with Google
Cloud account can try this out (free to sign-up). I just did and ran
this query:

```
SELECT count(1) FROM [gdelt-bq:full.events]
```

Received result

`266301241`

Cool.













