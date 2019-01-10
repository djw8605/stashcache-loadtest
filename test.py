from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(2)
    def tenm(self):
        self.client.get("/user/dweitzel/public/loadtest/loadtest.10M")

    @task(5)
    def onem(self):
        self.client.get("/user/dweitzel/public/loadtest/loadtest.1M")

    @task(1)
    def hunderedm(self):
        self.client.get("/user/dweitzel/public/loadtest/loadtest.100M")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 9000
