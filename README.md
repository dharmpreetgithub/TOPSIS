# TOPSIS Implementation 

## 1. Methodology

The project follows the workflow shown below:
Input CSV File
       ->
Input Validation
       ->
Normalization of Decision Matrix
        ->
Weighted Normalization
       ->
Determine Ideal Best & Worst
       ->
Distance Calculation
       ->
TOPSIS Score Computation
       ->
Ranking of Alternatives
       ->
Output CSV Generation


---

## 2. Description

- **Technique Used:** TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)
- **Programming Language:** Python
- **Libraries Used:** Pandas, NumPy
- **Application Type:** Command Line Program
- **Output:** CSV file containing Topsis Score and Rank
- **Validation Handling:** Included for incorrect inputs and file errors

### Project Objective

To rank multiple alternatives based on multiple criteria using the TOPSIS multi-criteria decision-making technique.

---

## 3. Input / Output

### Input (Command Line Format)


###Algorithm Explanation
Step 1: Normalize Decision Matrix

Each value is normalized using vector normalization to eliminate scale differences among criteria.

Step 2: Weighted Normalization

Each normalized value is multiplied by its corresponding weight to reflect the importance of each criterion.

Step 3: Determine Ideal Best and Ideal Worst

For each criterion:

If impact is '+', higher value is preferred.

If impact is '-', lower value is preferred.

Step 4: Calculate Separation Measures

Euclidean distance is calculated:

Distance from Ideal Best

Distance from Ideal Worst

Step 5: Compute TOPSIS Score

Score is calculated as:

Score = Distance from Worst / (Distance from Best + Distance from Worst)

Step 6: Rank Alternatives

Alternatives are ranked in descending order of TOPSIS score.
Higher score indicates better alternative.

