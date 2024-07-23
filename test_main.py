import pytest
from httpx import AsyncClient
from main import app
import time

base_url = "http://localhost:8080"

cities = [
    3439525,
    3439781,
]


@pytest.mark.asyncio
async def test_run_task():

    async with AsyncClient(app=app, base_url=base_url) as ac:
        time.sleep(10)
        response = await ac.post("/tasks", json={"id": "id1"})
        assert response.status_code == 201
        assert response.json() == {"id": "id1"}

        response = await ac.post("/tasks", json={"id": "id1"})
        assert response.status_code == 200
        assert response.json() == {"id": "id1"}


@pytest.mark.asyncio
async def test_get_completion():

    async with AsyncClient(app=app, base_url=base_url) as ac:
        time.sleep(10)
        await ac.post("/tasks", json={"id": "id2"})
        time.sleep(10)
        response = await ac.get("/completion/id2")
        assert response.status_code == 200

        assert "completed_percentage" in response.json()
        assert response.json()["completed_percentage"] == 100

        response = await ac.get("/completion/wrong-id")
        assert response.status_code == 404
        assert response.json() == {"completed_percentage": None}


@pytest.mark.asyncio
async def test_get_results():

    async with AsyncClient(app=app, base_url=base_url) as ac:
        time.sleep(10)
        await ac.post("/tasks", json={"id": "id3"})
        time.sleep(10)
        response = await ac.get("/results/id3")
        assert response.status_code == 200

        assert "results" in response.json()
        results = response.json()["results"]
        assert len(results) == 2
        for result in results:
            assert result["city_id"] in cities
            assert "humidity" in result
            assert "temp" in result

        response = await ac.get("/results/wrong-id")
        assert response.status_code == 404
        assert response.json() == {"results": None}


if __name__ == "__main__":
    pytest.main()
