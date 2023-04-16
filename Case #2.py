"""
Salary: Polevik Alexey =
        Elizarev Yaroslav =
        Nechaev Egor =
"""

dividend_income = 0.0
property_income = 0.0
deal_income = 0.0
wage_income = 0.0
wage_income_add = 0
property_haver = True
dividend = 0
property = 0
deal = 0
wage = 0
u1 = 0
u2 = 0
u3 = 0


name = str(input('Здравствуйте! Как Вас зовут? '))
print("Очень приятно,", name+"!")
print("Сегодня мы посчитаем ваш размер налога НДФЛ.")
print("Пожалуйста, отвечайте на следующие вопросы честно и точно.")
print("Начнем с общих вопросов.")


ans = str(input('Вы резидент РФ? (более 183 дней в РФ - резидент) '))
if ans.lower() == "да":
    res = True
else: res = False
ans = str(input('Полученная за год зарплата больше 5 млн? '))
if ans.lower() == "да":
    rich = True
else: rich = False

# nonresident branch
if res == False:
    dividend_income = 0.15
    property_income = 0.3
    deal_income = 0.3
    ans = str(input('Относитесь ли вы к одной из следующих категорий работников: высококвалифицированный специалист,'
                    ' беженец, участник Государственной программы по оказанию содействия добровольному переселению в Российскую Федерацию соотечественников,'
                    ' проживающих за рубежом, а также членами их семей, член экипажа судна, плавающего под Российским флагом? '))
    if ans.lower() == "да" and rich == True:
        wage_income = 0.15
        wage_income_add = 650000
    elif ans.lower() == "да" and rich == False:
        wage_income = 0.13
    else: wage_income = 0.3

# resident branch
else:
    dividend_income = 0.13
    if rich == True:
        property_income = 0.15
        deal_income = 0.15
        wage_income = 0.15
    else:
        wage_income = 0.13
        deal_income = 0.13
        ans = str(input('Вы продавали имущество? '))
        if ans.lower() == "да":
            ans = str(input('Имущество было получено по наследству, '
                            'в результате приватизации или в результате передачи по договору о пожизненном содержании с иждивением? '))
            if ans.lower() == "да":
                ans = str(input('Вы владели жильем более 3 лет? '))
                if ans.lower() == "нет":
                    property_income = 0.13
            else:
                ans = str(input('Являлось ли Ваше жилье единственным располагаемым Вами или Вашим супругом на момент продажи? '))
                if ans.lower() == "нет":
                    ans = str(input('Вы владели жильем более 5 лет? '))
                    if ans.lower() == "нет":
                        property_income = 0.13
            ans = str(input('У Вас двое или более детей? '))
            if ans.lower() == "да":
                property_income = 0.0
        else: property_haver = False


print("Хорошо, теперь перейдем к вычислению.")
u1 = int(input('Введите ваш годовой доход по облигациям, выпущенных до 1 января 2007 года: '))
u2 = int(input('Введите ваш годовой доход c выигрышей и призов, получаемых в проводимых конкурсах,'
               ' играх и других мероприятиях в целях рекламы товаров, работ и услуг' ))
if u2<=4000:
    u2=0
u3 = int(input('Введите ваши процентные доходы по вкладам в банках: '))
if u3<=4000:
    u3=0
dividend = int(input('Введите ваш годовой доход по дивидентам: '))
if property_haver == True:
    property = int(input('Введите ваш годовой доход c продажи имущества: '))
deal = int(input('Введите ваш годовой доход c гражданско-правовых договоров (аренда имущества и тд): '))
wage = int(input('Введите ваш годовой доход c зарплаты: '))


print("Отлично, вот сколько вы должны: ")
print(round(dividend*dividend_income + property*property_income + deal*deal_income + wage*wage_income + wage_income_add))


#debug
""" 
print(dividend_income,
property_income,
deal_income,
wage_income,
wage_income_add,
property_haver)
"""
