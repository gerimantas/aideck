from locust import HttpUser, task, between

class OrchestratorLoadTest(HttpUser):
    wait_time = between(1, 5)

    @task
    def trigger_agents(self):
        self.client.post("/api/agents/run", json={"project_id": "test", "input": "load test"})
