"""
Salary: Polevik Alexey =
        Elizarev Yaroslav =
        Nechaev Egor =
"""

dividend_bid = 0.0
property_bid = 0.0
deal_bid = 0.0
wage_bid = 0.0
wage_addition = 0
property_haver = True
dividend_income = 0
property_income = 0
deal_income = 0
wage_income = 0
q1 = 0
q2 = 0
q3 = 0


name = str(input('Здравствуйте! Как Вас зовут? '))
print("Очень приятно,", name+"!")
print("Сегодня мы посчитаем Ваш размер налога НДФЛ.")
print("Пожалуйста, отвечайте на следующие вопросы честно и точно.")
print("Начнем с общих вопросов.")


ans = str(input('Вы резидент РФ? (более 183 дней в РФ - резидент) '))
if ans.lower() == "да":
    res = True
else: res = False
ans = str(input('Ваша заработная плата, доходы от дивидендов,'
                ' доходы от операций с ценными бумагами суммарно составляют более 5 млн рублей? '))
if ans.lower() == "да":
    rich = True
else: rich = False

# nonresident branch
if res == False:
    dividend_bid = 0.15
    property_bid = 0.3
    deal_bid = 0.3
    ans = str(input('Относитесь ли вы к одной из следующих категорий работников: высококвалифицированный специалист,'
                    ' беженец, участник Государственной программы по оказанию содействия добровольному переселению в Российскую Федерацию соотечественников,'
                    ' проживающих за рубежом, а также членами их семей, член экипажа судна, плавающего под Российским флагом? '))
    if ans.lower() == "да" and rich == True:
        wage_bid = 0.15
        wage_addition = 650000
    elif ans.lower() == "да" and rich == False:
        wage_bid = 0.13
    else: wage_bid = 0.3

# resident branch
else:
    dividend_bid = 0.13
    if rich == True:
        property_bid = 0.15
        deal_bid = 0.15
        wage_bid = 0.15
    else:
        wage_bid = 0.13
        deal_bid = 0.13
        ans = str(input('Вы продавали имущество? '))
        if ans.lower() == "да":
            ans = str(input('Имущество было получено по наследству, '
                            'в результате приватизации или в результате передачи по договору о пожизненном содержании с иждивением? '))
            if ans.lower() == "да":
                ans = str(input('Вы владели жильем более 3 лет? '))
                if ans.lower() == "нет":
                    property_bid = 0.13
            else:
                ans = str(input('Являлось ли Ваше жилье единственным располагаемым Вами или Вашим супругом на момент продажи? '))
                if ans.lower() == "нет":
                    ans = str(input('Вы владели жильем более 5 лет? '))
                    if ans.lower() == "нет":
                        property_bid = 0.13
            ans = str(input('У Вас двое или более детей? '))
            if ans.lower() == "да":
                property_bid = 0.0
        else: property_haver = False


print("Хорошо, теперь перейдем к вычислению.")
q1 = int(input('Введите Ваш годовой доход по облигациям, выпущенных до 1 января 2007 года: '))
q2 = int(input('Введите Ваш годовой доход c выигрышей и призов, получаемых в проводимых конкурсах,'
               ' играх и других мероприятиях в целях рекламы товаров, работ и услуг' ))
if q2 <= 4000:
    q2 = 0
q3 = int(input('Введите Ваши процентные доходы по вкладам в банках: '))
dividend_income = int(input('Введите Ваш годовой доход по дивидентам: '))
if property_haver == True:
    property_income = int(input('Введите Ваш годовой доход c продажи имущества: '))
deal_income = int(input('Введите Ваш годовой доход c гражданско-правовых договоров (аренда имущества и тд): '))
wage_income = int(input('Введите Ваш годовой доход c зарплаты: '))


print("Отлично, вот сколько Вы должны: ")
print(round(dividend_income*dividend_bid + property_income*property_bid + deal_income*deal_bid + wage_income*wage_bid + wage_addition + q1*0.09 + q2*0.35 + q3*wage_bid))

