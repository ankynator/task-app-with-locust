from locust import HttpUser, task, between
from lorem_text import lorem

class HelloWorldUser(HttpUser):
    wait_time = between(1,3)

    @task(10)
    def view_home(self):
        self.client.get("/")

    @task
    def create_task(self):
        random_task = lorem.words(5)
        self.client.post('/create-task', {'content': random_task, 'done': False})
