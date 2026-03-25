# Testing:

Testing means checking that your code actually does what you think it does before your users find out it doesn't.

## Types of Tests:

### 1. Unit Tests:

- Test one small piece in isolation

        def test_calculate_discount():
        assert calculate_discount(100, 10) == 90

### 2. Integration Tests:

- Test how pieces work together

        def test_user_creation_saves_to_db():
            response = client.post("/users/", {"name": "Haider"})
            assert User.objects.filter(name="Haider").exists()

### 3. End-to-End (E2E) Tests:

- Test the whole flow like a real user
- Does the full signup → login → dashboard flow work?

# Assert

- assert says "I guarantee this is true if not, crash and tell me."
- It is a debugging/testing statement used to verify that a condition is True.

### Key Takeaway:

- Use assert for debugging and testing
- Not for handling runtime errors
- Avoid in production backend logic
- Prefer pytest asserts in testing
- Remember: asserts can be disabled with -O flag
