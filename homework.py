MIN_IN_H = 60
M_IN_KM = 1000
CM_IN_M = 100
KMH_IN_MSEC = 0.278


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type,
                 duration,
                 distance,
                 speed,
                 calories) -> None:
        self.training_type = training_type
        self.duration = duration
        self.duration = float('{:.3f}'.format(self.duration))
        self.distance = distance
        self.distance = float('{:.3f}'.format(self.distance))
        self.speed = speed
        self.speed = float('{:.3f}'.format(self.speed))
        self.calories = calories
        self.calories = float('{:.3f}'.format(self.calories))

    def get_message(self):
        print(f'Тип тренировки: {self.training_type}; '
              f'Длительность: {self.duration} ч.; '
              f'Дистанция: {self.distance} км; '
              f'Ср. скорость: {self.speed} км/ч; '
              f'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.training_type = self.__class__.__name__
        self.calories: float

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        self.distance = self.action * self.LEN_STEP / M_IN_KM
        return self.distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        self.mean_speed = self.distance / self.duration
        return self.mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return self.calories

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        self.get_distance()
        self.get_mean_speed()
        self.get_spent_calories()
        self.info = InfoMessage(self.training_type,
                                self.duration,
                                self.distance,
                                self.mean_speed,
                                self.get_spent_calories(),
                                )
        return self.info


class Running(Training):
    """Тренировка: бег."""
    LEN_STEP = 0.65
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        min_duration = self.duration / MIN_IN_H
        self.calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER
                          * self.mean_speed
                          + self.CALORIES_MEAN_SPEED_SHIFT)
                         * self.weight / M_IN_KM
                         * min_duration)
        return self.calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    LEN_STEP = 0.65
    CALORIES_MEAN_SPEED_MULTIPLIER = 0.035
    CALORIES_MEAN_SPEED_SHIFT = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        self.height = height
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        min_duration = self.duration / MIN_IN_H
        m_height = self.height / CM_IN_M
        mean_speed_in_m_sec = self.mean_speed * KMH_IN_MSEC
        self.calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER
                          * self.weight
                          + (mean_speed_in_m_sec**2
                             / m_height)
                          * self.CALORIES_MEAN_SPEED_SHIFT
                          * self.weight)
                         * min_duration)
        return self.calories


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    CALORIES_MEAN_SPEED_MULTIPLIER = 2
    CALORIES_MEAN_SPEED_SHIFT = 1.1

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        self.mean_speed = (self.length_pool
                           * self.count_pool
                           / M_IN_KM
                           / self.duration)
        return self.mean_speed

    def get_spent_calories(self) -> float:
        self.calories = ((self.mean_speed
                          + self.CALORIES_MEAN_SPEED_SHIFT)
                         * self.CALORIES_MEAN_SPEED_MULTIPLIER
                         * self.weight
                         * self.duration)
        return self.calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_types = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
    training: Training = training_types[workout_type](*data)
    return training


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
