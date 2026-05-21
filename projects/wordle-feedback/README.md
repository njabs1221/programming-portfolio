# Wordle Feedback

Produces Wordle-style feedback for a target word and a guess.

- uppercase letter: correct letter in the correct position
- lowercase letter: correct letter in the wrong position
- `.`: letter not found

## Concepts used

- string processing
- duplicate-letter handling
- two-pass matching algorithm

## Run

```bash
python3 main.py
```

## Example

Input:

```text
CRANE
CABLE
```

Output:

```text
CA..E
```
