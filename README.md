# Package Classification System

This project implements a system to classify packages based on their dimensions and weight.

## Description

The system classifies packages into three categories:

- **STANDARD**: Packages that are neither bulky nor heavy.
- **SPECIAL**: Packages that are either bulky OR heavy, but not both.
- **REJECTED**: Packages that are both bulky AND heavy.

## Classification Criteria

- A package is considered **bulky** if:
  - Its volume is ≥ 1,000,000 cm³, or
  - Any of its dimensions is ≥ 150 cm

- A package is considered **heavy** if:
  - Its mass is ≥ 20 kg

## Error Handling

The system includes validations to ensure that package data is valid:

- **Negative dimensions**: If any dimension (width, height, length) is negative, a `ValueError` will be raised.
- **Negative mass**: If the package mass is negative, a `ValueError` will be raised.

## Usage
To use the package classification system, follow these steps:

1. Import the `Package` class from the module:
   ```python
   from package import Package
   ```

2. Create a package instance with its dimensions (in centimeters) and mass (in kilograms):
   ```python
   # Example: package of 30x40x50 cm with a mass of 15 kg
   my_package = Package(30, 40, 50, 15)
   ```

3. Use the `sort()` method to get the package classification:
   ```python
   classification = my_package.sort()
   print(f"Package classification: {classification}")
   ```
