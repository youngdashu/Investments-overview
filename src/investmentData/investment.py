import json
import datetime
from types import SimpleNamespace
from typing import List

from src.gui.ui_main_window import Ui_MainWindow

# from src.utilityQtObjectsFunctions.functions import wrongTextEditStyleSheet, correctTextEditStyleSheet
wrongTextEditStyleSheet = """QTextEdit{
    background: rgb(212, 121, 123);
    border: 5px rgb(219, 33, 37);
}
"""

correctTextEditStyleSheet = """QTextEdit{
    background: rgb(207, 206, 209);
    }
"""
noDataText = "Brak danych"


class Main_Char:
    def __init__(self, saved, price, area):
        self.last_saved = saved
        self.price = price
        self.area = area


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
    def __init__(self, ui):
        self.title = "Unnamed"
        self.id = self.getId()
        self.Main_Char = Main_Char(float("inf"), 0, "")
        self.Info = Info(0, 0, "", "", "", 0, 0)
        self.Contribution = Contribution("", "", "", "", "", "", "", "")
        self.Credit = Credit("", "", "", "")
        self.Rent = Rent(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.Eval = Eval(None)

        self.ui: Ui_MainWindow = ui

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
        return id

    def save(self):
        print("zapisuję")
        self.Main_Char.last_saved = str(datetime.datetime.now())
        self.Eval.notes = list(filter(lambda noteStr: noteStr is not None, self.Eval.notes))
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
        try:
            purchasePrice = float(purchasePrice)
            if purchasePrice < 0:
                raise ValueError
            self.Main_Char.price = purchasePrice
            self.ui.text_purchase_price.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_purchase_price.setStyleSheet(wrongTextEditStyleSheet)

    def area(self):
        return self.Main_Char.area

    def setArea(self, area):
        if area is "":
            self.Main_Char.area = 0.0
            self.ui.text_area.setStyleSheet(correctTextEditStyleSheet)
        else:
            try:
                area = float(area)
                if area < 0:
                    raise ValueError
                self.Main_Char.area = area
                self.ui.text_area.setStyleSheet(correctTextEditStyleSheet)
            except ValueError:
                self.ui.text_area.setStyleSheet(wrongTextEditStyleSheet)

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
        try:
            ownContribution = float(ownContribution)
            if ownContribution < 0 or (0 < self.purchasePrice() < ownContribution):
                raise ValueError
            self.Contribution.contr = float(ownContribution)
            self.ui.text_own_contribution.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_own_contribution.setStyleSheet(wrongTextEditStyleSheet)

    def ownContributionPercent(self):
        ownContributionPercent = noDataText
        try:
            ownContributionPercent = str(
                round(float((self.ownContribution() / self.purchasePrice()) * 100), 2)) + "%" if type(
                self.ownContribution()) is not str and type(self.purchasePrice()) is not str else noDataText
        finally:
            return ownContributionPercent

    def brokerMargin(self):
        return self.Contribution.marg_b

    def setBrokerMargin(self, brokerMargin):
        try:
            brokerMargin = float(brokerMargin)
            if brokerMargin < 0:
                raise ValueError
            self.Contribution.marg_b = float(brokerMargin)
            self.ui.text_broker_margin.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_broker_margin.setStyleSheet(wrongTextEditStyleSheet)

    def brokerMarginPercent(self):
        try:
            return str(round(float((self.brokerMargin() / self.purchasePrice()) * 100), 2)) + "%" if type(
                self.brokerMargin()) is not str and type(self.purchasePrice()) is not str else noDataText
        finally:
            return noDataText

    def notaryMargin(self):
        return self.Contribution.marg_n

    def setNotaryMargin(self, notaryMargin):
        try:
            notaryMargin = float(notaryMargin)
            if notaryMargin < 0:
                raise ValueError
            self.Contribution.marg_n = float(notaryMargin)
            self.ui.text_notary_margin.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_notary_margin.setStyleSheet(wrongTextEditStyleSheet)

    def notaryMarginPercent(self):
        try:
            return str(round(float((self.notaryMargin() / self.purchasePrice()) * 100), 2)) + "%" if type(
                self.notaryMargin()) is not str and type(self.purchasePrice()) is not str else noDataText
        finally:
            return noDataText

    def tax(self):
        return self.Contribution.tax

    def setTax(self, tax):
        try:
            tax = float(tax)
            if tax < 0:
                raise ValueError
            self.Contribution.tax = float(tax)
            self.ui.text_tax.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_tax.setStyleSheet(wrongTextEditStyleSheet)

    def taxPercent(self):
        try:
            return str(round(float((self.tax() / self.purchasePrice()) * 100), 2)) + "%" if type(
                self.tax()) is not str and type(self.purchasePrice()) is not str else noDataText
        finally:
            return noDataText

    def otherCosts(self):
        return self.Contribution.other

    def setOtherCosts(self, otherCosts):
        try:
            otherCosts = float(otherCosts)
            if otherCosts < 0:
                raise ValueError
            self.Contribution.other = float(otherCosts)
            self.ui.text_other_costs.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_other_costs.setStyleSheet(wrongTextEditStyleSheet)

    def otherCostsPercent(self):
        try:
            return str(round(float((self.otherCosts() / self.purchasePrice()) * 100), 2)) + "%" if type(
                self.otherCosts()) is not str and type(self.purchasePrice()) is not str else noDataText
        finally:
            return noDataText

    def renovationCost(self):
        return self.Contribution.redec

    def setRenovationCost(self, renovationCost):
        try:
            renovationCost = float(renovationCost)
            if renovationCost < 0:
                raise ValueError
            self.Contribution.redec = float(renovationCost)
            self.ui.text_renovation.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_renovation.setStyleSheet(wrongTextEditStyleSheet)

    def renovationCostPercent(self):
        try:
            return str(round(float((self.renovationCost() / self.purchasePrice()) * 100), 2)) + "%" if type(
                self.renovationCost()) is not str and type(self.purchasePrice()) is not str else noDataText
        finally:
            return noDataText

    def entryCost(self):
        try:
            return float(self.ownContribution()) + float(self.brokerMargin()) + float(self.notaryMargin()) + float(
                self.tax()) + float(self.otherCosts()) + float(self.renovationCost())
        except ValueError:
            return ""

    def investedVsPurchasePrice(self):
        try:
            return self.entryCost() / self.purchasePrice() if type(
                self.entryCost()) is not str and type(self.purchasePrice()) is not str else noDataText
        finally:
            return noDataText

    # noinspection PyBroadException
    def bankCredit(self):
        try:
            return self.purchasePrice() - self.ownContribution()
        except:
            return ""


    def bankContributionPercent(self):
        try:
            return (self.bankCredit() / self.Main_Char.price) if type(
                self.bankCredit()) is not str and type(self.Main_Char.price) is not str else noDataText
        finally:
            return noDataText

    def interestRate(self):
        return self.Credit.rate

    def setInterestRate(self, interestRate):
        try:
            interestRate = float(interestRate)
            if interestRate < 0:
                raise ValueError
            self.Credit.rate = float(interestRate)
            self.ui.text_interest_rate.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_interest_rate.setStyleSheet(wrongTextEditStyleSheet)

    def repaymentPeriod(self):
        return self.Credit.time

    def setRepaymentPeriod(self, period):
        try:
            period = float(period)
            if period < 0:
                raise ValueError
            self.Credit.time = float(period)
            self.ui.text_repayment_period.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_repayment_period.setStyleSheet(wrongTextEditStyleSheet)

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
                float(monthlyInstallmentInterestPart=self.monthlyInstallment() - self.monthlyInstallmentCapitalPart())
        finally:
            return monthlyInstallmentInterestPart

    def creditInsurancePerMonth(self):
        return self.Credit.monthly_insurance

    def setCreditInsurancePerMonth(self, creditInsurance):
        try:
            creditInsurance = float(creditInsurance)
            if creditInsurance < 0:
                raise ValueError
            self.Credit.monthly_insurance = float(creditInsurance)
            self.ui.text_credit_credit_insurance_per_month.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_credit_credit_insurance_per_month.setStyleSheet(wrongTextEditStyleSheet)

    def totalCreditCost(self):
        totalCreditCost = noDataText
        try:
            if self.monthlyInstallment() is not noDataText:
                totalCreditCost = float(self.monthlyInstallment() + self.creditInsurancePerMonth())
        finally:
            return totalCreditCost

    def rentIncomeMinPerMonth(self):
        return self.Rent.income_min

    def setRentIncomeMinPerMonth(self, rentIncome):
        try:
            rentIncome = float(rentIncome)
            if rentIncome < 0:
                raise ValueError
            self.Rent.income_min = float(rentIncome)
            self.ui.text_rent_income_min_month.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_rent_income_min_month.setStyleSheet(wrongTextEditStyleSheet)

    def rentIncomeMaxPerMonth(self):
        return self.Rent.income_max

    def setRentIncomeMaxPerMonth(self, rentIncome):
        try:
            rentIncome = float(rentIncome)
            if rentIncome < 0:
                raise ValueError
            self.Rent.income_max = float(rentIncome)
            self.ui.text_rent_income_max_month.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_rent_income_max_month.setStyleSheet(wrongTextEditStyleSheet)

    def incomeReceivedPerMonth(self):
        return self.Rent.income_real

    def setIncomeReceivedPerMonth(self, income):
        try:
            income = float(income)
            if income < 0:
                raise ValueError
            self.Rent.income_real = float(income)
            self.ui.text_income_earned_month.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_income_earned_month.setStyleSheet(wrongTextEditStyleSheet)

    def rentTaxPerMonth(self):
        return self.Rent.tax_rent

    def setRentTaxPerMonth(self, rentTax):
        try:
            rentTax = float(rentTax)
            if rentTax < 0:
                raise ValueError
            self.Rent.tax_rent = float(rentTax)
            self.ui.text_rent_tax_month.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_rent_tax_month.setStyleSheet(wrongTextEditStyleSheet)

    def propertyTaxPerYear(self):
        return self.Rent.tax_estate

    def setPropertyTaxPerYear(self, propertyTax):
        try:
            propertTax = float(propertyTax)
            if propertTax < 0:
                raise ValueError
            self.Rent.tax_estate = float(propertyTax)
            self.ui.text_property_tax_year.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_property_tax_year.setStyleSheet(wrongTextEditStyleSheet)

    def electricityPerMonth(self):
        return self.Rent.power

    def setElectricityPerMonth(self, electricity):
        try:
            electricity = float(electricity)
            if electricity < 0:
                raise ValueError
            self.Rent.power = float(electricity)
            self.ui.text_electricity_month.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_electricity_month.setStyleSheet(correctTextEditStyleSheet)

    def gasPerMonth(self):
        return self.Rent.gas

    def setGasPerMonth(self, gas):
        try:
            gas = float(gas)
            if gas < 0:
                raise ValueError
            self.Rent.gas = float(gas)
            self.ui.text_gas_month.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_gas_month.setStyleSheet(wrongTextEditStyleSheet)

    def waterPerMonth(self):
        return self.Rent.water

    def setWaterPerMonth(self, water):
        try:
            water = float(water)
            if water < 0:
                raise ValueError
            self.Rent.water = float(water)
            self.ui.text_water_month.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_water_month.setStyleSheet(wrongTextEditStyleSheet)

    def internetPerMonth(self):
        return self.Rent.internet

    def setInternetPerMonth(self, internet):
        try:
            internet = float(internet)
            if internet < 0:
                raise ValueError
            self.Rent.internet = float(internet)
            self.ui.text_internet_month.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_internet_month.setStyleSheet(wrongTextEditStyleSheet)

    def otherPerMonth(self):
        return self.Rent.other

    def setOtherPerMonth(self, other):
        try:
            other = float(other)
            if other < 0:
                raise ValueError
            self.Rent.other = float(other)
            self.ui.text_other_costs_month.setStyleSheet(correctTextEditStyleSheet)
        except ValueError:
            self.ui.text_other_costs_month.setStyleSheet(wrongTextEditStyleSheet)

    def costsTotalPerMonth(self):
        return float(self.Rent.tax_estate) + float(self.Rent.tax_rent) + float(self.Rent.power) + float(
            self.Rent.water) + float(self.Rent.gas) + float(self.Rent.internet) + float(self.Rent.other)

    def gainLossPerMonth(self):
        return self.incomeReceivedPerMonth() - self.costsTotalPerMonth() if type(
            self.incomeReceivedPerMonth()) is not str and type(self.costsTotalPerMonth()) is not str else noDataText

    def gainLossPerYear(self):
        return float((self.incomeReceivedPerMonth() - self.costsTotalPerMonth())) * 12 if type(
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
        totalReturnTimeMonths = noDataText
        try:
            totalReturnTimeMonths = float((self.entryCost() + self.bankCredit()) / self.gainLossPerMonth())
        finally:
            return totalReturnTimeMonths

    def totalReturnTimeYears(self):
        return self.totalReturnTimeMonths() * 12

    def returnRate(self):
        return self.gainLossPerYear() / self.entryCost()

    def notes(self):
        return self.Eval.notes

    def setNotes(self, notes: List[str]):
        self.Eval.notes = notes

    def setNote(self, index: int, note: str):
        self.Eval.notes[index] = note


def getInvestments():
    investments = []
    try:
        f = open('guide.txt', 'x')
        f.close()
    except FileExistsError:
        pass
    with open("guide.txt") as guide:
        for line in guide.readlines():
            if "InvStart__" in line:
                tp = 10
                ids = ""
                titles = ""
                times = ""
                while line[tp].isdigit():
                    ids = ids + line[tp]
                    tp += 1
                tp += 1
                while line[tp].isalpha() or line[tp] == " ":
                    titles = titles + line[tp]
                    tp += 1
                times = line[line.find("last_saved") + 16:line.find("last_saved") + 35]
                investments.append((ids, titles, times))
    return investments


def getInvestmentById(InvestmentId, ui):
    investment = Investment(ui)
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
            if line.find("InvStart__") < 0:
                new = new + line
            else:
                try:
                    tp = 10
                    Id = ""
                    while line[tp].isdigit():
                        Id = Id + line[tp]
                        tp += 1
                    if int(investmentId) != int(Id):
                        new = new + line
                except:
                    pass
    guide = open("guide.txt", "w")
    guide.write(new)
    guide.close()
