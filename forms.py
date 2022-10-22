from django import forms


class BmrForm(forms.Form):
    genders = (
        ("M", "Мужчина"),
        ("F", "Женщина"),
    )
    gender = forms.ChoiceField(choices=genders, label="пол")
    height = forms.IntegerField(min_value=1, label="рост в см")
    weight = forms.IntegerField(min_value=1, label="вес в кг")
    age = forms.IntegerField(min_value=1, label="возраст в годах")
    activities = (
        (1.2, "Сидячий образ жизни без нагрузок"),
        (1.375, "Тренировки  1-3 раза в неделю"),
        (1.55, "Занятия 3-5 дней в неделю"),
        (1.725, "Интенсивные тренировки 6-7 раз в неделю"),
        (1.9, "Спортсмены, выполняющие упражнения чаще, чем раз в день")
    )
    activity = forms.ChoiceField(choices=activities, label="нагрзка")