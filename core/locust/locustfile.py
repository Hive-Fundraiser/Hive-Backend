from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    
    @task
    def advertisement_list(self):
        self.client.get("/charity/api/v1/ads")

    @task
    def advertisement_list(self):
        self.client.get("/charity/api/v1/category")

    @task
    def advertisement_list(self):
        self.client.get("/charity/api/v1/donation")