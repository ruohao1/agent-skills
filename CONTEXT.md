# Audit and design purposes

These terms distinguish the audit and design workflows in this marketplace.

## Language

### Audits

**Code maintainability audit**:
An assessment of how easily people can understand, test, and change a codebase as it grows.
_Avoid_: Scaling audit without specifying code growth.

**Runtime scaling audit**:
An assessment of behavior as data volume or concurrent work increases, within one process or across users, workers, and jobs. Its scope includes concurrency and recovery correctness, even at low traffic; general performance problems unrelated to these concerns are outside its purpose.
_Avoid_: Process scaling, which omits growth within one process.

**Security audit**:
An assessment of weaknesses an attacker could exploit in application code, dependencies, CI workflows, deployment configuration, and secret handling, based on available evidence.

**Combined audit**:
One report that brings together maintainability, runtime scaling, and security audits of the same source scope. Shared causes are reported once with all supported consequences. Missing passes remain explicit coverage gaps.

**Supported finding**:
An audit conclusion established by verified source, configuration, or observed behavior, with its triggering conditions and consequences stated. A reproduction is not required when the verified code path establishes the problem.

**Unverified lead**:
A suspected problem whose material prerequisites or consequences cannot yet be established from available evidence.

**Dependency finding**:
A security audit finding that identifies an in-scope dependency version affected by a verified advisory, with the advisory conditions and dependency use established. Application exploitability may remain unverified.

### Design

**Design workflow**:
A process that resolves consequential choices for a selected change or new capability. It can use audit findings as evidence, but does not require an audit or repeat decisions already adequately resolved.

**Product brief**:
A statement of the user problem, evidence, scope, constraints, and observable success criteria. It establishes the purpose of a proposed change.

**Product design**:
The design of the complete user experience, including workflows, rules, interactions, consequential states, recovery, and relevant visual presentation. It specifies how a proposed solution behaves for its users.

**Architecture design**:
The allocation of system responsibilities, data ownership, interactions, and runtime constraints needed to support a change. It applies within a single application as well as across separately running parts.

**Code design**:
The organization of an implementation into modules, interfaces, dependencies, files, and folders. It resolves structural choices needed to understand, test, and change the implementation.

**Design document**:
A concise record of the chosen approach for a coherent change, meaningful alternatives, constraints, and remaining decisions. It contains only the design scopes relevant to that change.
