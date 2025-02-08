|| Flake8 | Regex | CodeQL |
|---|---|---|---|
Accuracy | | | |
Performance | 1210.399s (20.17332min) | 76.709s (1.27848min) | 14.195s (0.23658min) + 575.381s (9.58968min)|
Readability | Very understandable | Understandable as long as you understand negative lookahead | Very understandable |
Writability | Very easy to write | Difficult to write since we need to check indentation for the return statement, but we also need to make sure that we're not detecting the return statement of another method below. | Very easy to write |