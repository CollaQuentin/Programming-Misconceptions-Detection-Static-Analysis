|| Flake8 | Regex | CodeQL |
|---|---|---|---|
Accuracy | | | |
Performance | | 48.555s (0.80925min) | 15.829s (0.26382min) + 469.053s (7.81755min) |
Readability | | Short and simple to understand | Very understandable |
Writability | | Very simple, the only particularity is that I decided not to match commas in the parenthesis (to prevent matching tuples) and other parenthesis (to prevent stuff as `return (1+2) * (3+4)`, where parenthesis around the equation are required) | Very simple to write (and possible) to write thanks to the `Value.isParenthesized()` method |