# What is Unit Testing?

unittest is Python’s built-in testing framework, inspired by Java’s JUnit.

👉 It is used to:

- Write test cases
- Organize tests
- Run tests
- Validate results

## Key Concepts in unittest

### 1. Test Case

- A class that contains test methods.

        import unittest

        class TestMath(unittest.TestCase):
            def test_add(self):
                self.assertEqual(2 + 3, 5)

### 2. Test Method

- Must start with test\_
- Each method tests one behavior

There are following unittest methods:

- assertEqual
- assertNotEqual
- assertTrue
- assertFalse
- assertIn
- assertNotIn
- ...

### 3. Test Runner

- Runs tests and shows results

        if __name__ == "__main__":
            unittest.main()

## Parameterized Testing (Workaround)

- unittest doesn’t support parameterization natively like pytest.
