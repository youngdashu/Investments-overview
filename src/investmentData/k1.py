import json
from typing import List

noDataText = "Brak danych"


class Main_Char:
    def __init__(self, price, area):
        self.price = price
        self.area = area
        # self.ppm = ppm


class Info:
    def __init__(self, date_start, date_end, desc, address1, address2, estimated_value, estimation_date):
        self.date_start = date_start
        self.date_end = date_end
        self.desc = desc
        self.address1 = address1
        self.address2 = address2
        self.estimated_value = estimated_value
        self.estimation_date = estimation_date


class Contribution:
    def __init__(self, contr, marg_b, marg_n, tax, other, redec, total, purchase):
        self.contr = contr
        self.marg_b = marg_b
        self.marg_n = marg_n
        self.tax = tax
        self.other = other
        self.redec = redec
        self.total = total
        self.purchase = purchase


class Credit:
    def __init__(self, rate, time, monthly_insurance, costs_total):
        self.rate = rate
        self.time = time
        self.monthly_insurance = monthly_insurance
        self.costs_total = costs_total


class Rent:
    def __init__(self, income_min, income_max, income_real, tax_rent, tax_estate, power, gas, water, internet, other,
                 cost_total, gain):
        self.income_min = income_min
        self.income_max = income_max
        self.income_real = income_real
        self.tax_rent = tax_rent
        self.tax_estate = tax_estate
        self.power = power
        self.gas = gas
        self.water = water
        self.internet = internet
        self.other = other
        self.cost_total = cost_total
        self.gain = gain


class Eval:
    def __init__(self, notes=None):
        if notes is None:
            notes = []
        self.notes: List[str] = notes


class Investment:
    def __init__(self):
        self.title = "Unnamed"
        self.id = self.getId()
        print(self.id)
        self.Main_Char = Main_Char(float("inf"), 0)
        self.Info = Info(0, 0, "", "", "", 0, 0)
        self.Contribution = Contribution(0, 0, 0, 0, 0, 0, 0, 0)
        self.Credit = Credit(float("inf"), 0, 0, 0)
        self.Rent = Rent(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.Eval = Eval(None)

    def getId(self):
        guide = open("guide.txt", "r+")
        text = guide.readlines()
        try:
            id = int(text[0]) + 1
            text[0] = str(id) + "\n"
            guide.close()
            guide = open("guide.txt", "w")
            guide.writelines(text)
            guide.close()
        except:
            guide.close()
            id = 0
            guide = open("guide.txt", "w")
            guide.writelines("0")
            guide.close()
        return (id)

    def save(self):
        print("zapisuję")
        self.inv = self.title + json.dumps(self.Main_Char.__dict__) + json.dumps(self.Info.__dict__) + json.dumps(
            self.Contribution.__dict__) + json.dumps(self.Credit.__dict__) + json.dumps(
            self.Rent.__dict__) + json.dumps(self.Eval.__dict__)
        outfile = open("guide.txt", "a")
        outfile.write("\n" + "InvStart__" + str(self.id))
        outfile.write(json.dumps(self.inv))
        outfile.write("__InvEnd")
        outfile.close()

    def setTitle(self, title):
        print("setting title to " + title + " inv: ", self)
        self.title = title

    def purchasePrice(self):
        return self.Main_Char.price

    def setPurchasePrice(self, purchasePrice):
        print("set purchase price ", purchasePrice)
        self.Main_Char.price = float(purchasePrice)

    def area(self):
        return self.Main_Char.area

    def setArea(self, area):
        self.Main_Char.area = float(area)

    def pricePerSquareMeter(self):
        pricePerSquareMeter = noDataText
        try:
            pricePerSquareMeter = float(self.purchasePrice()) / float(self.area())
        finally:
            return pricePerSquareMeter

    def startDate(self):
        return self.Info.date_start

    def setStartDate(self, startDate):
        self.Info.date_start = startDate

    def description(self):
        return self.Info.desc

    def setDescription(self, description):
        self.Info.desc = description

    def addressStreet(self):
        return self.Info.address1

    def setAddressStreet(self, addressStreet):
        self.Info.address1 = addressStreet

    def addressCity(self):
        return self.Info.address2

    def setAddressCity(self, addressCity):
        self.Info.address2 = addressCity

    def estimatedCurrentValue(self):
        return self.Info.estimated_value

    def setEstimatedCurrentValue(self, estimatedCurrentValue):
        self.Info.estimated_value = estimatedCurrentValue

    def lastEstimationDate(self):
        return self.Info.estimation_date

    def setLastEstimationDate(self, lastEstimationDate):
        self.Info.estimation_date = lastEstimationDate

    def finishDate(self):
        return self.Info.date_end

    def setFinishDate(self, finishDate):
        self.Info.date_end = finishDate

    def ownContribution(self):
        return self.Contribution.contr

    def setOwnContribution(self, ownContribution):
        self.Contribution.contr = float(ownContribution)

    def ownContributionPercent(self):
        ownContributionPercent = str(int((self.ownContribution() / self.purchasePrice()) * 100)) + "%" if type(
            self.ownContribution()) is not str and type(self.purchasePrice()) is not str else noDataText
        return ownContributionPercent

    def brokerMargin(self):
        return self.Contribution.marg_b

    def setBrokerMargin(self, brokerMargin):
        self.Contribution.marg_b = float(brokerMargin)

    def brokerMarginPercent(self):
        return str(int((self.brokerMargin() / self.purchasePrice()) * 100)) + "%" if type(
                self.brokerMargin()) is not str and type(self.purchasePrice()) is not str else noDataText

    def notaryMargin(self):
        return self.Contribution.marg_n

    def setNotaryMargin(self, notaryMargin):
        self.Contribution.marg_n = float(notaryMargin)

    def notaryMarginPercent(self):
        return str(int((self.notaryMargin() / self.purchasePrice()) * 100)) + "%" if type(
                self.notaryMargin()) is not str and type(self.purchasePrice()) is not str else noDataText

    def tax(self):
        return self.Contribution.tax

    def setTax(self, tax):
        self.Contribution.tax = float(tax)

    def taxPercent(self):
        return str(int((self.tax() / self.purchasePrice()) * 100)) + "%" if type(
            self.tax()) is not str and type(self.purchasePrice()) is not str else noDataText

    def otherCosts(self):
        return self.Contribution.other

    def setOtherCosts(self, otherCosts):
        self.Contribution.other = float(otherCosts)

    def otherCostsPercent(self):
        return str(int((self.otherCosts() / self.purchasePrice()) * 100)) + "%" if type(
                self.otherCosts()) is not str and type(self.purchasePrice()) is not str else noDataText

    def renovationCost(self):
        return self.Contribution.redec

    def setRenovationCost(self, renovationCost):
        self.Contribution.redec = float(renovationCost)

    def renovationCostPercent(self):
        return str(int((self.renovationCost() / self.purchasePrice()) * 100)) + "%" if type(
                self.renovationCost()) is not str and type(self.purchasePrice()) is not str else noDataText

    def entryCost(self):
        return int(
            int(self.ownContribution()) + int(self.brokerMargin()) + int(self.notaryMargin()) + int(self.tax()) + int(
                self.otherCosts()) + int(self.renovationCost()))

    def investedVsPurchasePrice(self):
        return self.entryCost() / self.purchasePrice() if type(
            self.entryCost()) is not str and type(self.purchasePrice()) is not str else noDataText

    def bankCredit(self):
        return self.Main_Char.price - self.Contribution.contr if type(
            self.Main_Char.price) is not str and type(self.Contribution.contr) is not str else noDataText

    def bankContributionPercent(self):
        return self.bankCredit() / self.Main_Char.price if type(
            self.bankCredit()) is not str and type(self.Main_Char.price) is not str else noDataText

    def interestRate(self):
        return self.Credit.rate

    def setInterestRate(self, interestRate):
        self.Credit.rate = float(interestRate)

    def repaymentPeriod(self):
        return self.Credit.time

    def setRepaymentPeriod(self, period):
        self.Credit.time = float(period)

    def monthlyInstallment(self):
        monthlyInstallment = noDataText
        try:
            monthlyInstallment = float((self.bankCredit() * self.interestRate()) / (
                    12 * (1 - (12 / (12 + self.interestRate())) ** self.repaymentPeriod())))
        finally:
            return monthlyInstallment

    def monthlyInstallmentCapitalPart(self):
        monthlyInstallmentCapitalPart = noDataText
        try:
            monthlyInstallmentCapitalPart = float(self.bankCredit() / self.repaymentPeriod())
        finally:
            return monthlyInstallmentCapitalPart

    def monthlyInstallmentInterestPart(self):
        monthlyInstallmentInterestPart = noDataText
        try:
            if self.monthlyInstallment() is not noDataText:
                float(monthlyInstallmentInterestPart = self.monthlyInstallment() - self.monthlyInstallmentCapitalPart())
        finally:
            return monthlyInstallmentInterestPart

    def creditInsurancePerMonth(self):
        return self.Credit.monthly_insurance

    def setCreditInsurancePerMonth(self, creditInsurance):
        self.Credit.monthly_insurance = float(creditInsurance)

    def totalCreditCost(self):
        totalCreditCost = noDataText
        try:
            if self.monthlyInstallment() is not noDataText:
                float(totalCreditCost = self.monthlyInstallment() + self.creditInsurancePerMonth())
        finally:
            return totalCreditCost

    def rentIncomeMinPerMonth(self):
        return self.Rent.income_min

    def setRentIncomeMinPerMonth(self, rentIncome):
        self.Rent.income_min = rentIncome

    def rentIncomeMaxPerMonth(self):
        return self.Rent.income_max

    def setRentIncomeMaxPerMonth(self, rentIncome):
        self.Rent.income_max = rentIncome

    def incomeReceivedPerMonth(self):
        return self.Rent.income_real

    def setIncomeReceivedPerMonth(self, income):
        self.Rent.income_real = float(income)

    def rentTaxPerMonth(self):
        return self.Rent.tax_rent

    def setRentTaxPerMonth(self, rentTax):
        self.Rent.tax_rent = float(rentTax)

    def propertyTaxPerYear(self):
        return self.Rent.tax_estate

    def setPropertyTaxPerYear(self, propertyTax):
        self.Rent.tax_estate = float(propertyTax)

    def electricityPerMonth(self):
        return self.Rent.power

    def setElectricityPerMonth(self, electricity):
        self.Rent.power = float(electricity)

    def gasPerMonth(self):
        return self.Rent.gas

    def setGasPerMonth(self, gas):
        self.Rent.gas = float(gas)

    def waterPerMonth(self):
        return self.Rent.water

    def setWaterPerMonth(self, water):
        self.Rent.water = float(water)

    def internetPerMonth(self):
        return self.Rent.internet

    def setInternetPerMonth(self, internet):
        self.Rent.internet = float(internet)

    def otherPerMonth(self):
        return self.Rent.other

    def setOtherPerMonth(self, other):
        self.Rent.other = float(other)

    def costsTotalPerMonth(self):
        return float(self.Rent.tax_estate) + float(self.Rent.tax_rent) + float(self.Rent.power) + float(
            self.Rent.water) + float(self.Rent.gas) + float(self.Rent.internet) + float(self.Rent.other)

    def gainLossPerMonth(self):
        return self.incomeReceivedPerMonth() - self.costsTotalPerMonth() if type(
            self.incomeReceivedPerMonth()) is not str and type(self.costsTotalPerMonth()) is not str else noDataText

    def gainLossPerYear(self):
        return (self.incomeReceivedPerMonth() - self.costsTotalPerMonth()) * 12 if type(
            self.incomeReceivedPerMonth()) is not str and type(self.costsTotalPerMonth()) is not str else noDataText

    def ownCapitalReturnTimeMonths(self):
        ownCapitalReturnTimeMonths = noDataText
        try:
            ownCapitalReturnTimeMonths = self.entryCost() / self.gainLossPerMonth()
        finally:
            return ownCapitalReturnTimeMonths

    def ownCapitalReturnTimeYears(self):
        ownCapitalReturnTimeYears = noDataText
        try:
            ownCapitalReturnTimeYears = (self.entryCost() / self.gainLossPerMonth()) * 12
        finally:
            return ownCapitalReturnTimeYears

    def totalReturnTimeMonths(self):
        return (self.entryCost() + self.bankCredit()) / self.gainLossPerMonth()

    def totalReturnTimeYears(self):
        return self.totalReturnTimeMonths() * 12

    def notes(self):
        return self.Eval.notes

    def setNotes(self, notes: List[str]):
        self.Eval.notes = notes

    def setNote(self, index: int, note: str):
        self.Eval.notes[index] = note


def getInvestments():
    investments = []
    with open("guide.txt") as guide:
        for line in guide.readlines():
            if "InvStart__" in line:
                tp = 10
                ids = ""
                titles = ""
                while line[tp].isdigit():
                    ids = ids + line[tp]
                    tp += 1
                tp += 1
                while line[tp].isalpha() or line[tp] == " ":
                    titles = titles + line[tp]
                    tp += 1
                investments.append((ids, titles))
    return investments


def getInvestmentById(InvestmentId):
    investment = Investment()
    with open("guide.txt") as guide:
        for line in guide.readlines():
            if "InvStart__" in line:
                tp = 10
                Id = ""
                ti = ""
                while line[tp].isdigit():
                    Id = Id + line[tp]
                    tp += 1
                if int(Id) == InvestmentId:
                    investment.id = int(Id)
                    tp += 1
                    while line[tp] != "{":
                        ti = ti + line[tp]
                        tp += 1
                    investment.title = ti
                    leng = tp + 1
                    while line[leng] != "}":
                        leng += 1
                    investment.Main_Char = json.loads(line[tp:leng + 1].replace('\\', ''),
                                                      object_hook=lambda d: SimpleNamespace(**d))
                    tp = leng + 1
                    leng += 2
                    while line[leng] != "}":
                        leng += 1
                    investment.Info = json.loads(line[tp:leng + 1].replace('\\', ''),
                                                 object_hook=lambda d: SimpleNamespace(**d))
                    tp = leng + 1
                    leng += 2
                    while line[leng] != "}":
                        leng += 1
                    investment.Contribution = json.loads(line[tp:leng + 1].replace('\\', ''),
                                                         object_hook=lambda d: SimpleNamespace(**d))
                    tp = leng + 1
                    leng += 2
                    while line[leng] != "}":
                        leng += 1
                    investment.Credit = json.loads(line[tp:leng + 1].replace('\\', ''),
                                                   object_hook=lambda d: SimpleNamespace(**d))
                    tp = leng + 1
                    leng += 2
                    while line[leng] != "}":
                        leng += 1
                    investment.Rent = json.loads(line[tp:leng + 1].replace('\\', ''),
                                                 object_hook=lambda d: SimpleNamespace(**d))
                    tp = leng + 1
                    leng += 2
                    while line[leng] != "}":
                        leng += 1
                    investment.Eval = json.loads(line[tp:leng + 1].replace('\\', ''),
                                                 object_hook=lambda d: SimpleNamespace(**d))
    return investment


def deleteInvestmentById(investmentId):
    new = ""
    with open("guide.txt") as guide:
        for line in guide.readlines():
            if new == "":
                new = line
            else:
                tp = 10
                Id = ""
                while line[tp].isdigit():
                    Id = Id + line[tp]
                    tp += 1
                if investmentId != int(Id):
                    new = new + line
    guide = open("guide.txt", "w")
    guide.write(new)
    guide.close()

# g = Investment()
# g.save()

# print(getInvestments())
