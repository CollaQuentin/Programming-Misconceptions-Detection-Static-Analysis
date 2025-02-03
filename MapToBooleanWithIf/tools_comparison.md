|| Flake8 | Regex | CodeQL |
|---|---|---|---|
Accuracy | | | |
Performance | 2044.421s (34.07369min) | 81.442s (1.35737min) | |
Readability | If we ignore the few functions defined at the start and only look at the logic below, the checker if very understandable | The regex doesn't use any complicated logic but is quite long, which can be though to read and understand | |
Writability | A little annoying to write because of all the verifications that had to be done (Are we assigning the same variable, to **opposite** booleans ?), but no complicated logic | There's not much variation possible in the pattern, so the Regex was not that complicated to write | |