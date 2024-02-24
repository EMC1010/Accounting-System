from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime

class Inventory:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Inventory System")
        self.root.geometry("1350x800")
        self.root.configure(background='#FFC0CB')

        #=================================FRAMES============================

        MainFrame = Frame(self.root, bd=20, width = 1350, height=700, bg='#cbffc0', relief=RIDGE)
        MainFrame.grid()

        LeftFrame = Frame(MainFrame, bd=10, width = 750, height=600, padx=10, bg='#c0cbff', relief=RIDGE)
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(MainFrame, bd=5, width = 560, height=600, padx=10, bg='#c0cbff', relief=RIDGE)
        RightFrame.pack(side=RIGHT)

        #=================================Frames for the ff widget, Text, Labels, Entry Widget============================
        LeftFrame0 = Frame(LeftFrame, bd=5, width = 712, height=143, padx=10, bg='#fff4c0', relief=RIDGE)
        LeftFrame0.grid(row=0, column=0)
        LeftFrame1 = Frame(LeftFrame, bd=5, width = 712, height=170, padx=10, bg='#fff4c0', relief=RIDGE)
        LeftFrame1.grid(row=1, column=0)
        LeftFrame2 = Frame(LeftFrame, bd=5, width = 712, height=168, padx=10, bg='#fff4c0', relief=RIDGE)
        LeftFrame2.grid(row=2, column=0)
        LeftFrame3 = Frame(LeftFrame, bd=5, width = 712, height=95, padx=10, bg='#fff4c0', relief=RIDGE)
        LeftFrame3.grid(row=3, column=0)

        RightFrame0 = Frame(RightFrame, bd=5, width = 522, height=200, padx=5, bg='#c0cbff', relief=RIDGE)
        RightFrame0.grid(row=0, column=0)
        RightFrame1 = Frame(RightFrame, bd=5, width = 522, height=280, padx=5, bg='#c0cbff', relief=RIDGE)
        RightFrame1.grid(row=1, column=0)
        RightFrame2 = Frame(RightFrame, bd=5, width = 522, height=95, padx=5, bg='#c0cbff', relief=RIDGE)
        RightFrame2.grid(row=2, column=0)

        AcctOpen = StringVar()
        AppDate = StringVar()
        NCreR = StringVar()
        LCreR = StringVar()
        DateRev = StringVar()
        ProdCode = StringVar()
        ProdType = StringVar()
        NumOfDays = StringVar()
        CostPerDay = StringVar()
        CredLimit = StringVar()
        CreCheck = StringVar()
        SettleDueDay = StringVar()
        PaymentD = StringVar()
        Discount = StringVar()
        Deposit = StringVar()
        PayDueDay = StringVar()
        PaymentM = StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        Tax = StringVar()
        SubTotal = StringVar()
        Total = StringVar()
        Receipt_Ref = StringVar()

        def Product(evt):
            values = str(self.cboProdType.get())
            pType = values
            if pType == "QA":
                ProdCode.set("QA123")
                CostPerDay.set("$450")
                CreCheck.set("No")
                SettleDueDay.set("10")
                PayDueDay.set("No")
                PaymentD.set("No")
                Deposit.set("No")
                PaymentM.set("Bank")

                n = float(LCreR.get())
                s = float(SettleDueDay.get())
                price = (n * s)
                TC = "$", str('%.2f'%(price ))
                PayDueDay.set(TC)

            elif pType == "Developer":
                ProdCode.set("Dev456")
                CostPerDay.set("$650")
                CreCheck.set("No")
                SettleDueDay.set("21")
                PayDueDay.set("No")
                PaymentD.set("No")
                Deposit.set("No")
                PaymentM.set("Cash")

                n = float(LCreR.get())
                s = float(SettleDueDay.get())
                price = (n * s)
                TC = "$", str('%.2f'%(price ))
                PayDueDay.set(TC)
        
            elif pType == "Technician":
                ProdCode.set("Tech789")
                CostPerDay.set("$100")
                CreCheck.set("No")
                SettleDueDay.set("6")
                PayDueDay.set("No")
                PaymentD.set("No")
                Deposit.set("No")
                PaymentM.set("GCash")

                n = float(LCreR.get())
                s = float(SettleDueDay.get())
                price = (n * s)
                TC = "$", str('%.2f'%(price ))
                PayDueDay.set(TC)

            elif pType == "IT Manager":
                ProdCode.set("IT-M012")
                CostPerDay.set("$900")
                CreCheck.set("No")
                SettleDueDay.set("18")
                PayDueDay.set("No")
                PaymentD.set("No")
                Deposit.set("No")
                PaymentM.set("Visa")

                n = float(LCreR.get())
                s = float(SettleDueDay.get())
                price = (n * s)
                TC = "$", str('%.2f'%(price ))
                PayDueDay.set(TC)

        def TotalCost():
            n = float(LCreR.get())
            s = float(SettleDueDay.get())
            price = (n * s)
            ST = "$",str('%.2f'%(price))
            iTax = "$",str('%.2f'%((price)*0.15))
            Tax.set(iTax)
            SubTotal.set(ST)
            TC = "$",str('%.2f'%(((price)*0.15)+price))
            Total.set(TC)

            self.txtReceipt.delete("1.0",END)
            x = random.randint(10908, 500876)
            randomRef = str(x)
            Receipt_Ref.set("BILL"+ randomRef)

            self.txtReceipt.insert(END,'Receipt Ref:\t\t\t\t'+ Receipt_Ref.get() +'\t\t\t'+ AppDate.get() +"\n")        
            self.txtReceipt.insert(END,'\nProduct Type:\t\t\t\t'+ ProdType.get() +"\n")
            self.txtReceipt.insert(END,'\nProduct Code:\t\t\t\t'+ ProdCode.get() +"\n")
            self.txtReceipt.insert(END,'\nNumber Of Days:\t\t\t\t'+ NumOfDays.get() +"\n")
            self.txtReceipt.insert(END,'\nAccount Open:\t\t\t\t'+ AcctOpen.get() +"\n")
            self.txtReceipt.insert(END,'\nNext Credit Review:\t\t\t\t'+ NCreR.get() +"\n")
            self.txtReceipt.insert(END,'\nLast Credit Review:\t\t\t\t'+ LCreR.get() +"\n")
            self.txtReceipt.insert(END,'\nTax:\t\t\t\t'+ Tax.get() +"\n")
            self.txtReceipt.insert(END,'\nSubTotal:\t\t\t\t'+ str(SubTotal.get()) +"\n")
            self.txtReceipt.insert(END,'\nTotal Cost:\t\t\t\t' + str(Total.get()))
                    
        def CheckCredit():
            if(var1.get() == 1):
                self.txtInfo.insert(END,"\tCheck Credit Approved\n")
            elif var1.get() == 0:
                self.txtInfo.delete("1.0",END)

        def TermAgreed():
            if(var2.get() == 1):
                self.txtInfo.insert(END,"\tTerm Agreed\n")
            elif var2.get() == 0:
                self.txtInfo.delete("1.0",END)

        def AccountOnHold():
            if(var3.get() == 1):
                self.txtInfo.insert(END,"\tAccount On Hold\n")
            elif var3.get() == 0:
                self.txtInfo.delete("1.0",END)
    
        def RestrictMailing():
            if(var4.get() == 1):
                self.txtInfo.insert(END,"\tRestrict Mailing\n")
            elif var4.get() == 0:
                self.txtInfo.delete("1.0",END)

        def Reset():
            AcctOpen.set("")
            AppDate.set("")
            NCreR.set("")
            LCreR.set("")
            DateRev.set("")
            ProdCode.set("")
            ProdType.set("")
            NumOfDays.set("")
            CostPerDay.set("")
            CredLimit.set("")
            CreCheck.set("")
            SettleDueDay.set("")
            PaymentD.set("")
            Discount.set("")
            Deposit.set("")
            PayDueDay.set("")
            PaymentM.set("")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            Tax.set("")
            SubTotal.set("")
            Total.set("")
            self.txtInfo.delete("1.0",END)
            self.txtReceipt.delete("1.0",END)
            return

        def iExit():
            iExit=tkinter.messagebox.askyesno("Inventory Systems", "Confirm if you want to exit")
            if iExit >0:
                root.destroy()
                return
        
        def iDates(evt):
            values = str(self.cboNumOfDays.get())
            NumOfDays = values
            if NumOfDays == "1-30":
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=30)
                d3 = (d1+d2)
                AppDate.set(d1)
                NCreR.set(d3)
                LCreR.set(30)
                DateRev.set(d3)

                CredLimit.set("$1,000")
                Discount.set("5%")
                AcctOpen.set("Yes")

            elif (NumOfDays == "31-90"):
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=90)
                d3 = (d1+d2)
                AppDate.set(d1)
                NCreR.set(d3)
                LCreR.set(90)
                DateRev.set(d3)

                CredLimit.set("$1,500")
                Discount.set("10%")
                AcctOpen.set("Yes")
            
            elif (NumOfDays == "91-270"):
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=270)
                d3 = (d1+d2)
                AppDate.set(d1)
                NCreR.set(d3)
                LCreR.set(270)
                DateRev.set(d3)

                CredLimit.set("$10,000")
                Discount.set("15%")
                AcctOpen.set("Yes")

            elif (NumOfDays == "271-365"):
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=365)
                d3 = (d1+d2)
                AppDate.set(d1)
                NCreR.set(d3)
                LCreR.set(365)
                DateRev.set(d3)

                CredLimit.set("$50,000")
                Discount.set("20%")
                AcctOpen.set("Yes")
            
            elif (NumOfDays == "0"):
                messagebox.showinfo("Zero selected", "You choose zero?")
        #=================================LeftFrame0==============================================
        self.lblProdType=Label(LeftFrame0, font=('arial', 16, 'bold'), text="Product Type:", padx=2, pady=16, bg='#fff4c0')
        self.lblProdType.grid(row=0, column=0, sticky=W)

        self.cboProdType = ttk.Combobox(LeftFrame0, textvariable=ProdType, state='read only', font=('arial', 18, 'bold'), width=12)
        self.cboProdType.bind("<<ComboboxSelected>>", Product)
        self.cboProdType['value'] = ('', 'Select an option', 'QA', 'Developer', 'Technician', 'IT Manager')
        self.cboProdType.current(0)
        self.cboProdType.grid(row=0, column=1)

        self.lblNumOfDays=Label(LeftFrame0, font=('arial', 16, 'bold'), text="Number Of Days:", padx=2, pady=2, bg='#fff4c0')
        self.lblNumOfDays.grid(row=0, column=2, sticky=W)

        self.cboNumOfDays = ttk.Combobox(LeftFrame0, textvariable=NumOfDays, state='read only', font=('arial', 18, 'bold'), width=12)
        self.cboNumOfDays.bind("<<ComboboxSelected>>", iDates)
        self.cboNumOfDays['value'] = ('0', '1-30', '31-90', '91-270', '271-365')
        self.cboNumOfDays.current(0)
        self.cboNumOfDays.grid(row=0, column=3)


        self.lblProdCode=Label(LeftFrame0, font=('arial', 16, 'bold'), text="Product Code:", padx=1, pady=16, bg='#fff4c0')
        self.lblProdCode.grid(row=1, column=0, sticky=W)

        self.txtProdCode=Entry(LeftFrame0, textvariable=ProdCode, font=('arial', 16, 'bold'), bd=8, fg="black", width=14, justify=RIGHT).grid(row=1, column=1)

        self.lblProdCode=Label(LeftFrame0, font=('arial', 16, 'bold'), text="Product Code:", padx=1, pady=2, bg='#fff4c0')
        self.lblProdCode.grid(row=1, column=2, sticky=W)

        self.txtCostPerDay=Entry(LeftFrame0, textvariable=CostPerDay, font=('arial', 16, 'bold'), bd=8, fg="black", width=14, justify=RIGHT).grid(row=1, column=3)
        #=================================LeftFrame1==============================================
        self.lblCredLimit=Label(LeftFrame1, font=('arial', 16, 'bold'), text="Credit Limit:", padx=2, pady=2, bg='#fff4c0')
        self.lblCredLimit.grid(row=0, column=0, sticky=W)

        self.cboCredLimit = ttk.Combobox(LeftFrame1, textvariable=CredLimit, state='read only', font=('arial', 18, 'bold'), width=12)
        self.cboCredLimit['value'] = ('', 'Select an option', '$1,000', '$5,000', '$10,000', '$50,000')
        self.cboCredLimit.current(0)
        self.cboCredLimit.grid(row=0, column=1, pady=2)


        self.lblCreCheck=Label(LeftFrame1, font=('arial', 16, 'bold'), text="Credit Check:", padx=2, pady=2, bg='#fff4c0')
        self.lblCreCheck.grid(row=0, column=2, sticky=W)

        self.cboCreCheck = ttk.Combobox(LeftFrame1, textvariable=CreCheck, state='read only', font=('arial', 18, 'bold'), width=12)
        self.cboCreCheck['value'] = ('', 'Select an option', 'Yes', 'No')
        self.cboCreCheck.current(0)
        self.cboCreCheck.grid(row=0, column=3, pady=2)


        self.lblSettleDueDay=Label(LeftFrame1, font=('arial', 16, 'bold'), text="Settle Due Day", padx=1, pady=16, bg='#fff4c0')
        self.lblSettleDueDay.grid(row=1, column=0, sticky=W)

        self.txtSettleDueDay=Entry(LeftFrame1, textvariable=SettleDueDay, font=('arial', 16, 'bold'), bd=2, fg="black", width=14, justify=RIGHT).grid(row=1, column=1)


        self.lblPaymentD=Label(LeftFrame1, font=('arial', 16, 'bold'), text="Payment Due:", padx=1, pady=2, bg='#fff4c0')
        self.lblPaymentD.grid(row=1, column=2, sticky=W)

        self.cboPaymentD = ttk.Combobox(LeftFrame1, textvariable=PaymentD, state='readonly', font=('arial', 18, 'bold'), width=12)
        self.cboPaymentD['value'] = ('', 'Select an option', 'Yes', 'No')
        self.cboPaymentD.current(0)
        self.cboPaymentD.grid(row=1, column=3, pady=2)


        self.lblDiscount=Label(LeftFrame1, font=('arial', 16, 'bold'), text="Discount:", padx=1, pady=2, bg='#fff4c0')
        self.lblDiscount.grid(row=2, column=0, sticky=W)

        self.cboDiscount = ttk.Combobox(LeftFrame1, textvariable=Discount, state='readonly', font=('arial', 18, 'bold'), width=12)
        self.cboDiscount['value'] = ('', 'Select an option', '5%', '10%', '15,%', '20%')
        self.cboDiscount.current(0)
        self.cboDiscount.grid(row=2, column=1, pady=2)


        self.lblDeposit=Label(LeftFrame1, font=('arial', 16, 'bold'), text="Deposit:", padx=1, pady=2, bg='#fff4c0')
        self.lblDeposit.grid(row=2, column=2, sticky=W)

        self.cboDeposit = ttk.Combobox(LeftFrame1, textvariable=Deposit, state='readonly', font=('arial', 18, 'bold'), width=12)
        self.cboDeposit['value'] = ('', 'Select an option' , 'Yes' , 'No')
        self.cboDeposit.current(0)
        self.cboDeposit.grid(row=2, column=3, pady=2)


        self.lblPayDueDay=Label(LeftFrame1, font=('arial', 16, 'bold'), text="Pay Due Due:", padx=1, pady=2, bg='#fff4c0')
        self.lblPayDueDay.grid(row=3, column=0, sticky=W)

        self.txtPayDueDay=Entry(LeftFrame1, textvariable=PayDueDay, font=('arial', 16, 'bold'), bd=2, fg="black", width=14, justify=RIGHT).grid(row=3, column=1)


        self.lblPaymentM=Label(LeftFrame1, font=('arial', 16, 'bold'), text="Payment Method:", padx=0, pady=4, bg='#fff4c0')
        self.lblPaymentM.grid(row=3, column=2, sticky=W)

        self.cboPaymentM = ttk.Combobox(LeftFrame1, textvariable=PaymentM, state='readonly', font=('arial', 18, 'bold'), width=12)
        self.cboPaymentM['value'] = ('', 'Select an option', 'Cash', 'GCash', 'Visa', 'Bank')
        self.cboPaymentM.current(0)
        self.cboPaymentM.grid(row=3, column=3, pady=2)
        #=================================LeftFrame2==============================================
        LeftFrame2LL = Frame(LeftFrame2, bd=5, width = 300, height=160, padx=5, bg='powder blue', relief=RIDGE)
        LeftFrame2LL.grid(row=0, column=0)
        LeftFrame2LR = Frame(LeftFrame2, bd=5, width = 300, height=160,  bg='cadet blue', relief=RIDGE)
        LeftFrame2LR.grid(row=0, column=1)

        self.chkCheckCredit = Checkbutton(LeftFrame2LL, text="Check Credit", variable=var1, onvalue=1, offvalue=0, font=('arial',16,'bold'), bg='powder blue', command=CheckCredit).grid(row=0, sticky=W)
        self.chkTermAgreed = Checkbutton(LeftFrame2LL, text="Term Agreed", variable=var2, onvalue=1, offvalue=0, font=('arial',16,'bold'), bg='powder blue', command=TermAgreed).grid(row=1, sticky=W)
        self.chkAccountOnHold = Checkbutton(LeftFrame2LL, text="Account On Hold", variable=var3, onvalue=1, offvalue=0, font=('arial',16,'bold'), bg='powder blue', command=AccountOnHold).grid(row=2, sticky=W)
        self.chkRestrictMailing = Checkbutton(LeftFrame2LL, text="Restrict Mailing", variable=var4, onvalue=1, offvalue=0, font=('arial',16,'bold'), bg='powder blue', command=RestrictMailing).grid(row=3, sticky=W)

        self.txtInfo = Text(LeftFrame2LR, height=9, width=63, bg='cadet blue', font=('arial',9,'bold'))
        self.txtInfo.grid(row=0, column=0, pady=2)
        #=================================LeftFrame3==============================================
        self.lblTax=Label(LeftFrame3, font=('arial', 18, 'bold'), text="Tax:", padx=14, pady=4, bg='#fff4c0')
        self.lblTax.grid(row=0, column=0, sticky=W)
        self.txtTax=Entry(LeftFrame3, textvariable=Tax, font=('arial', 16, 'bold'), bd=8, fg="black", width=14, justify=LEFT).grid(row=1, column=0, padx=23, pady=5)


        self.lblSubTotal=Label(LeftFrame3, font=('arial', 18, 'bold'), text="SubTotal:", padx=14, pady=4, bg='#fff4c0')
        self.lblSubTotal.grid(row=0, column=1, sticky=W)
        self.txtSubTotal=Entry(LeftFrame3, textvariable=SubTotal, font=('arial', 16, 'bold'), bd=8, fg="black", width=14, justify=LEFT).grid(row=1, column=1, padx=23, pady=5)


        self.lblTotal=Label(LeftFrame3, font=('arial', 18, 'bold'), text="Total:", padx=14, pady=4, bg='#fff4c0')
        self.lblTotal.grid(row=0, column=2, sticky=W)
        self.txtTotal=Entry(LeftFrame3, textvariable=Total, font=('arial', 16, 'bold'), bd=8, fg="black", width=14, justify=LEFT).grid(row=1, column=2, padx=23, pady=5)
        #=================================RightFrame0==============================================

        self.lblAcctOpen=Label(RightFrame0, font=('arial', 18, 'bold'), text="Account Opened:", padx=2, pady=2, bg='#c0cbff')
        self.lblAcctOpen.grid(row=0, column=0, sticky=W)

        self.cboAcctOpen = ttk.Combobox(RightFrame0, textvariable=AcctOpen, state='read only', font=('arial', 18, 'bold'), width=16)
        self.cboAcctOpen['value'] = ('', 'Select an option', 'Yes', 'No')
        self.cboAcctOpen.current(0)
        self.cboAcctOpen.grid(row=0, column=1, pady=2)

        self.lblAppDate=Label(RightFrame0, font=('arial', 18, 'bold'), text="Application Date:", padx=2, pady=2, bg='#c0cbff')
        self.lblAppDate.grid(row=1, column=0, sticky=W)

        self.cboAppDate = ttk.Combobox(RightFrame0, textvariable=AppDate, state='read only', font=('arial', 18, 'bold'), width=16)
        self.cboAppDate['value'] = ('', 'Select an option', 'Yes', 'No')
        self.cboAppDate.current(0)
        self.cboAppDate.grid(row=1, column=1, pady=2)

        self.lblNCreR=Label(RightFrame0, font=('arial', 18, 'bold'), text="Next Credit Review:", padx=2, pady=2, bg='#c0cbff')
        self.lblNCreR.grid(row=2, column=0, sticky=W)

        self.cboNCreR = ttk.Combobox(RightFrame0, textvariable=NCreR, state='read only', font=('arial', 18, 'bold'), width=16)
        self.cboNCreR['value'] = ('', 'Select an option', 'Yes', 'No')
        self.cboNCreR.current(0)
        self.cboNCreR.grid(row=2, column=1, pady=2)

        self.lblLCreR=Label(RightFrame0, font=('arial', 18, 'bold'), text="Last Credit Review:", padx=2, pady=2, bg='#c0cbff')
        self.lblLCreR.grid(row=3, column=0, sticky=W)

        self.cboLCreR = ttk.Combobox(RightFrame0, textvariable=LCreR, state='read only', font=('arial', 18, 'bold'), width=16)
        self.cboLCreR['value'] = ('', 'Select an option', 'Yes', 'No')
        self.cboLCreR.current(0)
        self.cboLCreR.grid(row=3, column=1, pady=2)

        self.lblDateRev=Label(RightFrame0, font=('arial', 18, 'bold'), text="Date Review:", padx=2, pady=2, bg='#c0cbff')
        self.lblDateRev.grid(row=4, column=0, sticky=W)

        self.cboDateRev = ttk.Combobox(RightFrame0, textvariable=DateRev, state='read only', font=('arial', 18, 'bold'), width=16)
        self.cboDateRev['value'] = ('', 'Select an option', 'Yes', 'No')
        self.cboDateRev.current(0)
        self.cboDateRev.grid(row=4, column=1, pady=2)

        #=================================Text, Labels, Entry Widget============================

        self.txtReceipt = Text(RightFrame1, pady=2, height=19, width=71, font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0, column=0, pady=2)

        #=================================Buttons============================

        self.btnTotal = Button(RightFrame2, padx=18, pady=2, bd=4, fg="black", font=('arial',9,'bold'), width=9, bg='#c0cbff', text="Total", command=TotalCost).grid(row=0, column=0)
        self.btnReset = Button(RightFrame2, padx=18, pady=2, bd=4, fg="black", font=('arial',9,'bold'), width=9, bg='#c0cbff', text="Reset", command=Reset).grid(row=0, column=1)
        self.btnExit = Button(RightFrame2, padx=18, pady=2, bd=4, fg="black", font=('arial',9,'bold'), width=9, bg='#c0cbff', text="Exit", command=iExit).grid(row=0, column=2)

if __name__=='__main__':
    root = Tk()
    application = Inventory(root)
    root.mainloop()