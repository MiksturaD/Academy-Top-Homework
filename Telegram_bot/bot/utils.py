class Habit:
    def __init__(self, name: str, description: str = None, metric: str = None, target_date: str = None) -> None:
        self.name = name
        self.description = description
        self.metric = metric
        self.target_date = target_date

    def __repr__(self) -> str:
        return (f'Название: {self.name}\nОписание: {self.description}\nЕдиница измерения: {self.metric}'
                f'\nЦелевая дата: {self.target_date}')
