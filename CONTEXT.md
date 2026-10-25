# Audit purposes

These terms distinguish the audit purposes in this marketplace.

## Language

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
