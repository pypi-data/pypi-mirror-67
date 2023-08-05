#coding: utf-8

import requests

class Processes:

  def __init__(self):
    self.url = "http://scienceportal-dev.linea.gov.br/api/graphql"

  def processes(self, parameters=""):
    query = """{
      processesList%s {
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
    }""" % parameters

    response = requests.post(self.url, json={ 'query': query }).json()

    edges = response['data']['processesList']['edges']

    # Removing unecessary parent node property inside of every process:
    processes = list(map(lambda x: x['node'], edges))

    return processes


  # Get all processes:
  def all(self):
    return self.processes()


  # Get process by its process id:
  def by_id(self, id):
    query = """{
      processByProcessId(processId: %s) {
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
    }""" % id

    response = requests.post(self.url, json={ 'query': query }).json()

    process = response['data']['processByProcessId']

    return process