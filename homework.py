M_IN_KM = 1000


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):

        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration} ч.; '
                f'Дистанция: {self.distance} км; '
                f'Ср. скорость: {self.speed} км/ч; '
                f'Потрачено ккал: {self.calories}. ')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.00

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance: float = self.action * self.LEN_STEP / M_IN_KM
        return f'{distance} км.'

    def get_mean_speed(self, distance) -> float:
        """Получить среднюю скорость движения."""
        avarage = distance/self.duration
        return f'Средняя скорость = {avarage} км/ч.'

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return 'Тренировка выполнена!'


class Running(Training):
    """Тренировка: бег."""

    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000

    def __init__(self, action, duration, weight):
        super().__init__(action, duration, weight)

    action = LEN_STEP * M_IN_KM

    def get_distance(self) -> float:
        super().get_distance()

    def get_mean_speed(self, distance) -> float:
        super().get_mean_speed(distance)

    def get_spent_calories(self) -> float:
        super().get_spent_calories()

    def show_training_info(self) -> InfoMessage:
        super().show_training_info()


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000

    def __init__(self, action, duration, weight):
        super().__init__(action, duration, weight)

    action = LEN_STEP * M_IN_KM

    def get_distance(self) -> float:
        super().get_distance()

    def get_mean_speed(self, distance) -> float:
        super().get_mean_speed(distance)

    def get_spent_calories(self) -> float:
        super().get_spent_calories()

    def show_training_info(self) -> InfoMessage:
        super().show_training_info()


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    M_IN_KM: int = 1000

    def __init__(self, action, duration, weight):
        super().__init__(action, duration, weight)

    action = LEN_STEP * M_IN_KM

    def get_distance(self) -> float:
        super().get_distance()

    def get_mean_speed(self, distance) -> float:
        super().get_mean_speed(distance)

    def get_spent_calories(self) -> float:
        super().get_spent_calories()

    def show_training_info(self) -> InfoMessage:
        super().show_training_info()


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
