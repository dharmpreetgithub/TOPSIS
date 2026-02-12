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

```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFileName>

