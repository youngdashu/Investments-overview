class_count=0
class main_char:
    price: int=0
    area=0
    try:
        ppm=price/area
    except:
        ppm=0
class info:
    date_start=""
    date_end=""
    desc=""
    address1=""
    address2=""
    estimated_value=0
    estimation_date=""
class contribution:
    contr=0
    marg_b=0
    marg_n=0
    tax=0
    other=0
    redec=0
    total=contr+marg_b+marg_n+tax+other+redec
    purchase=0
class credit:
    bank_c=0
    bank_perc=0
    rate=0
    time=0
    month_rate=0
    capital_part=0
    interest_part=0
    monthly_insurance=0
    costs_total=0
class rent:
    income_min=0
    income_max=0
    income_real=0
    tax_rent=0
    tax_estate=0
    power=0
    gas=0
    water=0
    internet=0
    other=0
    cost_total=tax_estate+tax_rent+power+gas+water+other
    gain=income_real-cost_total
class eval:
    return_time=0
    return_total=0
    return_rate=0
    rate_total=0
    notes=""
class stats:
    num=class_count+1
    stat1=main_char()
    stat2=info()
    stat3=contribution()
    try:
        stat3.purchase=stat3.total/stat1.price
    except:
        pass
    stat4=credit()
    stat5=rent()
    stat6=eval()
