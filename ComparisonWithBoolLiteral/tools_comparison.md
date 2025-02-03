|| Flake8 | Regex | CodeQL |
|---|---|---|---|
Accuracy | | | |
Performance | 1893.390s (31.55649min) | 92.905s (1.54842min) | 16.495s (0.27492min) |
Readability | Left and right side of a comparison are not analyzed the same way (`node.left` vs `node.comparators`), which can seem weird when looking at the checker, but still understandable nonetheless | Readable for a Regex. It would have been a little clearer to have two different patterns (one for the bool literal on the left side, and one for the bool literal on the right side). | Readable |
Writability | Very easy | Very easy | Required the use of the "any" (`_`) character, which requires some knowledge of CodeQL, but far from the worse checker to implement |