"""
1.  Воспроизведение мультимедиа.
    Создайте два класса:

    AudioFileMixin — требует наличие поля audio_tracks (список треков).
    Метод play_audio() выводит:
    Воспроизведение аудио для <НазваниеКласса>:
    <название трека>
    <название трека>

    VideoFileMixin — требует наличие поля video_files (список видео).
    Метод play_video() выводит:
    Воспроизведение видео для <НазваниеКласса>:
    <название видео>
    <название видео>
    Если нужное поле отсутствует — выбрасывайте AttributeError.
"""


class AudioFileMixin:

    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError(f"У {self.__class__.__name__} отсутствует атрибут 'audio_tracks'")

        print(f"Воспроизведение аудио для {self.__class__.__name__}:")
        for track in self.audio_tracks:
            print(track)


class VideoFileMixin:

    def play_video(self):
        if not hasattr(self, "video_files"):
            raise AttributeError(f"У {self.__class__.__name__} отсутствует атрибут 'video_files'")

        print(f"Воспроизведение видео для {self.__class__.__name__}:")
        for track in self.video_files:
            print(track)


"""
2.  Устройства.
    Создайте два класса:
    MediaPlayer — поддерживает только аудио. Принимает список треков.
    Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
    Проверьте работу классов, вызвав методы воспроизведения.
Данные:
tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]
Пример вывода:
Воспроизведение аудио для MediaPlayer:
track1.mp3
track2.mp3
Воспроизведение аудио для Laptop:
track1.mp3
track2.mp3
Воспроизведение видео для Laptop:
movie.mp4
trailer.mov
"""


class MediaPlayer(AudioFileMixin):

    def __init__(self, audio_tracks=None):
        if audio_tracks:
            self.audio_tracks = audio_tracks


class Laptop(AudioFileMixin, VideoFileMixin):

    def __init__(self, audio_tracks=None, video_files=None):
        if audio_tracks:
            self.audio_tracks = audio_tracks
        if video_files:
            self.video_files = video_files


tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

audio = MediaPlayer(tracks)
audio.play_audio()
media = Laptop(tracks, movies)
media.play_audio()
media.play_video()

# проверяем на ошибки
media = Laptop('', movies)
media.play_audio()
#
media = Laptop(tracks)
media.play_video()
#
media = Laptop()
media.play_audio()
media.play_video()
#
audio = MediaPlayer()
audio.play_audio()