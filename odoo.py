# -*- coding: utf8 -*-

import xmlrpclib

class OdooConnector:
    def __init__(self, username, password, database, server_url):
        """Create a new OdooConnector instance

        Args:
            username : Username
            password : The password                
            database : The odoo database name
            server_url : The url of odoo server ending with / and including the port
                exemple : http://localhost:8069/

        Returns:
            id of new record
        """
        self._username = username
        self._password = password
        self._server_url = server_url
        self._database = database
        self._uid = None
        self._sock = None



    def _connect(self):
        if(self._uid is None):
            sock_common = xmlrpclib.ServerProxy ("%s%s"%(self._server_url, 'xmlrpc/common'))
            self._sock = xmlrpclib.ServerProxy("%s%s"%(self._server_url, 'xmlrpc/object'))
            self._uid = sock_common.login(self._database, self._username, self._password)

    def create(self, model, obj):		
        """Create a new record in odoo

        Args:
            model: String represent the model id in odoo like res.parner or product.product
            obj : An dict with data you want to save
                Exemple : Save a res.partner with name Ludovic
                { "name": "Ludovic"}

        Returns:
            id of new record
        """
        self._connect()
        return self._sock.execute(self._database, self._uid, self._password, model, 'create', obj)

    def search(self, model, params):
        """Search records

        Args:
            model: String represent the model id in odoo like res.parner or product.product
            params : [('name', 'ilike', "test")])

        Returns:
            (Array) ids of records according with the search keywords
        """        
        self._connect()
        return self._sock.execute(self._database, self._uid, self._password, model, 'search', params)


    def update(self, model, id, obj):
        """Update an existing record in odoo

        Args:
            model: String represent the model id in odoo like res.parner or product.product
            id: Id of the existing record
            obj : An dict with data you want to update
                Exemple : Update a res.partner with name Ludovic
                { "name": "Ludovic"}

        Returns:
           
        """
        self._connect()
        return self._sock.execute(self._database, self._uid, self._password, model, 'write', id, obj)

    def return_one(self, array):
        """Return the first element in a array or None

        Args:
            array: An array
        Returns:
            The first element or None
        """
        if (len(array) > 0):
            return array[0]
        else:
            return None