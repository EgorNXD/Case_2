"""
Salary: Polevik Alexey = 30
        Elizarev Yaroslav = 45
        Nechaev Egor = 45
"""
import russian_localizator as ru

dividend_bid = 0.0
property_bid = 0.0
deal_bid = 0.0
wage_bid = 0.0
wage_addition = 0
property_seller = True
dividend_income = 0
property_income = 0
deal_income = 0
wage_income = 0
old_bonds = 0
lotteries = 0
bank_deposit = 0

name = str(input(ru.name))
print(ru.glad, name + "!")
print(ru.intention)
print(ru.require)
print(ru.start)

ans = str(input(ru.rezident))
if ans.lower() == ru.yes:
    res = True
else:
    res = False
ans = str(input(ru.big_income))
if ans.lower() == ru.yes:
    rich = True
else:
    rich = False

# nonresident branch
if not res:
    dividend_bid = 0.15
    property_bid = 0.3
    deal_bid = 0.3
    ans = str(input(ru.special_labor_category))
    if ans.lower() == ru.yes and rich:
        wage_bid = 0.15
        wage_addition = 650000
    elif ans.lower() == ru.yes and not rich:
        wage_bid = 0.13
    else:
        wage_bid = 0.3

# resident branch
else:
    dividend_bid = 0.13
    if rich:
        property_bid = 0.15
        deal_bid = 0.15
        wage_bid = 0.15
    else:
        wage_bid = 0.13
        deal_bid = 0.13
        ans = str(input(ru.did_u_sold_pprty))
        if ans.lower() == ru.yes:
            ans = str(input(ru.property_ownrshp_condtns))
            if ans.lower() == ru.yes:
                ans = str(input(ru.own_three_yrs_or_not))
                if ans.lower() == ru.no:
                    property_bid = 0.13
            else:
                ans = str(input(ru.only_real_estate))
                if ans.lower() == ru.no:
                    ans = str(input(ru.own_five_yrs_or_not))
                    if ans.lower() == ru.no:
                        property_bid = 0.13
            ans = str(input(ru.how_many_chldrn))
            if ans.lower() == ru.yes:
                property_bid = 0.0
        else:
            property_seller = False

print(ru.lets_get_down_counting)

bank_deposit = int(input(ru.bank_deposit_inc))
dividend_income = int(input(ru.dividents))
if property_seller:
    property_income = int(input(ru.estate_sale_inc))
deal_income = int(input(ru.citizens_deals_inc))
wage_income = int(input(ru.salary))
old_bonds = int(input(ru.old_bonds))
lotteries = int(input(ru.lotteries))
if lotteries <= 4000:
    lotteries = 0

print(ru.total)
print(round(
    dividend_income*dividend_bid + property_income*property_bid + deal_income*deal_bid + wage_income*wage_bid
    + wage_addition + old_bonds*0.09 + lotteries*0.35 + bank_deposit*wage_bid))
