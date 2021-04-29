''' program: invsetmentGUI.py
    Author: Jami
    Date: 4/21/21 '''

from breezypythongui import EasyFrame

class TextAreaDemo(EasyFrame):
    """An investment calculator that demonstrates the use of a multi-line text area widget."""
    def __init__(self):
        """sets up window and the widgets."""
        EasyFrame.__init__(self)
        self.addLabel(text = "Initial Amount", row = 0, column = 0)
        self.addLabel(text = "Number of years", row = 1, column = 0)
        self.addLabel(text = "Interest Rate in %", row = 2, column = 0)
        self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
        self.period = self.addIntegerField(value = 0, row = 1, column = 1)
        self.rate = self.addIntegerField(value = 0, row = 2, column = 1)
        self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height =15)
        self.button = self.addButton(text = "compute", row = 3, column = 0, columnspan = 2, command = self.compute)
                 
        #change the button color!
        self.button["background"] = "yellow"


    def compute(self):
        """ compute the investment report based on the inpute and output of the full report."""
        # Input phase
        startBalance = self.amount.getNumber()
        years = self.period.getNumber()
        rate = self.rate.getNumber()
        #if any of the inputs are a zero, just exit the function
        if startBalance == 0 or rate == 0 or years == 0:
            self.outputArea.setText("Please make sure that none of the inputs contain a ZE")
            return

        # Calculation phase
        # Covernt the rate to a decimal number
        rate = rate / 100

        # Initialize the accumulator for the interest
        totalInterest = 0.0

        # Display the header for the table in tabular notation
        result = "%4s %18s %10s %16s \n" % \
                ("Year", "Starting Balance", "Interest", "Ending Balance")

        # Compute and display the results for each year
        for year in range(1, years + 1):
                interest = startBalance * rate
                endBalance = startBalance + interest
                result += "%4d %18.2f %10.2f %16.2f \n" % \
                    (year, startBalance, interest, endBalance)
                startBalance = endBalance
                totalInterest += interest

        # append the total to the result string for the entire report
            
        result += "Ending balance: $%0.2f \n" % endBalance
        result += "Total interest earned: $%0.2f \n" % totalInterest

        # output the result while preserving read- only status
        self.outputArea["State"] = "normal"
        self.outputArea.setText(result)
        self.outputArea["state"] = "disabled"


# definition of the main() function for program entery
def main():
	""" instantiates and pops up the window."""
	TextAreaDemo().mainloop()


#globel call to the main() function
main()