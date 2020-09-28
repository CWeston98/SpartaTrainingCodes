import configparser

_config = configparser.ConfigParser()
_config.read('./config.ini')


def find_url(page="homepage_url"):
    try:
        page_address = _config['DEFAULT'][page]
        return page_address + "?offset=0&limit=1500"
    except KeyError:
        print(f'The page {page} does not exist')
