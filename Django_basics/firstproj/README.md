## URL Reverse Resolution:

URL Reverse Resolution is the practice of referencing a URL by a specific name rather than its hardcoded path (e.g., using add_task instead of /tasks/add/).

### Why use it?

Decoupling: You can change the URL structure in urls.py without breaking links in your HTML or views.

Maintenance: Update a path in one place, and it updates site-wide automatically.
