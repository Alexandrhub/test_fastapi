# from datetime import datetime
#
# from app.bookings.dao import BookingDAO
#
#
# async def test_add_and_get_booking():
#     new_booking = await BookingDAO.add_rows(
#         user_id=2,
#         room_id=2,
#         date_from=datetime.strptime("2023-07-10", "%Y-%m-%d"),
#         date_to=datetime.strptime("2023-07-24", "%Y-%m-%d"),
#     )
#     assert new_booking.user_id == 2
#     assert new_booking.room_id == 2
#     assert await BookingDAO.select_one_or_none_filter_by(id=new_booking.id)
#     await BookingDAO.delete_booking_for_user(new_booking.user_id, user_id=2)
#     assert await BookingDAO.select_one_or_none_filter_by(id=new_booking.id) is None
