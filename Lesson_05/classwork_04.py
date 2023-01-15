'''Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона, к которому относится этот месяц.
Например, передаем 2, на выходе получаем "Winter".'''
my_map = {
    "Winter":[12,1,2],
    "Spring":[3,4,5],
    "Sammer":[6,7,8],
    "fall":[9,10,11],
}
def  month_to_season(month_number):
    for season,month in my_map.items():
     if month_number in month:
      return season
print(month_to_season(2))