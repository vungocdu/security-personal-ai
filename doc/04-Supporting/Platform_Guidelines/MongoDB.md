# MongoDB Server Manual Documentation

The MongoDB Server Manual is the official comprehensive documentation for the MongoDB database server, accessible at https://www.mongodb.com/docs/manual/. This repository contains version 7.2 of the manual, covering all aspects of MongoDB database operations including CRUD operations, aggregation, replication, sharding, security, administration, and deployment. Built using Sphinx with custom MongoDB extensions and the Snooty documentation platform, this documentation serves as the authoritative reference for MongoDB database administrators, developers, and architects working with MongoDB server deployments.

This repository is structured as a traditional Sphinx documentation project with reStructuredText (.txt) source files, Python-based build configuration, and extensive code examples demonstrating MongoDB features across multiple programming languages (JavaScript/Node.js, Python, Java, C#, Go). The documentation includes detailed reference material for all MongoDB commands, operators, methods, configuration options, and architectural concepts, along with practical tutorials for common deployment scenarios, security configurations, and performance optimization strategies.

## Documentation Structure

Content organization in reStructuredText format

The repository follows a hierarchical organization with source files in the `source/` directory. Main topic areas are organized into directories (`core/`, `reference/`, `tutorial/`, `administration/`) with individual `.txt` files containing reStructuredText markup. The `snooty.toml` configuration file defines project metadata, cross-references (intersphinx), table of contents structure, constants, and version-specific banners for this MongoDB 7.2 documentation.

```bash
# View main documentation topics
ls /tmp/context7-isolated-f4CaGL/repo/source/
# Output: core/, reference/, tutorial/, administration/, includes/, images/,
#         index.txt, crud.txt, aggregation.txt, replication.txt, sharding.txt, security.txt

# Browse core database concepts
ls /tmp/context7-isolated-f4CaGL/repo/source/core/
# Output: aggregation-pipeline.txt, transactions.txt, replica-set-*.txt,
#         sharding-*.txt, csfle/, queryable-encryption/, indexes/, security-*.txt

# View reference documentation
ls /tmp/context7-isolated-f4CaGL/repo/source/reference/
# Output: command/, operator/, method/, configuration-options.txt,
#         bson-types.txt, write-concern.txt, read-concern.txt

# Check project configuration
cat /tmp/context7-isolated-f4CaGL/repo/snooty.toml
# Shows: name="docs", title="MongoDB Manual", version="7.2",
#        intersphinx references, constants, banners
```

## Sphinx Build System

Giza-based documentation build pipeline

The documentation is built using Sphinx with the Giza build system, which provides MongoDB-specific extensions for documentation generation. The `conf.py` file configures Sphinx with custom extensions including MongoDB directives, tabs, markdown support, and cross-reference capabilities. Building the documentation generates static HTML output in the `build/` directory.

```python
# File: /tmp/context7-isolated-f4CaGL/repo/conf.py (excerpt)
extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
    'mongodb',
    'directives',
    'intermanual',
    'testcode',
    'tabs',
    'markdown',
    'fasthtml',
    'source_constants',
    'icon'
]

source_constants = {
    'version': '7.2',
    'release': '7.2.1',
    'version-dev': '7.3',
    'version-last': '7.0',
    'package-name-org': 'mongodb-org',
    'package-name-enterprise': 'mongodb-enterprise'
}
```

```bash
# Install build dependencies
pip install giza

# Build HTML documentation
make html
# Output: HTML files generated in build/v7.2/html/

# Clean build artifacts
make clean
# Output: Removes build/ directory

# View build configuration
cat /tmp/context7-isolated-f4CaGL/repo/Makefile
# Shows: Build targets and staging/production deployment URLs
```

## Snooty Configuration

Project metadata and versioning system

The `snooty.toml` file serves as the central configuration for the MongoDB Manual, defining project identity, version constants, cross-documentation references, and content organization. It includes intersphinx mappings to other MongoDB documentation properties (Atlas, drivers, tools), constants for version numbers and product names, and banners for version-specific warnings.

```toml
# File: /tmp/context7-isolated-f4CaGL/repo/snooty.toml (excerpt)
name = "docs"
title = "MongoDB Manual"
sharedinclude_root = "https://raw.githubusercontent.com/10gen/docs-shared/main/"

intersphinx = [
    "https://www.mongodb.com/docs/atlas/objects.inv",
    "https://www.mongodb.com/docs/database-tools/objects.inv",
    "https://www.mongodb.com/docs/mongodb-shell/objects.inv"
]

[constants]
version = "7.2"
release = "7.2.1"
version-dev = "7.3"
version-last = "7.0"
latest-lts-version = "7.0"
mongosh = ":binary:`~bin.mongosh`"
atlas = "MongoDB Atlas"
csfle = "Client-Side Field Level Encryption"
qe = "Queryable Encryption"

[[banners]]
targets = ["*"]
variant = "info"
value = """
This version of the documentation is archived and no longer supported.
View the current documentation to learn how to upgrade your MongoDB server.
"""
```

```rst
.. Example cross-reference usage in source/core/transactions.txt
To start a multi-document transaction, use :method:`Session.startTransaction()`.
For connection details, see :atlas:`Connect to Atlas </connect-to-database-deployment>`.
Query operators are documented in :manual:`Query Operators </reference/operator/query>`.
```

## Code Examples System

Multi-language code snippets with includes

The documentation includes extensive code examples demonstrating MongoDB features across multiple programming languages. Examples are organized in the `source/includes/` directory with support for JavaScript/Node.js, Python (PyMongo), Java, C#, Go, and MongoDB Shell (mongosh). Many examples use include directives to embed tested code snippets, particularly for encryption features (CSFLE and Queryable Encryption).

```javascript
// File: /tmp/context7-isolated-f4CaGL/repo/source/includes/qe-tutorials/node/queryable-encryption-tutorial.js
const { MongoClient } = require('mongodb');
const { ClientEncryption } = require('mongodb-client-encryption');

async function main() {
  // Connection string with encryption options
  const uri = process.env.MONGODB_URI;

  // Configure automatic encryption
  const autoEncryptionOpts = {
    keyVaultNamespace: 'encryption.__keyVault',
    kmsProviders: {
      local: {
        key: process.env.LOCAL_MASTER_KEY,
      },
    },
  };

  const client = new MongoClient(uri, { autoEncryption: autoEncryptionOpts });

  try {
    await client.connect();
    const db = client.db('medicalRecords');
    const collection = db.collection('patients');

    // Insert encrypted document
    const result = await collection.insertOne({
      name: 'John Doe',
      ssn: '123-45-6789', // This field will be encrypted
      bloodType: 'O+',
      medicalRecords: [{ condition: 'Diabetes', date: new Date() }],
    });

    console.log('Inserted document:', result.insertedId);
  } finally {
    await client.close();
  }
}

module.exports = { main };
```

```python
# File: /tmp/context7-isolated-f4CaGL/repo/source/includes/qe-tutorials/python/queryable_encryption_tutorial.py
from pymongo import MongoClient
from pymongo.encryption import ClientEncryption
import os

def main():
    # Connection string with encryption options
    uri = os.environ.get('MONGODB_URI')

    # Configure automatic encryption
    kms_providers = {
        'local': {
            'key': os.environ.get('LOCAL_MASTER_KEY')
        }
    }

    auto_encryption_opts = {
        'keyVaultNamespace': 'encryption.__keyVault',
        'kmsProviders': kms_providers
    }

    client = MongoClient(uri, auto_encryption_opts=auto_encryption_opts)

    try:
        db = client.medicalRecords
        collection = db.patients

        # Insert encrypted document
        result = collection.insert_one({
            'name': 'John Doe',
            'ssn': '123-45-6789',  # This field will be encrypted
            'bloodType': 'O+',
            'medicalRecords': [
                {'condition': 'Diabetes', 'date': datetime.now()}
            ]
        })

        print(f'Inserted document: {result.inserted_id}')
    finally:
        client.close()

if __name__ == '__main__':
    main()
```

```bash
# Run Node.js Queryable Encryption tutorial
cd /tmp/context7-isolated-f4CaGL/repo/source/includes/qe-tutorials/node
npm install
MONGODB_URI="mongodb://localhost:27017" LOCAL_MASTER_KEY="$(openssl rand -base64 96)" node queryable-encryption-tutorial.js

# Run Python tutorial
cd /tmp/context7-isolated-f4CaGL/repo/source/includes/qe-tutorials/python
pip install pymongo pymongo[encryption]
MONGODB_URI="mongodb://localhost:27017" LOCAL_MASTER_KEY="$(openssl rand -base64 96)" python queryable_encryption_tutorial.py
```

## Core Documentation Topics

Major subject areas and concepts

The documentation is organized into major topic areas covering MongoDB's feature set. Core concepts in `source/core/` include replication (replica sets), sharding (horizontal scaling), transactions, aggregation pipelines, indexes, security features (authentication, authorization, encryption), and storage engines. The reference section provides comprehensive API documentation for all database commands, operators, and methods.

```rst
.. File: /tmp/context7-isolated-f4CaGL/repo/source/core/transactions.txt (excerpt)

================
Transactions
================

.. contents:: On this page
   :local:
   :backlinks: none
   :depth: 1

In MongoDB, an operation on a single document is atomic. Because you can use
embedded documents and arrays to capture relationships between data in a
single document structure instead of normalizing across multiple documents
and collections, this single-document atomicity obviates the need for
distributed transactions for many practical use cases.

Multi-Document Transactions
-----------------------------

Starting in version 4.0, MongoDB provides the ability to perform
multi-document transactions against replica sets. Starting in MongoDB 4.2,
distributed transactions add support for multi-document transactions on
sharded clusters.

Multi-document transactions can be used across multiple operations,
collections, databases, documents, and shards.

Transactions API
~~~~~~~~~~~~~~~~

Use the following methods to control transactions:

- :method:`Session.startTransaction()`
- :method:`Session.commitTransaction()`
- :method:`Session.abortTransaction()`
```

```bash
# Browse major topic areas
ls /tmp/context7-isolated-f4CaGL/repo/source/core/
# Key files:
# - transactions.txt (multi-document ACID transactions)
# - replica-set-*.txt (high availability and replication)
# - sharding-*.txt (horizontal scaling and data distribution)
# - aggregation-pipeline.txt (data processing pipelines)
# - indexes/ (indexing strategies and types)
# - csfle/ (Client-Side Field Level Encryption)
# - queryable-encryption/ (Queryable Encryption with encrypted search)
# - security-*.txt (authentication, authorization, encryption)

# View reference documentation structure
ls /tmp/context7-isolated-f4CaGL/repo/source/reference/
# - command/ (database commands: insert, find, update, etc.)
# - operator/ (query, aggregation, update operators)
# - method/ (shell methods organized by category)
# - configuration-options.txt (mongod/mongos configuration)
# - bson-types.txt (BSON data types)
```

## In-Use Encryption Features

CSFLE and Queryable Encryption documentation

The manual includes comprehensive documentation for MongoDB's encryption features: Client-Side Field Level Encryption (CSFLE) and Queryable Encryption (QE). These sections in `source/core/csfle/` and `source/core/queryable-encryption/` provide architecture overviews, implementation guides, and detailed tutorials with runnable code examples for multiple key management services (AWS KMS, Azure Key Vault, GCP KMS, KMIP-compliant providers, and local testing).

```rst
.. File: /tmp/context7-isolated-f4CaGL/repo/source/core/queryable-encryption.txt (excerpt)

=====================
Queryable Encryption
=====================

{+qe-equality-ga+} is generally available (GA) in MongoDB 7.0 and later.

Queryable Encryption is a feature that enables you to encrypt sensitive data
in your application before it is sent to MongoDB, while still allowing you
to query the encrypted data. This provides an additional layer of security
for sensitive workloads, ensuring that only applications with access to the
encryption keys can decrypt and read the data.

Key Concepts
------------

**Data Encryption Keys (DEK)**
   Keys used to encrypt individual fields in documents. Stored encrypted in
   the Key Vault collection.

**Customer Master Key (CMK)**
   Master key stored in a Key Management Service (KMS) that encrypts DEKs.

**Key Vault Collection**
   MongoDB collection storing encrypted Data Encryption Keys.

**Encrypted Field Configuration**
   Schema defining which fields should be encrypted and with what algorithm.
```

```bash
# Browse encryption documentation
ls /tmp/context7-isolated-f4CaGL/repo/source/core/queryable-encryption/
# Output: fundamentals/, tutorials/, reference/
#         Quick-start guides, key management, encryption schemas

# View generated encryption examples
ls /tmp/context7-isolated-f4CaGL/repo/source/includes/generated/in-use-encryption/
# Output: csfle/, queryable-encryption/
#         Examples for: node/, python/, java/, csharp/, go/, mongosh/
#         KMS providers: aws/, azure/, gcp/, kmip/, local/

# Check tutorial structure
ls /tmp/context7-isolated-f4CaGL/repo/source/includes/qe-tutorials/
# Output: node/, python/, csharp/, java/, go/, mongosh/
#         Each contains: README.md, tutorial files, helper functions, package config
```

## Reference Documentation

Comprehensive API and operator reference

The reference section provides exhaustive documentation for all MongoDB database commands, query and aggregation operators, shell methods, configuration options, and BSON data types. Commands are organized by category (CRUD, aggregation, replication, sharding, administration), and operators are grouped by function (comparison, logical, array, text, geospatial). Each reference entry includes syntax, parameters, examples, and version information.

```rst
.. File: /tmp/context7-isolated-f4CaGL/repo/source/reference/operator/query/gt.txt (conceptual)

====
$gt
====

.. default-domain:: mongodb

.. contents:: On this page
   :local:
   :backlinks: none
   :depth: 1

Definition
----------

.. query:: $gt

   *Syntax*: ``{ field: { $gt: value } }``

   :query:`$gt` selects those documents where the value of the
   ``field`` is greater than (i.e. ``>``) the specified ``value``.

Behavior
--------

For comparison of different BSON type values, see the
:ref:`BSON comparison order <bson-types-comparison-order>`.

Examples
--------

The following examples use the ``inventory`` collection:

.. code-block:: javascript

   db.inventory.insertMany( [
      { item: "nuts", quantity: 30 },
      { item: "bolts", quantity: 50 },
      { item: "washers", quantity: 10 }
   ] )

Query for Greater Than
~~~~~~~~~~~~~~~~~~~~~~

Select all documents where ``quantity`` is greater than ``20``:

.. code-block:: javascript

   db.inventory.find( { quantity: { $gt: 20 } } )

This query returns:

.. code-block:: javascript

   { item: "nuts", quantity: 30 }
   { item: "bolts", quantity: 50 }
```

```bash
# Browse query operators
ls /tmp/context7-isolated-f4CaGL/repo/source/reference/operator/query/
# Comparison: $eq, $gt, $gte, $lt, $lte, $ne, $in, $nin
# Logical: $and, $or, $not, $nor
# Element: $exists, $type
# Array: $all, $elemMatch, $size

# View aggregation operators
ls /tmp/context7-isolated-f4CaGL/repo/source/reference/operator/aggregation/
# Pipeline stages: $match, $group, $project, $sort, $limit, $lookup
# Operators: $sum, $avg, $min, $max, $concat, $dateToString

# Browse shell methods
ls /tmp/context7-isolated-f4CaGL/repo/source/reference/method/
# Categories: js-collection, js-database, js-cursor, js-replication,
#             js-sharding, js-user-management, js-bulk
```

## Tutorial Structure

Practical how-to guides

The tutorial section contains step-by-step guides for common MongoDB tasks including installation, deployment, configuration, and operational procedures. Tutorials cover replica set deployment and maintenance, sharded cluster configuration, backup and restoration strategies, security configuration (authentication, authorization, TLS/SSL), performance optimization, and upgrade procedures.

```rst
.. File: /tmp/context7-isolated-f4CaGL/repo/source/tutorial/deploy-replica-set.txt (conceptual)

=====================
Deploy a Replica Set
=====================

.. contents:: On this page
   :local:
   :backlinks: none
   :depth: 1

Overview
--------

This tutorial describes how to create a three-member replica set
from three existing :binary:`~bin.mongod` instances running with
:setting:`~security.authorization` enabled.

Prerequisites
-------------

- Three MongoDB instances running on separate servers
- Network connectivity between all members
- Authentication enabled with keyfile or x.509 certificates

Procedure
---------

.. procedure::
   :style: normal

   .. step:: Start each MongoDB instance

      On each server, start :binary:`~bin.mongod` with replication enabled:

      .. code-block:: bash

         mongod --replSet rs0 --port 27017 --bind_ip localhost,<hostname>
                --keyFile /path/to/keyfile --dbpath /data/db

   .. step:: Connect to one MongoDB instance

      .. code-block:: bash

         mongosh --host <hostname> --port 27017

   .. step:: Initiate the replica set

      .. code-block:: javascript

         rs.initiate({
           _id: "rs0",
           members: [
             { _id: 0, host: "mongodb0.example.net:27017" },
             { _id: 1, host: "mongodb1.example.net:27017" },
             { _id: 2, host: "mongodb2.example.net:27017" }
           ]
         })
```

```bash
# Browse tutorial categories
ls /tmp/context7-isolated-f4CaGL/repo/source/tutorial/ | grep -E "(deploy|install|configure|backup)"
# Deployment: deploy-replica-set.txt, deploy-sharded-cluster.txt
# Installation: install-mongodb-on-*.txt, install-mongodb-enterprise-on-*.txt
# Configuration: configure-*.txt, enable-authentication.txt
# Backup: backup-*.txt, restore-*.txt

# View administration tutorials
ls /tmp/context7-isolated-f4CaGL/repo/source/tutorial/ | grep -E "(backup|security|performance)"
# Security: authenticate-*.txt, configure-ldap.txt, configure-x509.txt
# Performance: analyze-query-plan.txt, manage-indexes.txt
# Backup: backup-with-filesystem-snapshots.txt, backup-sharded-cluster-*.txt
```

## Version and Release Management

Version constants and deprecation notices

The documentation includes version-specific information managed through constants in `snooty.toml` and banners targeting specific pages. Version 7.2 constants include current version, development version, last LTS version, and package names. Banners provide warnings for deprecated features, preview features, and archived documentation versions.

```toml
# File: /tmp/context7-isolated-f4CaGL/repo/snooty.toml (excerpt)
[constants]
version = "7.2"
release = "7.2.1"
version-dev = "7.3"
version-last = "7.0"
latest-lts-version = "7.0"
minimum-lts-version = "5.0"

[[banners]]
targets = ["core/queryable-encryption.txt", "core/queryable-encryption/*.txt"]
variant = "warning"
value = """
{+qe-equality-ga+} is generally available (GA) in MongoDB 7.0 and later.
The {+qe-preview+}, released in version 6.0, is no longer supported.
"""

[[banners]]
targets = ["*"]
variant = "info"
value = """
This version of the documentation is archived and no longer supported.
View the current documentation to learn how to upgrade your MongoDB server.
"""
```

```rst
.. Example version directive usage in source files
.. versionadded:: 7.0
   Queryable Encryption with equality queries is generally available.

.. versionchanged:: 7.2
   The :dbcommand:`bulkWrite` command now supports ordered and unordered operations.

.. deprecated:: 7.0
   The :method:`db.collection.mapReduce()` method is deprecated.
   Use aggregation pipeline with :pipeline:`$group` instead.
```

## Cross-Documentation References

Intersphinx linking system

The MongoDB Manual uses Sphinx's intersphinx extension to create cross-references to other MongoDB documentation properties including MongoDB Atlas, database tools, MongoDB Shell, Compass, and various driver documentation. These references are defined in `snooty.toml` and enable seamless linking between documentation sets using role directives like `:atlas:`, `:manual:`, and `:mongosh:`.

```toml
# File: /tmp/context7-isolated-f4CaGL/repo/snooty.toml (excerpt)
intersphinx = [
    "https://pymongo.readthedocs.io/en/stable/objects.inv",
    "https://motor.readthedocs.io/en/stable/objects.inv",
    "https://www.mongodb.com/docs/atlas/objects.inv",
    "https://www.mongodb.com/docs/compass/current/objects.inv",
    "https://www.mongodb.com/docs/database-tools/objects.inv",
    "https://www.mongodb.com/docs/mongodb-shell/objects.inv"
]
```

```rst
.. Example cross-reference usage patterns

For cloud deployments, see :atlas:`Create a Cluster </tutorial/create-new-cluster>`.

Use :mongosh:`mongosh </reference>` to connect to your database.

The :binary:`~bin.mongodump` and :binary:`~bin.mongorestore` tools are documented
in :dbtools:`MongoDB Database Tools </>`.

For driver-specific implementations, see:
- :node-docs:`MongoDB Node.js Driver </>`
- :pymongo:`PyMongo Documentation </>`
- :java-docs:`MongoDB Java Driver </>`
```

---

## Summary

The MongoDB Server Manual is the definitive technical reference for MongoDB database server version 7.2, providing comprehensive documentation for all database features, operations, and administrative tasks. Built with Sphinx and the Snooty documentation platform, the manual combines detailed conceptual explanations, complete API reference documentation, and practical tutorials with tested code examples across multiple programming languages. The documentation structure supports MongoDB's core feature areas including CRUD operations, aggregation pipelines, replication for high availability, sharding for horizontal scaling, multi-document ACID transactions, comprehensive security features (authentication, authorization, encryption at rest and in transit), and advanced encryption capabilities through Client-Side Field Level Encryption and Queryable Encryption.

Primary use cases include: database administrators referencing configuration options and deployment procedures; developers learning MongoDB query syntax, operators, and best practices; security engineers implementing encryption and access control; architects designing replica set and sharded cluster topologies; and operations teams performing backup, monitoring, and performance tuning tasks. The documentation's integration patterns emphasize cross-referencing with other MongoDB documentation properties (Atlas, tools, drivers), version-specific guidance with clear deprecation notices and feature availability, runnable code examples demonstrating real-world usage patterns, and comprehensive reference material covering every database command, operator, and configuration option. This architecture ensures MongoDB users have authoritative, accurate, and practical documentation for successfully deploying and operating MongoDB database servers across all supported versions and deployment topologies.
