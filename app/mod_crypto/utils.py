def format_crypto_history(crypto_history):
    """
    takes the crypto_history as an argument and formats it using some of the basic HTML tags allowed by Telegram,
    like <br>, <b>, <i>, and so on
    :param crypto_history: List of crypto currency history
    :return: String formatted for Telegram
    """
    rows = []
    for crypto_price in crypto_history:
        date = crypto_price['date'].strftime('%d.%m.%Y %H:%M')  # Formats the date into a string: '24.02.2018 15:09'
        price = crypto_price['price']
        # <b> (bold) tag creates bolded text
        row = '{}: $<b>{}</b>'.format(date, price)  # 24.02.2018 15:09: $<b>10123.4</b>
        rows.append(row)

    # Use a <br> (break) tag to create a new line
    return '<br>'.join(rows)  # Join the rows delimited by <br> tag: row1<br>row2<br>row3
