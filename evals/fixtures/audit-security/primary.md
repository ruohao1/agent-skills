# Task

Audit Ledger Room for security risks, including its dependencies and CI configuration. Return all supported findings. Do not modify code, create tickets, or test deployed systems.

# Source context

These are synthetic completed source and advisory reads. Numbered lines identify source locations. Package names and advisory IDs below are fictional; do not query actual registries or services. Do not inspect other repositories or use connectors. No tests, scanner, exploit, or deployed configuration check was run by you. All relevant application paths and the following verified contracts are supplied.

Ledger Room stores private reports owned by separate accounts. Every authenticated account may call read_report, search, and profile. Report IDs occur in shareable links and are not authorization secrets. The intended policy is that an account can only read its own reports; sharing is not implemented.

Verified host contracts and repository evidence:
- require_session validates the signed session and returns its account. It does not authorize object access. The database has no row-level security or hidden owner filter.
- request.path_params.id is a validated UUID. request.query.q is a decoded user string with a 1000-character length limit; it is not SQL-escaped. fetch_all executes the supplied SQL string. Parameter arrays in fetch_one bind values safely.
- Every API request passes through log_request. Application logs are retained for 30 days and readable by an operations group that is not authorized to impersonate accounts. Authorization headers contain reusable bearer tokens.
- The repository is public, accepts outside pull requests, and has the displayed workflow enabled. Repository secrets include RELEASE_TOKEN. There is no environment approval gate for this job. These are supplied repository facts, not a newly performed host check.
- The archive plugin loads at startup with the displayed configuration. The host's archive-import extension implementation and its input sources are unavailable. It is not established whether an attacker can reach the extraction operation.
- A deployed package inventory and the resolved lock both show archivekit 2.4.2 and safeweb 1.8.4. No other packages are reported affected in the supplied evidence.

Synthetic authoritative advisory read, checked for this fixture:
- ARCHIVE-2026-04, archivekit maintainer: versions 2.4.0 through 2.4.3 allow writes outside the destination when a crafted archive is extracted with allow_parent_paths=True. Version 2.4.4 fixes it. The lock, inventory, and configuration establish those version and option conditions; whether crafted archives reach this application is unknown. The vendor labels the generic advisory High.
- SAFEWEB-2025-08, safeweb maintainer: a session bypass affects versions below 1.8.0. Version 1.8.4 is outside the affected range. A stale scanner export still labels this dependency Critical without resolving the installed version.

Existing tests check each owner's normal report and search result, profile rendering, and successful archive plugin registration. No cross-account or injection regression is in the supplied inventory. A deployment file binds the app to an internal interface behind a gateway; the live gateway's configuration is unavailable. Do not infer its public exposure or isolation from the file alone.

`app/reports.py`

```python
1 from host.auth import require_session
2
3 def read_report(request, db):
4     user = require_session(request)
5     return db.fetch_one(
6         "SELECT id, owner_id, contents FROM reports WHERE id = ?",
7         [request.path_params["id"]],
8     )
```

`app/search.py`

```python
1 from host.auth import require_session
2
3 def search(request, db):
4     user = require_session(request)
5     term = request.query["q"]
6     sql = f"SELECT id, title FROM reports WHERE owner_id = '{user.id}' AND title LIKE '%{term}%'"
7     return db.fetch_all(sql)
```

`app/logging.py`

```python
1 def log_request(request, logger):
2     logger.info("request path=%s authorization=%s", request.path, request.headers.get("Authorization"))
```

`app/archive_plugin.py`

```python
1 import archivekit
2 from host.plugins import register
3
4 archivekit.configure(allow_parent_paths=True)
5 register("archive_import", archivekit.extract)
```

`app/profile.py`

```python
1 from host.auth import require_session
2
3 def profile(request, db):
4     user = require_session(request)
5     return db.fetch_one("SELECT display_name FROM users WHERE id = ?", [user.id])
```

`.github/workflows/check.yml`

```yaml
1 name: Check contribution
2 on: pull_request_target
3 permissions:
4   contents: write
5 jobs:
6   check:
7     runs-on: ubuntu-latest
8     steps:
9       - uses: actions/checkout@v4
10         with:
11           ref: ${{ github.event.pull_request.head.sha }}
12       - run: python -m unittest discover -s tests
13         env:
14           RELEASE_TOKEN: ${{ secrets.RELEASE_TOKEN }}
```

`requirements.lock`

```text
1 archivekit==2.4.2
2 safeweb==1.8.4
```
