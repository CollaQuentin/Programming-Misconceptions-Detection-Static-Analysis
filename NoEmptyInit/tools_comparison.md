|| Flake8 | Regex | CodeQL |
|---|---|---|---|
Accuracy | | | |
Performance | 1037.477s (17.29128min) | 59.327s (0.98878min) | 14.467s (0.24112min) |
Readability | Verifying that a statement is "useless" is a little tedious, but overall the checker is understandable | Difficult to read because of all the different kind of "useless" statements that we consider, making the regex longer. | Quite understandable, even if longer than expected |
Writability | Tedious but not complicated to implement, there's no complicated logic behind this checker. | Once again, tedious but not necessarily complicated to write. The only issue was to take in account the indentation, which is not always easy/natural using Regex. | The logic was similar to flake8, the hardest part was to understand and apply CodeQL's syntax (as it was one of my first CodeQL checker). |