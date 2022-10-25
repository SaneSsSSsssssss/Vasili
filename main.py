def time():
   hour = 20
   if hour  >= 6 and hour <= 11:
      print('Доброе Утро')
   elif hour >= 12 and hour <= 17:
      print('Добрый День')
   elif hour >= 18 and hour <= 22:
      print('Добрый Вечер')
   elif (hour >= 23 and hour <= 24) or (hour >= 0 and hour <= 5):
      print('Доброй Ночи')

def hello(names):
   print(names)

def hell():
   print('Я Василий, ваш персональный помощник.')
   print('Я ещё маленький, но постоянно расту и умнею -')
   print('ведь мой код каждый день дописывают!')

hello('Рамиз')
time()
hell()
