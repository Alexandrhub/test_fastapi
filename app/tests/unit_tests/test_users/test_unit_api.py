from httpx import AsyncClient


async def test_register_user(ac: AsyncClient):
    response = await ac.post(
        "/auth/register",
        json={"email": "kot@pes.com", "password": "kotopes"},
    )
    assert response.status_code == 201
