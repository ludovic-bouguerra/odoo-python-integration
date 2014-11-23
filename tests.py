import unittest

from odoo import OdooConnector
from mock import patch, call, MagicMock

class XmlRpcMockClient:
    def __init__(self):
        self.execute = MagicMock()
        self.login = MagicMock(return_value="UID")

class OdooConnectorTest(unittest.TestCase):
    """
        Todo Refactoriser les tests

    """

    def setUp(self):
        self._username = "username"
        self._password = "password"
        self._database = "database"
        self._url = "http://example.com:8069/"
        
        self.o = OdooConnector(self._username, self._password, self._database, self._url)

    def _assert_call_login(self, mock_server_proxy):
        expected_params_server_proxy = [call("http://example.com:8069/xmlrpc/common"), call("http://example.com:8069/xmlrpc/object")]
        self.assertEquals(expected_params_server_proxy, mock_server_proxy.call_args_list)
        

    @patch('xmlrpclib.ServerProxy')
    def test_create(self, mock_server_proxy):
        """

        """
        mock_server_proxy.return_value = XmlRpcMockClient()

        obj = {"name": "test"} 
        self.o.create("res.partner", obj)
                
        self._assert_call_login(mock_server_proxy)
        mock_server_proxy.return_value.execute.assert_called_once_with(self._database, "UID", self._password, "res.partner", "create", obj)
    

    @patch('xmlrpclib.ServerProxy')
    def test_search(self, mock_server_proxy):
        """

        """

        mock_server_proxy.return_value = XmlRpcMockClient()
        
        search_params = [('name', 'ilike', "test")]
        model = "res.partner"
        
        self.o.search(model,  search_params)


        self._assert_call_login(mock_server_proxy)

        mock_server_proxy.return_value.execute.assert_called_once_with(self._database, "UID", self._password, model, "search", search_params)
    
    

    @patch('xmlrpclib.ServerProxy')
    def test_update(self, mock_server_proxy):
        """

        """
        mock_server_proxy.return_value = XmlRpcMockClient()
        
        obj = {"name" : "test"}
        id = 10
        model = "res.partner"
        
        self.o.update(model, id, obj)

        self._assert_call_login(mock_server_proxy)

        mock_server_proxy.return_value.execute.assert_called_once_with(self._database, "UID", self._password, model, "write", id, obj)

    def test_return_one(self):
        array_one_value = [0]
        array_two_values = [0, 1]
        array_empty = []

        self.assertEquals(0, self.o.return_one(array_one_value))
        self.assertEquals(0, self.o.return_one(array_two_values))
        self.assertEquals(None, self.o.return_one(array_empty))


if __name__ == '__main__':
    unittest.main() 