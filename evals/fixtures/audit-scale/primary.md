# Task

Audit Relay Desk for runtime scaling problems as its data and workload grow. Include concurrency and recovery. Return all supported findings; do not change code or create issues.

# Source context

These are synthetic completed repository reads. Numbered lines identify source locations. Do not inspect other repositories, use connectors, or run live tests. All relevant application paths and adapter contracts are supplied; no further inspection is available. No tests or load measurements have been run for this audit.

Relay Desk reserves prepaid account credits, sends queued notifications, renders exports, and serves account event reports. Authenticated account membership is enforced by the host before these functions run. Amounts are validated positive integers. Public report responses must include all requested events in chronological order. There are no published workload targets or production metrics; account history has no configured size limit.

Host contracts, verified from adapter documentation:
- Each balance read and balance write is atomic on its own. There is no transaction spanning the two calls. All API workers use the same database.
- pending_messages returns unsent messages. mailer.send can deliver a message and then lose its acknowledgement; it has no deduplication parameter. On a process restart, unsent messages are retried.
- claim_next_queued atomically changes one queued job to running with its worker ID. Only queued jobs are eligible. The schema has status and worker_id, with no claim expiry; no restart reconciliation or recovery job exists. complete_job changes running to done.
- all_events materializes a list; load_owner makes one database round trip. Owner records can repeat across events. No batching or streaming adapter is currently used.
- Template names come from a fixed allowlist of twelve immutable bundled files. The same loader object is reused. Cache misses are harmless and may occur separately in each process.
- HTTP adapters may stream a response if the application is changed to use that interface. There is no proxy pagination or hidden query cache.

Existing test inventory covers a successful reservation, rejected over-budget reservation, normal delivery, normal export completion, and report contents for two events. It contains no concurrent-worker, interruption, or large-history tests. This is a test inventory, not a passing execution result.

`app/quota.py`

```python
1 def reserve(store, account_id, amount):
2     remaining = store.balance(account_id)
3     if amount > remaining:
4         return False
5     store.set_balance(account_id, remaining - amount)
6     return True
```

`app/delivery.py`

```python
1 def deliver(store, mailer):
2     for message in store.pending_messages():
3         mailer.send(message.recipient, message.body)
4         store.mark_sent(message.id)
```

`app/exports.py`

```python
1 def work_one(store, renderer, worker_id):
2     job = store.claim_next_queued(worker_id)
3     if job is None:
4         return
5     output = renderer.render(job.input)
6     store.complete_job(job.id, output)
```

`app/report.py`

```python
1 import json
2
3 def account_report(store, account_id):
4     rows = store.all_events(account_id)
5     result = []
6     for row in rows:
7         owner = store.load_owner(row.owner_id)
8         result.append({"id": row.id, "owner": owner.name, "text": row.text})
9     return json.dumps(result)
```

`app/templates.py`

```python
1 from functools import lru_cache
2
3 @lru_cache(maxsize=32)
4 def template(name, loader):
5     return loader.read(name)
```

`app/settings.py`

```python
1 API_WORKERS = 4
2 EXPORT_WORKERS = 2
3 DELIVERY_WORKERS = 1
```
