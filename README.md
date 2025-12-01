# Python Learning Challenges

This repository contains a collection of Python modules and scripts designed to help you learn and practice fundamental programming concepts. Each module focuses on a specific topic, including data structures, control flow, object-oriented programming, and practical coding challenges proposed to me during my **School of Software Engineering (2025)** training at Endava Uruguay.

<br>

## Contents

- **data_structures/**  
  Learn about mutable and immutable collections in Python, including lists, dictionaries, sets, tuples, strings, and variables.

- **control_structures/**  
  Practice with control flow statements such as `if`, `match-case`, `for`, and `while` loops, including iterative patterns and input validation.

- **comprehensions/**  
  Explore list, set, dict comprehensions, and generator expressions for concise and expressive data transformations.

- **oop/**  
  Understand object-oriented programming concepts like classes, attributes, methods, inheritance, and special methods.

- **challenges/**  
  Solve practical exercises such as password validation, guessing games, and simple battle simulations.

<br>

## How to Use

Each script is self-contained and can be run independently. You can use them as examples, modify them for your own practice, or extend them with new features.

1. **Clone the repository**  
   Open a terminal and run:
   ```
   git clone git@github.com:codenamecoffee/Python_Fundamentals_Exercises.git
   cd Python_Fundamentals_Exercises
   ```

2. **Run any module**

   - **If the module does NOT have relative imports or depend on other package files:**  
     From the repository root, run:
     ```
     python path/to/module.py
     ```
     Example:
     ```
     python data_structures/variables.py
     ```

   - **If the module HAS relative imports or imports other files from the package:**  
     Use the `-m` flag to run it as a module from the repository root:
     ```
     python -m folder.module_name
     ```
     Example:
     ```
     python -m data_structures.variables
     ```
     > This ensures that relative imports work correctly.

   - **On Windows, if you have multiple Python versions installed:**  
     You can use the launcher:
     ```
     py -3 path\to\module.py
     py -3 -m folder.module_name
     ```

3. **About the Python interpreter**  
   Make sure you have Python 3.10 or higher installed:
   ```
   python --version
   ```

4. **(Optional) Use a virtual environment**  
   To isolate dependencies and Python versions:
   ```
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Mac/Linux:
   source .venv/bin/activate
   ```
   Then run the modules as shown above.

---

**Notes:**
- Use `python -m package.module` if the file has relative imports or depends on other modules in the same package.
- If it is just a simple script and does not import other files, you can run it directly with `python file.py`.
- Currently, most scripts in this repository do not use relative imports, but these instructions will help if you add internal dependencies in the future.

<br>

## Requirements

- Python 3.10 or higher is recommended (for `match-case` syntax).
- No external dependencies required.

<br>

## License

This repository is for educational purposes.

<br>

## Author

Federico González Lage
