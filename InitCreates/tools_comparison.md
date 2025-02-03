|| Flake8 | Regex | CodeQL |
|---|---|---|---|
Accuracy | | | |
Performance | 1137.605s (18.96008min) | 76.278s (1.27130min) | 14.526s (0.24209min) |
Readability | Easy to read | Very complicated to read : The regex is long, uses multiple negative lookahead, multiple references to previously matched group, ... | Easy to understand, as the query doesn't require the use of any kind of formula or wildcard such as `_`.|
Writability | Very easy to write | Very complicated to write, mainly because of the identation and the risk of catastrophic backatracking if the `__init__` method gets too long (which then requires some kind of optimization in the regex) | Easy to write. I decided not to very `f.isMethod()` since some exercices that I was analyzing don't require to write the signature of the class, which led to CodeQL not recognizing `__init__` as a method. |