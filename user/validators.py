def phone_validator(value):
    if not len(value) == 13:
        raise ValueError("Telefon raqamida xatolik bor to'g'ri tel kriting misol +998882640011")
    else:
        return True
