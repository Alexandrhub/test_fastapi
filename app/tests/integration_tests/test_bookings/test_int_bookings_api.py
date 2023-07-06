import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "room_id, date_from, date_to, booked_rooms, status_code",
    [
        (4, "2030-05-01", "2030-05-15", 3, 200),
        (4, "2030-05-02", "2030-05-16", 4, 200),
        (4, "2030-05-03", "2030-05-17", 5, 200),
        (4, "2030-05-04", "2030-05-18", 6, 200),
        (4, "2030-05-05", "2030-05-19", 7, 200),
        (4, "2030-05-06", "2030-05-20", 8, 200),
        (4, "2030-05-07", "2030-05-21", 9, 200),
        (4, "2030-05-08", "2030-05-22", 10, 200),
        # (4, "2030-05-09", "2030-05-23", 10, 409),
        # (4, "2030-05-10", "2030-05-24", 10, 409),
    ],
)
async def test_add_and_get_booking(
    room_id, date_from, date_to, status_code, booked_rooms, authenticated_ac: AsyncClient
):
    response = await authenticated_ac.post(
        "/bookings", params={"room_id": room_id, "date_from": date_from, "date_to": date_to}
    )

    assert response.status_code == status_code

    response = await authenticated_ac.get("/bookings")

    assert len(response.json()) == booked_rooms


async def test_get_and_delete_bookings(authenticated_ac: AsyncClient):
    response = await authenticated_ac.get("/bookings")
    # Check that after we added  8 bookings we have 10 now
    assert len(response.json()) == 10
    # Check if delete works
    for booking in response.json():
        response = await authenticated_ac.delete(f"/bookings/{booking['id']}")
        assert response.status_code == 204
