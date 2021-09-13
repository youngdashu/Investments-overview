import json

noDataText = "Brak danych"


class Main_Char:
    def __init__(self, price, area, ppm):
        self.price = price
        self.area = area
        self.ppm = ppm


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
    def __init__(self, notes):
        self.notes = notes


class Investment:
    def __init__(self):
        self.title = ""
        self.id = self.getId()
        self.Main_Char = Main_Char(float("inf"), 0, 0)
        self.Info = Info(0, 0, "", "", "", 0, 0)
        self.Contribution = Contribution(0, 0, 0, 0, 0, 0, 0, 0)
        self.Credit = Credit(float("inf"), 0, 0, 0)
        self.Rent = Rent(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.Eval = Eval("")

    def getId(self):
        pass

    def save(self):
        self.inv = json.dumps(self.Main_Char.__dict__) + json.dumps(self.Info.__dict__) + json.dumps(
            self.Contribution.__dict__) + json.dumps(self.Credit.__dict__) + json.dumps(
            self.Rent.__dict__) + json.dumps(self.Eval.__dict__)
        guide = open("guide.txt", "r")
        line = guide.readlines()
        num = int(''.join(line[-1:]))
        guide.close()
        guide = open("guide.txt", "a")
        guide.write('\n' + str(num + 1) + ": " + str(self.title))
        guide.close()
        outfile = open("data.txt", "a")
        outfile.write("IStart__" + str(num) + "__")
        outfile.write(json.dumps(self.inv))
        outfile.write("__End__")
        outfile.close()

    def setTitle(self, title):
        print("setting title to " + title + " inv: ", self)
        self.title = title

    def purchasePrice(self):
        return self.Main_Char.price

    def setPurchasePrice(self, purchasePrice):
        self.Main_Char.price = purchasePrice

    def area(self):
        return self.Main_Char.area

    def setArea(self, area):
        self.Main_Char.area = area

    def pricePerSquareMeter(self):
        return self.Main_Char.ppm

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
        self.Contribution.contr = ownContribution

    def brokerMargin(self):
        return self.Contribution.marg_b

    def setBrokerMargin(self, brokerMargin):
        self.Contribution.marg_b = brokerMargin

    def notaryMargin(self):
        return self.Contribution.marg_n

    def setNotaryMargin(self, notaryMargin):
        self.Contribution.marg_n = notaryMargin

    def tax(self):
        return self.Contribution.tax

    def setTax(self, tax):
        self.Contribution.tax = tax

    def otherCosts(self):
        return self.Contribution.other

    def setOtherCosts(self, otherCosts):
        self.Contribution.other = otherCosts

    def renovationCost(self):
        return self.Contribution.redec

    def setRenovationCost(self, renovationCost):
        self.Contribution.redec = renovationCost

    def entryCost(self):
        return self.ownContribution() + self.brokerMargin() + self.notaryMargin() + self.tax() + self.otherCosts() + self.renovationCost()

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
        self.Credit.rate = interestRate

    def repaymentPeriod(self):
        return self.Credit.time

    def setRepaymentPeriod(self, period):
        self.Credit.time = period

    def monthlyInstallment(self):
        monthlyInstallment = noDataText
        try:
            monthlyInstallment = (self.bankCredit() * self.interestRate()) / (
                    12 * (1 - (12 / (12 + self.interestRate())) ** self.repaymentPeriod()))
        finally:
            return monthlyInstallment

    def monthlyInstallmentCapitalPart(self):
        monthlyInstallmentCapitalPart = noDataText
        try:
            monthlyInstallmentCapitalPart = self.bankCredit() / self.repaymentPeriod()
        finally:
            return monthlyInstallmentCapitalPart

    def monthlyInstallmentInterestPart(self):
        monthlyInstallmentInterestPart = noDataText
        try:
            monthlyInstallmentInterestPart = self.monthlyInstallment() - self.monthlyInstallmentCapitalPart()
        finally:
            return monthlyInstallmentInterestPart

    def creditInsurancePerMonth(self):
        return self.Credit.monthly_insurance

    def setCreditInsurancePerMonth(self, creditInsurance):
        self.Credit.monthly_insurance = creditInsurance

    def totalCreditCost(self):
        totalCreditCost = noDataText
        try:
            totalCreditCost = self.monthlyInstallment() + self.creditInsurancePerMonth()
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
        self.Rent.income_real = income

    def rentTaxPerMonth(self):
        return self.Rent.tax_rent

    def setRentTaxPerMonth(self, rentTax):
        self.Rent.tax_rent = rentTax

    def propertyTaxPerYear(self):
        return self.Rent.tax_estate

    def setPropertyTaxPerYear(self, propertyTax):
        self.Rent.tax_estate = propertyTax

    def electricityPerMonth(self):
        return self.Rent.power

    def setElectricityPerMonth(self, electricity):
        self.Rent.power = electricity

    def gasPerMonth(self):
        return self.Rent.gas

    def setGasPerMonth(self, gas):
        self.Rent.gas = gas

    def waterPerMonth(self):
        return self.Rent.water

    def setWaterPerMonth(self, water):
        self.Rent.water = water

    def internetPerMonth(self):
        return self.Rent.internet

    def setInternetPerMonth(self, internet):
        self.Rent.internet = internet

    def otherPerMonth(self):
        return self.Rent.other

    def setOtherPerMonth(self, other):
        self.Rent.other = other

    def costsTotalPerMonth(self):
        return self.Rent.tax_estate + self.Rent.tax_rent + self.Rent.power + self.Rent.water + self.Rent.gas + self.Rent.internet + self.Rent.other

    def incomeOrLossPerMonth(self):
        return self.incomeReceivedPerMonth() - self.costsTotalPerMonth() if type(
            self.incomeReceivedPerMonth()) is not str and type(self.costsTotalPerMonth()) is not str else noDataText

    def ownCapitalReturnTimeMonths(self):
        ownCapitalReturnTimeMonths = noDataText
        try:
            ownCapitalReturnTimeMonths = self.entryCost() / self.incomeOrLossPerMonth()
        finally:
            return ownCapitalReturnTimeMonths

    def ownCapitalReturnTimeYears(self):
        return self.ownCapitalReturnTimeMonths() * 12

    def totalReturnTimeMonths(self):
        return (self.entryCost() + self.bankCredit()) / self.incomeOrLossPerMonth()

    def totalReturnTimeYears(self):
        return self.totalReturnTimeMonths() * 12

# g = Investment()
# g.save()
