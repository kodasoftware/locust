from locust import TaskSet, task, between
from locust.contrib.fasthttp import FastHttpUser

class SearchTasks(TaskSet):
  @task(9)
  def search(self):
    print('Executing search')
    response = self.client.post('/graphs', json={
      "@context": {
        "images": "https://vocabularies.sauce.dneg.com/images/",
        "core": "https://vocabularies.sauce.dneg.com/core/",
        "api": "https://vocabularies.sauce-project.tech/api/",
        "filter": {
          "@id": "api:Filter"
        },
        "option": {
          "@id": "api:FilterOption",
          "@container": "@set"
        },
        "exact": "https://vocabularies.sauce-project.tech/api/FilterExact",
        "like": {
          "@id": "https://vocabularies.sauce-project.tech/api/FilterLike",
          "@container": "@set"
        },
        "clf": "https://vocabularies.sauce.dneg.com/classification/"
      },
      "@graph": [{
        "@type": "images:Texture",
        "core:title": {
          "option": ["rock"],
          "api:Sort": "ASC"
        },
        "clf:sample": {},
        "core:depicts": {}
      }]
    }, name='query graphs')
    pass

  # @task(3)
  # def get(self):
    # response = self.client.post('/graphs', json={
    #   "@context": {
    #     "core": "https://vocabularies.sauce.dneg.com/core/",
    #     "clf": "https://vocabularies.sauce.dneg.com/classification/",
    #     "downloadURL": { "@id": "https://vocabularies.sauce.dneg.com/core/downloadURL", "@type": "@id" },
    #     "segment": { "@id": "https://vocabularies.sauce.dneg.com/core/segment", "@type": "@id" },
    #     "File-Type": "https://vocabularies.sauce.dneg.com/images/File-Type/",
    #     "Huffman": "https://vocabularies.sauce.dneg.com/images/Huffman/",
    #     "JFIF": "https://vocabularies.sauce.dneg.com/images/JFIF/",
    #     "JPEG": "https://vocabularies.sauce.dneg.com/images/JPEG/"
    #   },
    #   "@id": "https://sauce.dneg.com/graphs/37e6ca0d-bfea-49cc-8436-473da451feed",
    #   "@graph": {
    #     "@id": "https://sauce.dneg.com/assets/rock_05-64912e6c-6f31-4976-95e6-2558e0a01658",
    #     "@type": "core:Asset",
    #     "core:title": {},
    #     "clf:sample": {},
    #     "core:depicts": { "core:label": {} },
    #     "downloadURL": {},
    #     "segment": {},
    #     "File-Type:Detected-File-Type-Long-Name": {},
    #     "File-Type:Detected-File-Type-Name": {},
    #     "File-Type:Detected-MIME-Type": {},
    #     "File-Type:Expected-File-Name-Extension": {},
    #     "Huffman:Number-of-Tables": {},
    #     "JFIF:Resolution-Units": {},
    #     "JFIF:Thumbnail-Height-Pixels": {},
    #     "JFIF:Thumbnail-Width-Pixels": {},
    #     "JFIF:Version": {},
    #     "JFIF:X-Resolution": {},
    #     "JFIF:Y-Resolution": {},
    #     "JPEG:Component-1": {},
    #     "JPEG:Component-2": {},
    #     "JPEG:Component-3": {},
    #     "JPEG:Compression-Type": {},
    #     "JPEG:Data-Precision": {},
    #     "JPEG:Image-Height": {},
    #     "JPEG:Image-Width": {},
    #     "JPEG:Number-of-Components": {}
    #   }
    # }, name='query graph')
  #   pass

  @task(1)
  def stop(self):
    self.interrupt()

class Search(TaskSet):
  tasks = [SearchTasks]

class User(FastHttpUser):
  wait_time = between(1, 7)
  task_set = Search
