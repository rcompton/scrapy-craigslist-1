scrapy-craigslist
=================
This is a [Scrapy](http://scrapy.org/) project that allows for configurable crawling of Craigslist for ads that match certain keywords. It is nowhere near complete.

Use cases:

 * Watch for all apartments in `Pittsburgh` that allow dogs.
 * Watch for `Atari 2600` in `for sale/electronics` and `For Sale/computers` in `all US cities`.
 * Watch for jobs with keywords `python` and `developer` in `Pennsylvania`, `Ohio`, `Maryland` and `New York` posted within the `last 7 days`.

Other features:

 * Ability to search once or monitor daily
 * Generate email reports
 * Parse tags for exact info when available


In the far future, I'd like to incorporate some sort of anti-spam/autocorrect feature with NLTK, prioritize results ala every other search feature out there, and perhaps integrate with Solr or ElasticSearch.
