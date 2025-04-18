# djangosignals

This repository contains code examples and explanations related to Django Signals and Python custom class behavior.

- **test_signals.py**  
  Contains code to test whether Django signals are executed synchronously by default.

- **check_thread.py**  
  Contains code to check if Django signals run in the same thread as the caller.

- **trans_test.py**  
  Contains code to verify whether Django signals execute within the same database transaction as the caller.

- **Answers.txt**  
  Contains theory-based answers and explanations for all three Django signal behavior questions.

- **customClasses.py**  
  Contains a Python implementation of a `Rectangle` class that:
  - Accepts `length` and `width` as inputs
  - Supports iteration
  - Yields `{'length': value}` followed by `{'width': value}` when iterated
