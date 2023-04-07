
class User:

    def __init__(self, name, surname, age, address, wallet):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.wallet = wallet

    def user_info(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Возраст: {self.age}, Адрес: {self.address}, Денег на счету: {self.wallet} "


class Website:
    user = User
    def __init__(self, order_num, order_sum, user):
        self.order_num = order_num
        self.order_sum = order_sum
        self.user = user

    def subtraction(self,  order_sum):
        self.user.wallet -= order_sum
        return self.user.wallet

    def ordering(self, order_num: int, order_sum: int):
        print(f"Ваш заказ успешно оформлен, номер заказа {self.order_num}\n"
              f"Списано с карты {self.order_sum}! Осталось-> {self.user.wallet}")

        return order_num, order_sum


class Delivery:
    user1 = User

    def __init__(self, time, user1):
        self.time = time
        self.user1 = user1

    def start(self):
        return f"Заказ скоро доставят через {self.time} минут по адресу {self.user1.address}"

    def finish(self):
        return f"Заказ успешно доставлен вам {self.user1.name} {self.user1.surname} "


    def rating(self):
        while False <= 0:
            try:
                value = float(input("Введите число от 0 до 10 на сколько понравилась доставка->" ))
                if value > 0:
                    input("Раскажите почему оно вам понравилось ")
                    break
                if value < 0:
                    print("Не должно быть меньше 0")
                    continue
                elif value == 0:
                    input("Раскажите почему оно вам не понравилось ")
                    break
            except ValueError:
                print("Введенно не число")

class Assistant:
    user2 = User
    def __init__(self, user2):
        self.user2 = user2

    def choice(self):
        x = input('У вас возникали проблемы с нашим сервисом ? \nДА/НЕТ ')
        while (x.lower() != "да" or x.lower() != "нет"):
            if x.lower() == "да":
                print(f" {self.descrip_problem()}")
                break
            elif x.lower() == "нет":
                print("До скорой встречи ")
                break
            else:
                x = input('У вас возникали проблемы с нашим сервисом ? \nДА/НЕТ ')


    def descrip_problem(self):
        problem = input("Опишите свою проблему ")
        print(f"Мы свяжемся с вами {self.user2.name} когда устраним проблему ")



new_user = User("Максим", "Пан", 15, "Удмурская", 5800)
print(new_user.user_info())
site = Website(57452734723, 5000, new_user)
site.subtraction(5000)
site.ordering(52185924, 5000)
print(new_user.user_info())
deliveryman = Delivery(24, new_user)
print(deliveryman.start())
deliveryman.rating()
print(deliveryman.finish())
help = Assistant(new_user)
print(help.choice())
