from locust import TaskSet, HttpUser, task, between
import json
import random
import sys
import resource

headers = { 'Authorization': 'Basic dGVzdDp4eXp6eQ==', 'Accept': 'application/sparql-results+json' }
class SearchTasks(TaskSet):
  @task(4)
  def getAssetsByDepiction(self):
    get_depictions_query = '''
      SELECT ?d ?p ?o
      WHERE {
        ?d a <https://vocabularies.sauce-project.tech/core/Asset> ;
          ?p ?o .
      }
    '''
    query = 'query=' + get_depictions_query
    try:
      response = self.client.get('/repositories/sauce', name='get all depictions', params=query, headers=headers)
    except Exception as err:
      print(err)
    if response.ok:
      body = json.loads(response.text)
      depictions = []
      for item in body['results']['bindings']:
        if item['d']['value'] not in depictions:
          depictions.append(item['d']['value'])
      depiction = None
      if len(depictions) > 0:
        depiction = depictions[random.randint(0, len(depictions) - 1)]
      if depiction:
        get_assets_with_depiction_query = '''
          SELECT ?s ?p ?o
          WHERE {
            ?s a <https://vocabularies.sauce-project.tech/core/Asset> ;
              <https://vocabularies.sauce-project.tech/core/depicts> <''' + depiction + '''> ;
              ?p ?o
          }
        '''
        query = 'query=' + get_assets_with_depiction_query
        try:
          asset_response = self.client.get('/repositories/sauce', name='get assets with depiction', params=query, headers=headers)
        except Exception as err:
          print(err)
        if asset_response.ok:
          pass
  
  @task(2)
  def searchForAssets(self):
    get_assets_query = '''
      SELECT ?s ?p ?o
      WHERE {
        ?s a <https://vocabularies.sauce-project.tech/core/Asset> ;
          <https://vocabularies.sauce-project.tech/core/title> ?title ;
          ?p ?o .
      }
      ORDER BY ASC(?title)
    '''
    query = 'query=' + get_assets_query
    try:
      response = self.client.get('/repositories/sauce', name='get all assets', params=query, headers=headers)
    except Exception as err:
      print(err)
    pass
    if response.ok:
      body = json.loads(response.text)
      # print(body['results'])
      assets = []
      for item in body['results']['bindings']:
        if item['s']['value'] not in assets:
          assets.append(item['s']['value'])
      asset = None
      if len(assets) > 0:
        asset = assets[random.randint(0, len(assets) - 1)]
      if asset:
        get_asset_query = '''
          SELECT ?p ?o
          WHERE {
            <''' + asset + '''> ?p ?o .
          }
        '''
        query = 'query=' + get_asset_query
        try:
          asset_response = self.client.get('/repositories/sauce', name='get an asset from results', params=query, headers=headers)
        except Exception as err:
          print(err)
        if asset_response.ok:
          pass
    
  @task(1)
  def stop(self):
    self.interrupt()

class SauceUser(HttpUser):
  wait_time = between(3, 15)
  tasks = [SearchTasks]