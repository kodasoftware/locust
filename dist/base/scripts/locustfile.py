from locust import TaskSet, HttpUser, task, between

class Tasks(TaskSet):
  @task(1)
  def someAction(self):
    # Do some stuff

class SauceUser(HttpUser):
  wait_time = between(3, 15)
  tasks = [Tasks]