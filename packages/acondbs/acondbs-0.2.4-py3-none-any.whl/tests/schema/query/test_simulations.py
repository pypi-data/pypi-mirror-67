import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
        { allSimulations {
             edges { node { name } }
           } }
         ''',
        id='allSimulations'
    ),
    pytest.param(
        '''
        { simulation(simulationId: 1001) { name } }
         ''',
        id='simulationBySimulationID'
    ),
    pytest.param(
        '''
        { simulation(simulationId: 2001) { name } }
         ''',
        id='simulationBySimulationID-nonexistent'
    ),
]

@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    client = Client(schema)
    with app.app_context():
        snapshot.assert_match(client.execute(query))

##__________________________________________________________________||
