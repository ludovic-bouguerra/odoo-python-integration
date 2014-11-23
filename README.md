odoo-python-integration
=======================

Base for integrate odoo webservice with your Python apps

TODO : Refactoriser tests unitaires
Ajouter la fonction read

For testing, installing dependencies :
pip install -r test_requirements.txt 

Usage : 

1/ Create a partner with name "Ludovic" 

o = OdooConnector(self._username, self._password, self._database, self._url)
o.create("res.partner", {name:"Ludovic"})

2/ Search a partner with name like Ludovic
the_id = o.search("res.partner", [('name', 'ilike', "test")])

the_id = id of partner


3/ Update partner 
Set name = test to partner id = 10
o.update("res.partner", 10, {name : "test"})

