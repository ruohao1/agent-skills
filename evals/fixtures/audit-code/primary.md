# Task

Audit this repository for code hygiene and refactoring opportunities as the codebase grows. I want readable code that is easy to extend. Return all supported findings. Do not change code or create tickets.

# Source context

The following are synthetic completed repository reads. The numbered lines are source locations, not executable prefixes. All application-owned Python files, configuration, and tests are included. There is no hidden application code, plugin loader, generated source, or public Python SDK. No further tools or repository inspection are needed.

The application is an internal desktop quote tool. The injected storage, charging, and notification adapters are maintained by the host application and are outside this repository. Their contracts provide the atomic persistence and error handling used here. Audit this application's maintainability; host-adapter implementation and traffic scaling are not requested.

`README.md`

```text
1 Quote Desk previews and finalizes one customer's quote at a time.
2 Quotes must use the same fee policy in preview and checkout.
3 Money is stored as integer cents. The UI displays euros.
4 The CSV exporter is loaded by the host through the quotedesk.exporters entry-point group.
5 The application is not distributed as a Python library.
6 Run python3 -m unittest discover -s tests to check it.
```

`pyproject.toml`

```toml
1 [project]
2 name = "quotedesk"
3 version = "0.1.0"
4 [project.entry-points."quotedesk.exporters"]
5 csv = "app.csv_export:export_quotes"
```

`app/__init__.py` is empty.

`app/checkout.py`

```python
1 from app.notifications import deliver
2
3 def checkout(quote_id, store, charger, sender):
4     quote = store.load(quote_id)
5     subtotal = sum(item["cents"] * item["quantity"] for item in quote["items"])
6     discounted = subtotal
7     if quote["tier"] == "partner":
8         discounted -= subtotal // 10
9     elif quote["tier"] == "member":
10         discounted -= min(subtotal // 20, 500)
11     handling = 0 if discounted >= 5000 else 250
12     total = discounted + handling
13     receipt = charger.charge(quote["customer_id"], total)
14     store.save_receipt(quote_id, receipt, total)
15     deliver(sender, quote["customer_id"], receipt)
16     return receipt
```

`app/preview.py`

```python
1 def preview(quote_id, store):
2     quote = store.load(quote_id)
3     subtotal = sum(item["cents"] * item["quantity"] for item in quote["items"])
4     discounted = subtotal
5     if quote["tier"] == "partner":
6         discounted -= subtotal // 10
7     elif quote["tier"] == "member":
8         discounted -= min(subtotal // 20, 500)
9     handling = 0 if discounted >= 5000 else 250
10     return discounted + handling
```

`app/notifications.py`

```python
1 from app.transport import relay
2
3 def deliver(sender, customer_id, receipt):
4     return relay(sender, customer_id, receipt)
```

`app/transport.py`

```python
1 from app.dispatch import dispatch
2
3 def relay(sender, customer_id, receipt):
4     return dispatch(sender, customer_id, receipt)
```

`app/dispatch.py`

```python
1 def dispatch(sender, customer_id, receipt):
2     return sender.send(customer_id, receipt)
```

`app/display.py`

```python
1 def format_total(cents):
2     """Format an amount supplied in whole euros."""
3     return f"€{cents // 100}.{cents % 100:02d}"
4
5 def data(q):
6     return {"ready": "Ready to charge", "paid": "Paid"}[q["status"]]
```

`app/screen.py`

```python
1 from app.display import data, format_total
2 from app.preview import preview
3
4 def quote_screen(quote_id, store):
5     quote = store.load(quote_id)
6     return {"status_label": data(quote), "total_label": format_total(preview(quote_id, store))}
```

`app/archive.py`

```python
1 def archive_paid_quotes(store, exporter):
2     paid = store.list_paid()
3     if not paid:
4         return None
5     artifact = exporter.write(paid)
6     store.mark_archived([quote["id"] for quote in paid])
7     return artifact
```

`app/csv_export.py`

```python
1 import csv
2 import io
3
4 def export_quotes(quotes):
5     output = io.StringIO()
6     writer = csv.writer(output)
7     writer.writerow(["id", "total_cents"])
8     writer.writerows((quote["id"], quote["total_cents"]) for quote in quotes)
9     return output.getvalue()
```

`app/legacy.py`

```python
1 def old_flat_fee(subtotal):
2     return subtotal + 400
```

`app/identifiers.py`

```python
1 def normalize_customer_search(value):
2     return value.strip().lower()
3
4 def normalize_export_tag(value):
5     return value.strip().lower()
```

`app/search.py`

```python
1 from app.identifiers import normalize_customer_search, normalize_export_tag
2
3 def search_customers(store, query):
4     return store.find_customer_names(normalize_customer_search(query))
5
6 def export_by_tag(store, tag):
7     return store.find_exports(normalize_export_tag(tag))
```

`tests/test_app.py`

```python
1 import unittest
2 from unittest.mock import Mock
3 from app.checkout import checkout
4 from app.preview import preview
5 from app.archive import archive_paid_quotes
6 from app.display import format_total
7 from app.screen import quote_screen
8 from app.csv_export import export_quotes
9 from app.search import search_customers, export_by_tag
10
11 class AppTests(unittest.TestCase):
12     def test_pricing(self):
13         for tier, subtotal, expected in [("regular", 1000, 1250), ("partner", 1000, 1150), ("member", 20000, 19500), ("partner", 10000, 9000)]:
14             with self.subTest(tier=tier, subtotal=subtotal):
15                 quote = {"items": [{"cents": subtotal, "quantity": 1}], "tier": tier, "customer_id": "C1"}
16                 store, charger, sender = Mock(), Mock(), Mock()
17                 store.load.return_value = quote
18                 self.assertEqual(preview("Q1", store), expected)
19                 checkout("Q1", store, charger, sender)
20                 charger.charge.assert_called_once_with("C1", expected)
21                 store.save_receipt.assert_called_once_with("Q1", charger.charge.return_value, expected)
22                 sender.send.assert_called_once_with("C1", charger.charge.return_value)
23     def test_archive_empty(self):
24         store, exporter = Mock(), Mock()
25         store.list_paid.return_value = []
26         self.assertIsNone(archive_paid_quotes(store, exporter))
27         exporter.write.assert_not_called()
28     def test_archive_paid(self):
29         store, exporter = Mock(), Mock()
30         store.list_paid.return_value = [{"id": "Q1"}]
31         self.assertEqual(archive_paid_quotes(store, exporter), exporter.write.return_value)
32         store.mark_archived.assert_called_once_with(["Q1"])
33     def test_screen(self):
34         store = Mock()
35         store.load.return_value = {"items": [{"cents": 1000, "quantity": 1}], "tier": "regular", "status": "ready"}
36         self.assertEqual(quote_screen("Q1", store), {"status_label": "Ready to charge", "total_label": "€12.50"})
37         self.assertEqual(format_total(1250), "€12.50")
38     def test_csv(self):
39         self.assertEqual(export_quotes([{"id": "Q1", "total_cents": 1250}]), "id,total_cents\r\nQ1,1250\r\n")
40     def test_search(self):
41         store = Mock()
42         search_customers(store, "  ALICE ")
43         store.find_customer_names.assert_called_once_with("alice")
44         export_by_tag(store, "  MONTHLY ")
45         store.find_exports.assert_called_once_with("monthly")
```

# Evidence limits

The supplied source snapshot is complete for this application. The host's external adapters were not inspected. No test execution result is supplied. Report code observations without claiming a test run or an observed production failure.
