# Combined audit task

Run the combined custom audit of the supplied repository using the available maintainability, runtime scaling, and security skills. Give one report. The runtime inventory and repository path are supplied with this task. Existing files belong to the user.

The repository is a small internal document service. The README, source, and contracts below are the full available application context. No dependencies or deployed systems need to be queried. Do not execute the application, install tools, or contact external services.

## README.md

Documents are private to their owner. Signed, unexpired sessions supply an account ID, but authentication does not authorize access to any particular document. Document IDs are valid UUIDs visible in shared links, not secrets. The database has no hidden owner filter or row-level security.

An authenticated account can upload an arbitrary-length body. The gateway enforces no byte limit, and request.read() returns the entire body as bytes. store.put() writes those bytes to durable storage. The upload response needs only the stored byte count. No specific maximum upload size or production memory measurement is available.

The checkout estimate and invoice charge must use the same ten-percent discount for a member and no discount otherwise. Amounts are integer cents, and floor division is intentional. These are the only pricing callers. There are no external consumers. Current tests cover one normal owner read, a small upload, and matching member prices.

## app.py

```python
async def upload(request, store):
    account = require_session(request)
    body = await request.read()
    await store.put(account.id, body)
    return {"bytes": len(body)}


async def read_document(request, db):
    account = require_session(request)
    row = await db.fetch_one(
        "SELECT contents FROM documents WHERE id = ?",
        [request.path_params["id"]],
    )
    return None if row is None else row["contents"]
```

`require_session` obeys the README contract. `fetch_one` binds its parameters safely. Its first argument is the full query; it adds no other predicates.

## pricing.py

```python
def checkout_estimate(cents, member):
    return cents * 90 // 100 if member else cents


def invoice_charge(cents, member):
    return cents * 90 // 100 if member else cents
```
