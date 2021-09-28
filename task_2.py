# 2.Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
seconds = int(input('Введите время в секундах = '))
seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
#print(f"Время в формате чч:мм:сс= {hour}:{minutes}:{seconds}")
print("%02d:%02d:%02d" % (hour, minutes, seconds))
