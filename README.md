# Grade Processing Tools
TA's best friends! :) 

## BSCI410 adjusted quiz score

required modules:
- `numpy`
- `argsparser`
- `sys`
- `pandas`
This script is optimized for .csv files exported from Canvas gradebook.
To obtain desired adjusted scores with the lowest quizzes scores dropped, use the following command
```
python BSCI410_adjusted_quiz_score.py \
-i {input_filename} \
-o {output_filename} \
-y {school_year} \
-t {total_of_adjusted_score} \
-n {number_of_quizzes_dropped}
```
