# What is Test-Driven Development (TDD)?

Test-Driven Development (TDD) is a software development approach where:

👉 You write tests BEFORE writing the actual code

## The TDD Cycle

🔁 Red → Green → Refactor

### 1- RED (Write failing test):

    def test_add():
        assert add(2, 3) == 5   # add() not implemented yet

### 2. GREEN (Make it pass)

- Write minimal code to pass the test

        def add(a, b):
            return a + b

### 3. REFACTOR (Improve code)

- Clean code without breaking tests
- optimize, rename, structure better

## 🔁 Cycle repeats for every feature

# Core Principles of TDD

✅ Write minimal code

- Only enough to pass test

✅ One test at a time

- Avoid writing 10 tests together

✅ Tests must be independent

- No dependency between tests

✅ Tests must be repeatable

- Same result every time

✅ Tests should be fast

- Unit tests should run in milliseconds

### Assert in TDD (Test Driven Development)

In TDD cycle:

- Write test with assert
- Run → fail
- Implement logic
- Run → pass

# Final Takeaway

👉 TDD is not just testing — it’s a design philosophy

It forces you to:

- Think before coding
- Write clean APIs
- Build reliable systems
