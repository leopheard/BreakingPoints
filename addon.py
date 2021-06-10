from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.simplecast.com/_iafZVRs"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://image.simplecastcdn.com/images/a2694d6e-ef6f-4f27-871c-e4396781ef11/4dee98e9-5154-4f50-8cd8-f170f8da8032/3000x3000/podcast-artwork.jpg?aid=rss_feed"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://image.simplecastcdn.com/images/a2694d6e-ef6f-4f27-871c-e4396781ef11/4dee98e9-5154-4f50-8cd8-f170f8da8032/3000x3000/podcast-artwork.jpg?aid=rss_feed"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup1)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

if __name__ == '__main__':
    plugin.run()
