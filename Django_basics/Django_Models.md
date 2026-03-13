# Django Models: The Database Blueprint

A **Model** is the single, definitive source of truth about your data. It contains the essential fields and behaviors of the data you’re storing. In Django, models act as an abstraction layer (ORM) between your Python code and the SQL database.

### 1. The Power of the ORM (Object-Relational Mapper)

Instead of writing raw SQL like `SELECT * FROM tasks_task;`, you interact with your database using Python code. The ORM handles the translation to SQL for you.

---

### 2. Practical Example

Defining a model in `models.py`:

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=64)
    priority = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.priority})"
```
