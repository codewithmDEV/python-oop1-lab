# Python OOP Lab - Bookstore

## Description
This project implements two classes to model items sold in a bookstore: `Book` and `Coffee`. Both classes use Python's `@property` decorator to validate their attributes before allowing changes.

## Classes

### Book
- Takes a `title` and `page_count` on creation.
- `page_count` must be an integer. Attempting to set it to a non-integer prints an error message instead of updating the value.
- `turn_page()` prints a message simulating turning a page.

### Coffee
- Takes a `size` and `price` on creation.
- `size` must be one of "Small", "Medium", or "Large". Any other value prints an error message instead of updating it.
- `tip()` prints a message and increases the price by 1.

## Running Tests
Tests are located in `lib/testing/`. Run them with:

\`\`\`
pytest lib/testing/
\`\`\`

## Test Results
![Passing tests](![alt text](image-1.png))