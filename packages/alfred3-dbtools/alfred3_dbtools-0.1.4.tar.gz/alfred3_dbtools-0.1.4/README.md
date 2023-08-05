# alfred3_dbtools

This module provides additional tools for working with databases in the context of alfred3 experiments (see [alfred3 on GitHub](https://github.com/ctreffe/alfred)).

## Installation

```bash
pip install alfred3_dbtools
```

## Usage

To import the tools for working with mongodb, include this statement at the beginning of your script:

```python
from alfred3_dbtools import mongotools
```

You can then access the classes provided in the module:

- `mongotools.MongoDBConnector` can be used to establish an independent connection to an instance of `pymongo.MongoClient`. 
    - Access to the client is provided via `mongotools.MongoDBConnector.db`. This will return either a database instance or, if a specific collection was given during initialisation, that collection instance.
    - See `help(mongotools.MongoDBConnector)` for details.

- `mongotools.ExpMongoDBConnector` can be used to establish a connection to an experiments' MongoDBs.
    - The constructor takes one parameter: `experiment`, which needs to be an alfred experiment. See `help(mongotools.ExpMongoDBConnector)` for details.
    - `mongotools.ExpMongoDBConnector.db` will return the MongoDB **collection** of the `MongoSavingAgent` with the lowest activation level (i.e. the primary `MongoSavingAgent`). It will raise a `ValueError`, if the lowest activation level is occupied by two or more `MongoSavingAgent`s.
    - `mongotools.ExpMongoDBConnector.list_agents` will return a list of all `MongoSavingAgent`s added to the experiment.
    - Your experiment needs to have at least **one MongoSavingAgent** for this class to work.

Refer to the [pymongo documentation](https://pymongo.readthedocs.io/en/stable/tutorial.html) for further details on how to interact with the clients.
