OJT Backend Developer Learning – 20th November 2025
1. PostgreSQL (Relational Database)
Advanced open-source RDBMS with robustness, extensibility, standards compliance.

Supports complex queries, custom data types, full-text search, ACID properties.

Strong concurrency, suitable for web apps to data warehousing.

2. API Concepts
a) JSON APIs
JSON (JavaScript Object Notation): encoding scheme for server communication.

JSON API: standardized implementation for data stores/structures.

Defines entity types, bundles, fields with communication protocols.

b) Authentication
Verifies client identity for secure API access.

Common methods: API keys, OAuth 2.0, JWT, Basic Auth.

Protects data, prevents unauthorized access, enables usage tracking.

c) JWT (JSON Web Token)
Securely transmits information as JSON objects.

Three parts: Header (token type/algorithm), Payload (claims/data), Signature (verification).

Used for authentication/authorization in web/mobile apps.

Compact, self-contained, HTTP header-friendly.

d) Ad Hoc Code
Actions taken at run-time rather than pre-defined in application.

Refers to solutions designed for singular purpose vs well-structured/planned code.

Useful for quick fixes but not ideal for long-term maintainability.

e) URI (Uniform Resource Identifier)
Identifies resources on the web.

Commonly used as targets of HTTP requests.

Represents location for resources (documents, photos, binary data).

Example: https://api.example.com/users/123

3. Redis (Caching)
Open-source, in-memory data structure store.

Supports: strings, lists, sets, hashes, sorted sets.

Use cases: caching, session management, real-time analytics, message brokering.

Offers persistence, replication, clustering, low-latency high-throughput.

LRU (Least Recently Used) Caching Algorithm
Caching strategy that discards items not recently accessed.

More efficient than basic FIFO (First-In-First-Out) approach.

When cache is full, removes least recently used item to make space.

Balances memory usage with access patterns for optimal performance.

Used in: Redis, CPU caches, browser caches.

4. Database Fundamentals
a) Database & DBMS
Database: structured collection of useful organizational data.

DBMS: software to maintain/extract large data collections efficiently.

b) ORMs (Object-Relational Mapping)
Maps database tables to classes, rows to objects.

Eliminates raw SQL queries, simplifies data manipulation.

Popular ORMs: Hibernate (Java), Entity Framework (.NET), SQLAlchemy (Python).

c) ACID Properties
Database transaction properties ensuring reliability:

Atomicity

Transaction is all-or-nothing.

If any operation fails, entire transaction rolls back.

Example: Money transfer—debit and credit must both succeed or both fail.

Consistency

Database remains in valid state before/after transaction.

Maintains rules, constraints, relationships (primary/foreign keys).

Example: Total balance across accounts stays constant during transfers.

Isolation

Transactions execute independently.

Changes invisible to others until committed.

Prevents dirty reads, non-repeatable reads, phantom reads.

Example: Concurrent modifications appear as sequential execution.

Durability

Committed changes are permanent, even after system crash.

Data stored in non-volatile memory.

Example: Transfer remains intact after system failure.

Importance: Critical for banking, e-commerce, healthcare—ensures data integrity and reliability.

d) Transactions
Sequence of operations (read, write, update, delete) executed as single logical unit.

All operations succeed or fail completely, ensuring consistency.

e) N+1 Problem
Performance issue in ORMs.

1 query fetches primary data, then N additional queries fetch related data for each item.

Results in N+1 total queries, causing performance bottleneck.

Solution: Use eager loading or joins to fetch related data in single query.

5. Testing
Overview
Systematically evaluates software functionality, performance, quality.

Types: Unit, Integration, System, Acceptance testing.

Methods: Manual or automated.

Goal: Identify defects, validate features, ensure reliability before deployment.

a) Integration Testing
Verifies interactions between components.

Tests module communication via APIs, databases, third-party services.

Catches issues like data mismatches, protocol errors missed by unit tests.

b) Unit Testing
Tests individual components in isolation.

Focuses on smallest testable parts (functions, methods).

Automated tests written by developers during coding.

Catches bugs early, improves code reliability.

c) Functional Testing
Ensures software meets functional requirements.

Black box testing: provides input, compares expected vs actual output.

No knowledge of source code required.

Contrasts with non-functional testing (performance, load, scalability).

6. CLI Application
Command Line Interface (CLI): text-based interface for software interaction.

Users type commands into console/terminal.

Widely used by developers, system admins for efficiency and powerful capabilities.

Benefits: Fast execution, scriptable, lightweight, precise control.

