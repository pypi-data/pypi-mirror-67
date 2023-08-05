"""Tools for interacting with MongoDB databases."""

import copy

from pymongo import MongoClient
import alfred3


class MongoDBConnector:
    """Connect to a MongoDB database or collection.

    Effectively, this class provides an interface to an instace of ``pymongo.MongoClient``. For further information on how to interact with a `MongoClient`, please refer to the `pymongo documentation <https://pymongo.readthedocs.io/en/stable/tutorial.html>`_.
    
    :param str host: Hostname or IP address.
    :param int port: Port number on which to connect.
    :param str username: Username for authentication.
    :param str password: Password for authentication.
    :param str database: Database to which to the client will connect.
    :param str collection: Collection inside the specified database to which the client will connect. If left empty, the client will connect directly to the database.
    :param str auth_source: Database to authenticate on. Defaults to "admin", the MongoDB default.
    :param bool ssl: If ``True``, create a connection to the server using Transport Layer Security (TLS/SSL).
    :param str ca_file: Filepath to a file containing a single or a bundle of “certification authority” certificates, which are used to validate certificates passed from the other end of the connection. Implies ``ssl=True``. Defaults to ``None``.
    """

    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        database: str,
        collection: str = None,
        auth_source: str = "admin",
        ssl: bool = False,
        ca_file: str = None,
    ):
        """Constructor method."""

        self._host = host
        self._port = port
        self._db_name = database
        self._collection = collection
        self._username = username
        self._password = password
        self._auth_source = auth_source
        self._ssl = True if ca_file else ssl
        self._ca_file = ca_file

        self._client = None
        self._db = None

        self.connected = False
        """`True`, if a connection was established."""

    def connect(self):
        """Establish the connection the MongoDB.

        If a collection was specified upon initialisation, the `MongoDBConnector` will connect to this collection. Else, it will connect to the specified database.
        """

        self._client = MongoClient(
            host=self._host,
            port=self._port,
            username=self._username,
            password=self._password,
            authSource=self._auth_source,
            tls=self._ssl,
            tlsCAFile=self._ca_file,
        )

        db = self._client[self._db_name]

        if self._collection:
            db = db[self._collection]

        self._db = db
        self.connected = True

    def disconnect(self):
        """Close the connection to the database."""

        self._client.close()
        self.connected = False

    @property
    def db(self):
        """Return the database or, if specified, collection given upon initialisation.
        
        If the instance of ``MongoDBConnector`` is not currently connected, a call to this property will trigger a call to ``MongoDBConnector.connect()`` before returning the database or collection.
        """

        if self.connected:
            if self._db is None:
                raise TypeError("No collection found.")
            else:
                return self._db
        
        elif not self.connected:
            self.connect()
            if self._db is None:
                raise TypeError("No collection found.")
            else:
                return self._db


class ExpMongoDBConnector:
    """Connect to an alfred experiment's MongoDB collection.
    
    Connects to the same database and collection that the given alfred experiment uses to save its data. If multiple `MongoSavingAgents` are attached to the experiment, ``ExpMongoDBConnector`` will connect to the ``MongoSavingAgent`` with the lowest activation level. Basically, it provides access to a copy of the ``pymongo.MongoClient`` that the experiment's saving agent uses. For further information on how to interact with a `MongoClient`, please refer to the `pymongo documentation <https://pymongo.readthedocs.io/en/stable/tutorial.html>`_.

    :param experiment: An instance of ``alfred.Experiment``.
    :type experiment: class: `alfred.Experiment`
    :raise: ValueError if not initialised with an alfred experiment.
    """

    def __init__(self, experiment):
        """Constructor method."""

        self._exp = experiment
        self._agents = None

        self._client = None
        self._collection = None

        self.connected = False
        """`True`, if a connection was established."""

        if not isinstance(self._exp, alfred3.Experiment):
            raise ValueError("The input must be an instance of alfred.Experiment.")

    def _gather_agents(self):
        """Collect all MongoSavingAgents from the provided alfred experiment, sorted by activation level (lowest first)."""

        self._agents = []
        for agent in self._exp.saving_agent_controller._agents:
            if isinstance(agent, alfred3.saving_agent.MongoSavingAgent):
                self._agents.append(copy.copy(agent))
        if not self._agents:
            raise ValueError(
                "Your experiment needs at least one MongoSavingAgent for ExpMongoDBConnector to work."
            )
        self._agents.sort(key=lambda x: x.activation_level)

    def connect(self):
        """Establish a connection to the experiment's MongoDB with the lowest activation level."""

        self._gather_agents()

        if (
            len(self._agents) > 1
            and self._agents[0].activation_level == self._agents[1].activation_level
        ):
            raise ValueError(
                "There are two or more MongoSavingAgents with the highest activation level."
            )

        self._client = self._agents[0]._mc
        self._collection = self._agents[0]._col
        self.connected = True

    def disconnect(self):
        """Close the connection to the database."""

        if self.connected:
            self._client.close()
            self.connected = False

    @property
    def db(self):
        """Return the MongoClient collection from the experiments' ``MongoSavingAgent`` with lowest activation level.
        
        If the instance of ``ExpMongoDBConnector`` is not currently connected, a call to this property will trigger a call to ``ExpMongoDBConnector.connect()`` before returning the collection.
        """

        if self.connected:
            if self._collection is None:
                raise TypeError("No collection found.")
            else:
                return self._collection
        
        elif not self.connected:
            self.connect()
            if self._collection is None:
                raise TypeError("No collection found.")
            else:
                return self._collection

    @property
    def list_agents(self):
        """Return a list of all ``MongoSavingAgents`` belonging to the given alfred experiment."""
        if self._agents:
            return self._agents
        else:
            self._gather_agents()
            return self._agents
