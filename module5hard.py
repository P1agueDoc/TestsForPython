import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = nickname
            else:
                print("Can't log in")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        user_new = User(nickname, password, age)
        self.current_user = user_new
        self.users.append(user_new)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(vid.title == video.title for vid in self.videos):
                self.videos.append(video)

    def get_videos(self, search):
        search = search.lower()
        result = []
        for video in self.videos:
            if search in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            video = None
            for i in self.videos:
                if i.title == title:
                    video = i

            if video is None:
                print("Видео не найдено")
            else:
                if self.current_user.age < 18 and video.adult_mode:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for second in range(video.duration + 1):
                        time.sleep(1)
                        print(f"Время: {second} сек")
                    Video.time_now = 0
                    print("Конец видео")




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')