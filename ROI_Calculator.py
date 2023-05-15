
# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming 
# create a program that will calculate the Return on Investment(ROI) for a 
# rental property.



class RentalROI():
    """Calculate the Return on Investment (ROI) for a rental property."""

    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cash_flow = 0
        self.ROI = 0

    

    def calc_income(self):
        print("\n\n--------------------- Monthly Income ---------------------")

        print("\n\nPlease fill in the information below (enter 0 if none)")
        print("(what your tenants pay for monthly)\n")


        num_of_units = int(input("Total number of units: "))

        rent = int(input("Cost of Rent: "))

        misc_fees = int(input("Other Fees (laundry, storage, etc.): "))


        self.income = num_of_units * (rent + misc_fees)

        print(f"\n\nYour Monthly Income for this property is " +
              f"${self.income}.\n\n")
    


    def calc_expenses(self):
        print("\n\n-------------------- Monthly Expenses --------------------")

        print("\n\nPlease fill in the information below (enter 0 if none)")
        print("(what you pay for monthly)\n")

        self.expenses += int(input("Property Tax: "))

        self.expenses += int(input("Total Insurance: "))

        self.expenses += int(input("Utilities: "))

        self.expenses += int(input("HOA (Home Owners Association) Fee: "))

        self.expenses += int(input("Lawn care / Snow removal: "))

        self.expenses += int(input("Vacancy: "))

        self.expenses += int(input("Repairs: "))

        self.expenses += int(input("Capital Expenditures: "))

        self.expenses += int(input("Property Management: "))

        self.expenses += int(input("Mortgage: "))

        print(f"\n\nYour Total Monthly Expenses for this property is " +
              f"${self.expenses}.\n\n")



    def calc_cash_flow(self):
        print("\n\n-------------------- Monthly Cash Flow --------------------")

        self.cash_flow = self.income - self.expenses
        print(f"\n\nYour monthly cash flow (profit) is " +
              f"${self.cash_flow}.\n\n\n")



    def calc_ROI(self):
        print("\n\n------------------ Return on Investment ------------------")

        print("\n\nPlease fill in the information below (enter 0 if none)")
        print("(Info regarding your property purchase)\n")

        total_invest = int(input("Down Payment: "))
        total_invest += int(input("Closing Costs: "))
        total_invest += int(input("Rehab Budget: "))
        total_invest += int(input("Misc Other: "))

        self.ROI = ((12 * self.cash_flow) / total_invest) * 100

        print(f"\n\nYour ROI for your rental property is {self.ROI}%")
        print(f"\nThis means that you earned {self.ROI}% of your investment " +
              "back in one year of leasing your property out to tenants.\n\n")

    

    def runner(self):
        print("\n============== Rental Property ROI Calculator ==============")
        print("\n\nWelcome to the Rental Property Return-On-Investment " + 
              "Calculator!")

        print("\nIn order to calculate your property's ROI, we'll first need " +
              "to figure out your property's income, expenses, and cash " +
              "flow.\n\n\n")
        
        while True:
            self.calc_income()
            self.calc_expenses()
            self.calc_cash_flow()
            self.calc_ROI()

            response = (input("\nDo you want to calculate the ROI for another "+
                              "rental property? (y/n) ")).lower()
            if response == 'n' or response == 'no':
                break




my_roi_calculator = RentalROI()

my_roi_calculator.runner()