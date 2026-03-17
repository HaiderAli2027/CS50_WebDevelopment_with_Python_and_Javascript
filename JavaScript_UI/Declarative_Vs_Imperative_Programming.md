# JavaScript Concepts: Imperative vs Declarative + State

## Imperative Programming (HOW):

You tell the computer step-by-step **how to perform a task.**

    Example:
    const numbers = [1, 2, 3, 4];
    let sum = 0;

    for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    }

    console.log(sum); // 10

### Explanation:

You manually control the loop, variables, and updates.

## Declarative Programming (WHAT):

You tell the computer **what result you want,** _not how to achieve it._

    Example:
    const numbers = [1, 2, 3, 4];

    const sum = numbers.reduce((total, num) => total + num, 0);

    console.log(sum); // 10

### Explanation:

You describe the operation, and JavaScript handles the internal steps.

## State in Web Apps (Changing Data):

State is the **data that changes over time and affects the UI.**

    Example 1 (Counter State):
    let count = 0;

    function increment() {
    count++;
    console.log(count);
    }

### Explanation:

"count" is the state. When it changes, the output changes.

    Example 2 (UI State - Page Switching):
    function showPage(page) {
    document.querySelectorAll('div').forEach(div => {
    div.style.display = 'none';
    });

        document.querySelector(`#${page}`).style.display = 'block';

    }

### Explanation:

The currently visible page is the state. When it changes, the UI updates.

Key Idea:
UI = f(state)

### Meaning:

When **state changes,** the UI automatically reflects the new state.
