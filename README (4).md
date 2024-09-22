
# Drug-Drug Interaction Analysis using DDInter Data

This project analyzes drug-drug interactions (DDIs) using data from the DDInter database. The analysis includes visualizing the distribution of interaction severity, identifying the most frequent drugs involved in interactions, and understanding the severity levels associated with these drugs.

## Steps:

1. **Data Collection**: Datasets were sourced from the DDInter database, which contains comprehensive drug-drug interaction information.
2. **Data Preprocessing**: The data was cleaned and prepared for analysis.
3. **Data Visualization**: Several visualizations were created to understand drug interactions:
   - **Figure 1**: Distribution of Drug Interaction Severity Levels
   - **Figure 2**: Top 10 Most Frequent Drugs (Drug_A) Involved in Interactions
   - **Figure 3**: Distribution of Interaction Severity Levels for Top 10 Drugs (Drug_A)
4. **Conclusion**: The analysis reveals that corticosteroids and antifungals are commonly involved in drug interactions, with most interactions falling under the "Moderate" severity level.

## Requirements:

To run the analysis, you will need the following Python libraries:
- pandas
- matplotlib
- seaborn

## How to Run:

1. Clone this repository.
2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the main script:
    ```bash
    python main.py
    ```

## Files:

- **main.py**: The main script that performs the analysis and generates the figures.
- **requirements.txt**: The list of Python dependencies required to run the script.
