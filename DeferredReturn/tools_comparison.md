|| Flake8 | Regex | CodeQL |
|---|---|---|---|
Accuracy | | | |
Performance | 1250.736s (20.84559min) | 62.653s (1.04421min) | 35.380s (0.58967min) |
Readability | Probably the less clear of the three, for each block of code we check if there's a return, and if there is one, we verify that it is the last statement in the block | Uses the indentation (through `\1`) to detect if there's something right after a `return` statement, which might not be the clearest thing, but the regex itself is not very short.| Very understandable |
Writability | | Easy to write, just look for something at the same indentation level and right after a `return` statement. | The use of `Stmt.isUnReachable()` may look great but unfortunately it matches more cases than it should, as it also matches where a condition will never be satisfied (which shouldn't be considered here). The solution proposed here was a great compromise between readability, effectiveness and writability |