import json
class Main_Char:
    def __init__(self,price,area,ppm):
        self.price=price
        self.area=area
        self.ppm=ppm
class Info:
    def __init__(self,date_start,date_end,desc,address1,address2,estimated_value,estimation_date):
        self.date_start=date_start
        self.date_end=date_end
        self.desc=desc
        self.address1=address1
        self.address2=address2
        self.estimated_value=estimated_value
        self.estimation_date=estimation_date
class Contribution:
    def __init__(self,contr,marg_b,marg_n,tax,other,redec,total,purchase):
        self.contr=contr
        self.marg_b=marg_b
        self.marg_n=marg_n
        self.tax=tax
        self.other=other
        self.redec=redec
        self.total=total
        self.purchase=purchase
class Credit:
    def __init__(self,bank_c,bank_perc,rate,time,month_rate,capital_part,interest_part,monthly_insurance,costs_total):
        self.bank_c=bank_c
        self.bank_perc=bank_perc
        self.rate=rate
        self.time=time
        self.month_rate=month_rate
        self.capital_part=capital_part
        self.interest_part=interest_part
        self.monthly_insurance=monthly_insurance
        self.costs_total=costs_total
class Rent:
    def __init__(self,income_min,income_max,income_real,tax_rent,tax_estate,power,gas,water,internet,other,cost_total,gain):
        self.income_min=income_min
        self.income_max=income_max
        self.income_real=income_real
        self.tax_rent=tax_rent
        self.tax_estate=tax_estate
        self.power=power
        self.gas=gas
        self.water=water
        self.internet=internet
        self.other=other
        self.cost_total=cost_total
        self.gain=gain
class Eval:
    def __init__(self,return_time,return_total,return_rate,rate_total,notes):
        self.return_time=return_time
        self.return_total=return_total
        self.return_rate=return_rate
        self.rate_total=rate_total
        self.notes=notes
class Investment:
    def __init__(self,title):
        self.title=title
        self.Main_Char=Main_Char(0,0,0)
        self.Info=Info(0,0,"","","",0,0)
        self.Contribution=Contribution(0,0,0,0,0,0,0,0)
        self.Credit=Credit(0,0,0,0,0,0,0,0,0)
        self.Rent=Rent(0,0,0,0,0,0,0,0,0,0,0,0)
        self.Eval=Eval(0,0,0,0,"")
    def save(self):
        self.inv=json.dumps(self.Main_Char.__dict__)+json.dumps(self.Info.__dict__)+json.dumps(self.Contribution.__dict__)+json.dumps(self.Credit.__dict__)+json.dumps(self.Rent.__dict__)+json.dumps(self.Eval.__dict__)
        guide=open("guide.txt","r")
        line=guide.readlines()
        num=int(''.join(line[-1:]))
        guide.close()
        guide = open("guide.txt", "a")
        guide.write('\n'+str(num+1)+": "+str(self.title))
        guide.close()
        outfile=open("data.txt", "a")
        outfile.write("IStart__"+str(num)+"__")
        outfile.write(json.dumps(self.inv))
        outfile.write("__End__")
        outfile.close()
g=Investment("Test")
g.save()