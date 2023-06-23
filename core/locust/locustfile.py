from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    
    def on_start(self):
        response = self.client.post('accounts/api/v1/jwt/create/' , data={
            "emai":"admin@admin.com" ,
            "password" : "a/@1234567"
        }).json()
        self.client.headers = {'Authorization' : f"Bearer {response.get('access' , None)}"}

        

    @task
    def ads_list(self):
        self.client.get("/charity/api/v1/ads")

    @task
    def category_list(self):
        self.client.get("/charity/api/v1/category")

    @task
    def donation_list(self):
        self.client.get("/charity/api/v1/donation")