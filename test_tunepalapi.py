from unittest import TestCase
from tunepalapi import Song
from tunepalapi import TunePalAPI

class Test(TestCase):
    def test_init(self):
        song = Song('Hello', 'Adele', '2015')
        self.assertEqual(song.title, 'Hello')
        self.assertEqual(song.artist, 'Adele')
        self.assertEqual(song.release_year, '2015')


class TestTunePalAPI(TestCase):

    def test_init(self):
        api = TunePalAPI(page_size=10)
        self.assertEqual(api.page_size, 10)
        self.assertGreater(len(api.songs), 0)

    def test__build_song_window(self):
        api = TunePalAPI(page_size=10)
        songs = [
            Song('Song 1', 'Artist 1', '1990'),
            Song('Song 2', 'Artist 2', '2000'),
            Song('Song 3', 'Artist 3', '2010'),
            Song('Song 4', 'Artist 4', '2020'),
            Song('Song 5', 'Artist 5', '2030'),
            Song('Song 6', 'Artist 6', '2040'),
            Song('Song 7', 'Artist 7', '2050'),
            Song('Song 8', 'Artist 8', '2060'),
            Song('Song 9', 'Artist 9', '2070'),
            Song('Song 10', 'Artist 10', '2080'),
            Song('Song 11', 'Artist 11', '2090'),
            Song('Song 12', 'Artist 12', '2100')
        ]
        api.current_page_index = 0
        api.page_size = 5
        song_window = api._build_song_window(songs)
        self.assertEqual(len(song_window), 5)
        self.assertEqual(song_window[0].title, 'Song 1')
        self.assertEqual(song_window[-1].title, 'Song 5')

        api.current_page_index = 1
        song_window = api._build_song_window(songs)
        self.assertEqual(len(song_window), 5)
        self.assertEqual(song_window[0].title, 'Song 6')
        self.assertEqual(song_window[-1].title, 'Song 10')

        api.current_page_index = 2
        song_window = api._build_song_window(songs)
        self.assertEqual(len(song_window), 2)
        self.assertEqual(song_window[0].title, 'Song 11')
        self.assertEqual(song_window[-1].title, 'Song 12')

    def test_add_song(self):
        api = TunePalAPI()
        api.add_song("title1", "artist1", "2022")
        self.assertEqual(len(api.songs), 1)
        api.add_song("title2", "artist2", "2021")
        self.assertEqual(len(api.songs), 2)
        api.add_song("title1", "artist1", "2022")  # adding duplicate song
        self.assertEqual(len(api.songs), 2)  # should still be 2

    def test_get_songs(self):
        self.fail()

    def test_next_page(self):
        self.fail()

    def test_previous_page(self):
        self.fail()

    def test_set_page_size(self):
        self.fail()

    def test_search(self):
        self.fail()

    def test_get_songs_since(self):
        self.fail()
