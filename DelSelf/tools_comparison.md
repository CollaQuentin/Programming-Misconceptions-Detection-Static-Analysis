|| Flake8 | Regex | CodeQL |
|---|---|---|---|
Accuracy | | | |
Performance | 1135.611s (18.92684min) | 0.514s (0.00857min) | 46.726s (0.77876min) |
Readability | Very understandable | Very understandable | Maybe not the most readable query, but still seems understandable without knowing CodeQL |
Writability | Very easy to write | Very easy to write. The only "trap" was to verify that the analyzed snippet of code was not deleting an attribute (e.g : `del self.name`) instead of `self`.| Easy to write, even without using the `exists()` formula. |