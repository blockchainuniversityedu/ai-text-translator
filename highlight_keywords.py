def highlight_keywords(text, keywords):
    highlight_text = text
    for keyword in keywords:
        highlight_text = highlight_text.replace(keyword, f'**{keyword}**')
    return highlight_text