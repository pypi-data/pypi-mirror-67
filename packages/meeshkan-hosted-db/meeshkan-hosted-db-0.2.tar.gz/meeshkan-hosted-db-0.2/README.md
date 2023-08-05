# meeshkan-hosted-db
Utility python package to access a [Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres) database using [psycopg2](https://www.psycopg.org/) on [meeshkan.io](https://meeshkan.io).

```python
from meeshkan_hosted_db import connect_to_db

with connect_to_db() as db:
    with db.cursor() as cursor:
        cursor.execute("SELECT NOW() as now;")
        result = cursor.fetchall()
    current_time = result[0][0]
```
