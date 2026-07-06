# Data Cleaning Log

This document explains the main cleaning steps applied to the animal observation dataset.

## Original Dataset

The original dataset contained **1,011 records** and **11 columns**.

Initial inspection showed several data quality issues, including:

- Duplicate records
- Missing values
- Inconsistent animal type names
- Inconsistent country names
- Empty or mostly empty columns
- Mixed date formats
- Invalid numeric values
- Invalid latitude values

## Cleaning Steps Applied

### 1. Standardised Column Names

Column names were cleaned to make them easier to use in Python.

The cleaning included:

- Removing extra spaces
- Converting names to lowercase
- Replacing spaces with underscores
- Removing brackets

Examples:

| Original Column | Cleaned Column |
|---|---|
| `Animal type` | `animal_type` |
| `Weight kg` | `weight_kg` |
| `Body Length cm` | `body_length_cm` |
| `Observation date` | `observation_date` |
| `Data compiled by` | `data_compiled_by` |

## 2. Removed Duplicate Records

Duplicate records were removed from the dataset.

The original dataset contained **167 duplicate records**.

## 3. Removed Unnecessary Columns

The following columns were removed:

| Column | Reason |
|---|---|
| `animal_code` | The column was completely empty. |
| `animal_name` | The column had a very large number of missing values and was not useful for general ML preparation. |

## 4. Cleaned Animal Type Values

The `animal_type` column contained spelling mistakes, symbols, and inconsistent values.

Examples of cleaned values:

| Original Value | Cleaned Value |
|---|---|
| `European bison™` | `European Bison` |
| `European bisson` | `European Bison` |
| `European buster` | `European Bison` |
| `red squirrell` | `Red Squirrel` |
| `red squirel` | `Red Squirrel` |
| `lynx?` | `Lynx` |
| `ledgehod` | `Hedgehog` |
| `wedgehod` | `Hedgehog` |

Rows with missing `animal_type` values were removed because animal type is a key column in the dataset.

## 5. Cleaned Country Values

The `country` column contained abbreviations and spelling mistakes.

Examples of cleaned values:

| Original Value | Cleaned Value |
|---|---|
| `PL` | `Poland` |
| `HU` | `Hungary` |
| `Hungry` | `Hungary` |
| `CZ` | `Czech Republic` |
| `DE` | `Germany` |
| `Czech` | `Czech Republic` |
| `Australia` | `Austria` |
| `CC` | `Czech Republic` |

## 6. Converted Observation Dates

The `observation_date` column was converted from text into a proper date format.

The dataset contained multiple date formats, including:

- `03.01.2024`
- `03.13.2024`
- `5 May 2024`
- `2 may 2024`

Multiple parsing rules were used so that all valid date formats could be converted successfully.

After cleaning, all observation dates were successfully converted.

## 7. Handled Missing Gender Values

Missing values in the `gender` column were filled with:

```text
not determined