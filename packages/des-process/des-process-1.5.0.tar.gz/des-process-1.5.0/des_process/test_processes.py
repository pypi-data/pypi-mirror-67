import unittest
import snapshottest
import requests
from des_process import process

class TestProcesses(snapshottest.TestCase):

  def setUp(self):
    self.url = "http://scienceportal-dev.linea.gov.br/api/graphql"

  def test_all(self):
    query = """{
      processesList(first: 5) {
        edges {
          node {
            processId
            startTime
            endTime
            name
            productLog
            processDir
            size
            processStatus {
              displayName
            }
          }
        }
      }
    }"""


    response = requests.post(self.url, json={ 'query': query })
    self.assertMatchSnapshot(response.json()['data'])