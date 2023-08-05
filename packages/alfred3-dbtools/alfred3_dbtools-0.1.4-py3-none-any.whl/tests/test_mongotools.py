import unittest
import os
import copy

import pymongo
import alfred3

from alfred3_dbtools import mongotools


class TestMongoDBConnector(unittest.TestCase):
    def setUp(self):
        self._host = os.environ.get("MONGODB_TESTHOST")
        self._port = int(os.environ.get("MONGODB_TESTPORT"))
        self._user1 = os.environ.get("MONGODB_TESTUSER")
        self._pw1 = os.environ.get("MONGODB_TESTPW")
        self._db = os.environ.get("MONGODB_TESTDB")
        self._col = os.environ.get("MONGODB_TESTCOL")
        self._user2 = os.environ.get("MONGODB_TESTUSER2")
        self._pw2 = os.environ.get("MONGODB_TESTPW2")
        self._auth_source = os.environ.get("MONGODB_TEST2AUTH")

    def test_minimal_connect(self):
        con = mongotools.MongoDBConnector(
            host=self._host,
            port=self._port,
            username=self._user1,
            password=self._pw1,
            database=self._db,
        )
        con.connect()
        self.assertTrue(con.connected)
        self.assertIsInstance(con.db, pymongo.database.Database)

    def test_auth_source_connect(self):
        con = mongotools.MongoDBConnector(
            host=self._host,
            port=self._port,
            username=self._user2,
            password=self._pw2,
            database=self._db,
            auth_source=self._auth_source,
        )
        con.connect()
        self.assertTrue(con.connected)
        self.assertIsInstance(con.db, pymongo.database.Database)

    def test_collection_connect(self):
        con = mongotools.MongoDBConnector(
            host=self._host,
            port=self._port,
            username=self._user2,
            password=self._pw2,
            database=self._db,
            collection=self._col,
            auth_source=self._auth_source,
        )
        con.connect()
        self.assertTrue(con.connected)
        self.assertIsInstance(con.db, pymongo.collection.Collection)

    def test_autoconnect(self):
        con = mongotools.MongoDBConnector(
            host=self._host,
            port=self._port,
            username=self._user2,
            password=self._pw2,
            database=self._db,
            collection=self._col,
            auth_source=self._auth_source,
        )
        self.assertFalse(con.connected)
        col = con.db
        self.assertTrue(con.connected)
        print(col)
        self.assertIsInstance(col, pymongo.collection.Collection)

    def test_disconnect(self):
        con = mongotools.MongoDBConnector(
            host=self._host,
            port=self._port,
            username=self._user2,
            password=self._pw2,
            database=self._db,
            collection=self._col,
            auth_source=self._auth_source,
        )
        con.connect()
        self.assertIsInstance(con.db, pymongo.collection.Collection)
        con.disconnect()
        self.assertFalse(con.connected)

    def test_insert_find_remove(self):
        con = mongotools.MongoDBConnector(
            host=self._host,
            port=self._port,
            username=self._user2,
            password=self._pw2,
            database=self._db,
            collection=self._col,
            auth_source=self._auth_source,
        )
        col = con.db
        test_document = {"test": "test"}

        col.insert_one(test_document)
        query = col.find_one(test_document)
        self.assertIsNotNone(query)

        col.delete_one(test_document)
        delquery = col.find_one(test_document)
        self.assertIsNone(delquery)


class TestExpMongoDBConnector(unittest.TestCase):
    def setUp(self):
        self._host = os.environ.get("MONGODB_TESTHOST")
        self._port = int(os.environ.get("MONGODB_TESTPORT"))
        self._user = os.environ.get("MONGODB_TESTUSER2")
        self._pw = os.environ.get("MONGODB_TESTPW2")
        self._db = os.environ.get("MONGODB_TESTDB")
        self._col = os.environ.get("MONGODB_TESTCOL")
        self._auth_source = os.environ.get("MONGODB_TEST2AUTH")

        self.exp = alfred3.Experiment()

        self.agent = alfred3.saving_agent.MongoSavingAgent(
            host=self._host + ":" + str(self._port),
            database=self._db,
            collection=self._col,
            user=self._user,
            password=self._pw,
            experiment=self.exp,
            auth_source=self._auth_source,
            use_ssl=False,
            ca_file_path=None,
            activation_level=10
        )

        self.exp.saving_agent_controller.add_saving_agent(self.agent)
        self.connector = mongotools.ExpMongoDBConnector(self.exp)
    
    def tearDown(self):
        self.exp = None
        self.connector = None

    def test_connect(self):
        self.connector.connect()
        col = self.connector.db
        self.assertIsInstance(col, pymongo.collection.Collection)
        self.assertTrue(self.connector.connected)
    
    def test_autoconnect(self):
        self.assertFalse(self.connector.connected)

        col = self.connector.db
        self.assertIsInstance(col, pymongo.collection.Collection)
        self.assertTrue(col.connected)
    
    def test_change(self):
        
        self.connector.connect()
        agent = self.connector._agents[0]
        agent.activation_level = 9

        self.assertEqual(agent.activation_level, 9)
        self.assertEqual(self.exp.saving_agent_controller._agents[1].activation_level, 10)
    
    def test_multi_agent_handling(self):
        agent2 = copy.copy(self.agent)
        agent3 = copy.copy(self.agent)
        agent4 = copy.copy(self.agent)
        
        agent2.activation_level = 10
        agent3.activation_level = 9
        agent4.activation_level = 9

        # additional agent, same level
        self.exp.saving_agent_controller.add_saving_agent(agent2)
        connector1 = mongotools.ExpMongoDBConnector(self.exp)
        self.assertRaises(ValueError, self.connector.connect)
        self.assertRaises(ValueError, connector1.connect)

        # third agent, lower level
        self.exp.saving_agent_controller.add_saving_agent(agent3)
        col = self.connector.db
        self.assertTrue(self.connector.connected)
        self.assertIsInstance(col, pymongo.collection.Collection)

        # fourth agent, same level as third
        self.exp.saving_agent_controller.add_saving_agent(agent4)
        connector2 = mongotools.ExpMongoDBConnector(self.exp)
        self.assertRaises(ValueError, self.connector.connect)
        self.assertRaises(ValueError, connector2.connect)
    
    def test_insert_find_remove(self):
        self.connector.connect()
        col = self.connector.db

        test_document = {"test": "test"}

        col.insert_one(test_document)
        query = col.find_one(test_document)
        self.assertIsNotNone(query)

        col.delete_one(test_document)
        delquery = col.find_one(test_document)
        self.assertIsNone(delquery)
    
    def test_list_agents(self):
        agent2 = copy.copy(self.agent)
        agent3 = copy.copy(self.agent)
        
        agent2.activation_level = 10
        agent3.activation_level = 9

        self.exp.saving_agent_controller.add_saving_agent(agent2)
        self.exp.saving_agent_controller.add_saving_agent(agent3)

        connector = mongotools.ExpMongoDBConnector(self.exp)
        agents_list = connector.list_agents

        self.assertEqual(len(agents_list), 3)
    
    def test_client(self):
        self.assertFalse(self.connector.connected)
        self.connector.connect()
        self.assertIsInstance(self.connector._client, pymongo.MongoClient)
    
    def test_input(self):
        with self.assertRaises(ValueError):
            mongotools.ExpMongoDBConnector("test")
    
    def test_no_mongo_agent(self):
        exp = alfred3.Experiment()
        with self.assertRaises(ValueError):
            connector = mongotools.ExpMongoDBConnector(exp)
            connector.connect()


if __name__ == "__main__":
    unittest.main()
