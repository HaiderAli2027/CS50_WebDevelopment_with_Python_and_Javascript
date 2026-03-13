# Django Class-Based Views (CBVs)

In Django, views can be written as Python functions (**Function-Based Views**) or as Python classes (**Class-Based Views**). While FBVs are excellent for learning the fundamentals, **Class-Based Views (CBVs)** allow you to write significantly less code by leveraging object-oriented programming (inheritance) and pre-built logic for common web development tasks.

---

## 1. Why Use CBVs?

Using classes for views offers several structural advantages:

- **DRY (Don't Repeat Yourself):** Django provides "Generic" views that handle common patterns—like listing items from a database or deleting an object—so you don't have to rewrite that logic every time.
- **Better Organization:** In a function-based view, you usually handle different HTTP methods (GET, POST, etc.) using `if` statements. In a CBV, these are handled by specific class methods (e.g., `get()` or `post()`), making the code much cleaner.
- **Inheritance:** You can create a "Base" view with shared logic (like login requirements) and have other views inherit from it.

---

## 2. Common Built-in Generic CBVs

Django comes with "ready-to-use" views for standard CRUD (Create, Read, Update, Delete) operations:

| View Type        | Purpose                                                         |
| :--------------- | :-------------------------------------------------------------- |
| **`ListView`**   | Renders a list of objects (e.g., a list of all your tasks).     |
| **`DetailView`** | Renders a single specific object (e.g., details for Task #5).   |
| **`CreateView`** | Displays a form to create an object and saves it automatically. |
| **`UpdateView`** | Displays a form to edit an existing object and saves changes.   |
| **`DeleteView`** | Handles the confirmation and deletion of an object.             |

---

## 3. Practical Example: ListView

Instead of manually querying the database and calling `render()`, you can let `ListView` do the heavy lifting.

### The View (`views.py`)

```python
from django.views.generic import ListView
from .models import Task

class TaskListView(ListView):
    # The model to query
    model = Task

    # The template to use (Default: tasks/task_list.html)
    template_name = "tasks/index.html"

    # The name to use inside the HTML template (Default: object_list)
    context_object_name = "tasks"
```
