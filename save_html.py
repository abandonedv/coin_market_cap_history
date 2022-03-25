def save_html(my_html, url):
    cryp_name = url.split("/")
    with open(f"saved_html/{cryp_name[-3]}.html", "w+", encoding="utf-8") as f:
        f.write(my_html)
