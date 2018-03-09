"""Написать функцию расчета аннуитетного платежа. Написать функцию расчета ежимесячного платежа. Рассчитать размер 
платежа при ипотеке 15 млн на 25 лет под 14% годовых. Мат. часть: 
http://biznes-kredit.info/malyj/raschet-annuitetnyh-platezhej-formula-excel.html """


period = 25  # срок кредита
creditPersentPerYear = 14  # процентная ставка в год
creditSum = 15000000  # сумма кредита в рублях


def get_annuetent_K():
    """Расчет ануетентный коэффициента"""
    creditPeriodInMonths = period * 12
    creditPersentPerMonths = creditPersentPerYear / 12 / 100
    totalPercentInPeriod = (1 + creditPersentPerMonths) ** creditPeriodInMonths
    return creditPersentPerMonths * totalPercentInPeriod / (totalPercentInPeriod - 1)


def get_annuetent_sum ():
    """Расчет ежемесячного аннуитентного платежа"""
    return get_annuetent_K() * creditSum


print("Ежемесячный платеж: {:.2f} руб".format(get_annuetent_sum()))