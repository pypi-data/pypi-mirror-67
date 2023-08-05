import unittest
import snapshottest
import requests
from des_process import product

class TestProducts(snapshottest.TestCase):

  def setUp(self):
    self.url = "http://scienceportal-dev.linea.gov.br/api/graphql"

  def test_all(self):
    query = """{
      productsList(first: 5) {
        edges {
          node {
            productId
            processId
            fileId
            jobId
            tableId
            classId
            flagRemoved
            displayName
            version
            selectedName
            table {
              tableId
              tableName
              schemaName
            }
          }
        }
      }
    }"""

    response = requests.post(self.url, json={ 'query': query })
    self.assertMatchSnapshot(response.json()['data'])

  def test_by_id(self):
    query = """{
      productByProductId(productId: 310867) {
        productId
        processId
        fileId
        jobId
        tableId
        classId
        flagRemoved
        displayName
        version
        selectedName
        table {
          tableId
          tableName
          schemaName
        }
      }
    }"""

    response = requests.post(self.url, json={ 'query': query })
    self.assertMatchSnapshot(response.json()['data'])

  def test_by_process_id(self):
    query = """{
      productsByProcessId(processId: 10034331) {
        productId
        processId
        fileId
        jobId
        tableId
        classId
        flagRemoved
        displayName
        version
        selectedName
        table {
          tableId
          tableName
          schemaName
        }
      }
    }"""

    response = requests.post(self.url, json={ 'query': query })
    self.assertMatchSnapshot(response.json()['data'])



  def test_by_name(self):
    query = """{
      productsList(displayName: "ExpTime Sum 51") {
        edges {
          node {
            productId
            processId
            fileId
            jobId
            tableId
            classId
            flagRemoved
            displayName
            version
            selectedName
            table {
              tableId
              tableName
              schemaName
            }
          }
        }
      }
    }"""

    response = requests.post(self.url, json={ 'query': query })
    self.assertMatchSnapshot(response.json()['data'])

  def test_by_tag_id(self):
    query = """{
      productsList(first: 5, tagId: 4) {
        edges {
          node {
            productId
            processId
            fileId
            jobId
            tableId
            classId
            flagRemoved
            displayName
            version
            selectedName
            table {
              tableId
              tableName
              schemaName
            }
          }
        }
      }
    }"""

    response = requests.post(self.url, json={ 'query': query })
    self.assertMatchSnapshot(response.json()['data'])

  def test_field_id(self):
    query = """{
      productsList(first: 5, fieldId: 50) {
        edges {
          node {
            productId
            processId
            fileId
            jobId
            tableId
            classId
            flagRemoved
            displayName
            version
            selectedName
            table {
              tableId
              tableName
              schemaName
            }
          }
        }
      }
    }"""

    response = requests.post(self.url, json={ 'query': query })
    self.assertMatchSnapshot(response.json()['data'])


  def test_type_id(self):
    query = """{
      productsList(first: 5, typeId: 24) {
        edges {
          node {
            productId
            processId
            fileId
            jobId
            tableId
            classId
            flagRemoved
            displayName
            version
            selectedName
            table {
              tableId
              tableName
              schemaName
            }
          }
        }
      }
    }"""


    response = requests.post(self.url, json={ 'query': query })
    self.assertMatchSnapshot(response.json()['data'])


  def test_class_id(self):
    query = """{
      productsList(first: 5, classId: 128) {
        edges {
          node {
            productId
            processId
            fileId
            jobId
            tableId
            classId
            flagRemoved
            displayName
            version
            selectedName
            table {
              tableId
              tableName
              schemaName
            }
          }
        }
      }
    }"""

    response = requests.post(self.url, json={ 'query': query })
    self.assertMatchSnapshot(response.json()['data'])