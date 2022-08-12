from booking.booking import Booking

with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='AUD')
        bot.select_place_to_go('Brazil')
        bot.select_dates(check_in_date='2022-08-14', check_out_date='2022-08-15')
        bot.select_adults(23)
        bot.click_search()





