from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import  QWidget, QMenu, QProgressDialog, QVBoxLayout, QHBoxLayout, QAbstractItemView, QTableWidgetItem, QLabel, QApplication
from datetime import date, datetime, timedelta
from decimal import Decimal
from logging import info, debug
from xulpymoney.datetime_functions import dtaware_day_end_from_date, date_last_of_the_month, date_first_of_the_next_x_months
from xulpymoney.objects.dividend import DividendHeterogeneusManager
from xulpymoney.objects.investmentoperation import InvestmentOperationHistoricalHeterogeneusManager
from xulpymoney.libxulpymoneyfunctions import  qmessagebox
from xulpymoney.casts import list2string, none2decimal0, lor_transposed
from xulpymoney.ui.myqtablewidget import qcenter, qleft, mqtwObjects
from xulpymoney.libxulpymoneytypes import eQColor, eMoneyCurrency
from xulpymoney.objects.annualtarget import AnnualTarget
from xulpymoney.objects.assets import Assets
from xulpymoney.objects.accountoperation import AccountOperationManagerHeterogeneus
from xulpymoney.objects.money import Money
from xulpymoney.objects.percentage import Percentage
from xulpymoney.ui.Ui_wdgTotal import Ui_wdgTotal

class TotalMonth:
    """All values are calculated in last day of the month"""
    def __init__(self, mem, year, month):
        self.mem=mem
        self.year=year
        self.month=month
        self.expenses_value=None
        self.no_loses_value=None
        self.dividends_value=None
        self.incomes_value=None
        self.funds_revaluation_value=None
        self.gains_value=None
        self.total_accounts_value=None
        self.total_investments_value=None
        self.total_investments_high_low_value=None
        self.total_zerorisk_value=None
        self.total_bonds_value=None

    def i_d_g_e(self):
        return self.incomes()+self.dividends()+self.gains()+self.expenses()

    def d_g(self):
        """Dividends+gains"""
        return self.gains()+self.dividends()

    def expenses(self):
        if self.expenses_value==None:
            self.expenses_value=Assets(self.mem).saldo_por_tipo_operacion( self.year,self.month, 1)#La facturación de tarjeta dentro esta por el union
        return self.expenses_value

    def dividends(self):
        if self.dividends_value==None:
            self.dividends_value=Assets(self.mem).dividends_neto(  self.year, self.month)
        return self.dividends_value

    def incomes(self):
        if self.incomes_value==None:
            self.incomes_value=Assets(self.mem).saldo_por_tipo_operacion(  self.year,self.month,2)-self.dividends()
        return self.incomes_value

    def gains(self):
        if self.gains_value==None:
            self.gains_value=Assets(self.mem).consolidado_neto(self.mem.data.investments, self.year, self.month)
        return self.gains_value

    def funds_revaluation(self):
        if self.funds_revaluation_value==None:
            self.funds_revaluation_value=self.mem.data.investments_active().revaluation_monthly(2, self.year, self.month)#2 if type funds
        return self.funds_revaluation_value

    def name(self):
        return "{}-{}".format(self.year, self.month)

    def last_day(self):
        return date_last_of_the_month(self.year, self.month)

    def first_day(self):
        return date(self.year, self.month, self.day)

    def total(self):
        """Total assests in the month"""
        return self.total_accounts()+self.total_investments()

    def total_accounts(self):
        if self.total_accounts_value==None:
            self.total_accounts_value=Assets(self.mem).saldo_todas_cuentas( self.last_day())
        return self.total_accounts_value

    def total_investments(self):
        if self.total_investments_value==None:
            self.total_investments_value=Assets(self.mem).saldo_todas_inversiones(self.last_day())
        return self.total_investments_value

    def total_investments_high_low(self):
        if self.total_investments_high_low_value==None:
            self.total_investments_high_low_value=Assets(self.mem).saldo_todas_inversiones_high_low(self.last_day())
        return self.total_investments_high_low_value


    def total_zerorisk(self): 
        if self.total_zerorisk_value==None:
            self.total_zerorisk_value=Assets(self.mem).patrimonio_riesgo_cero(self.last_day())
        return self.total_zerorisk_value

    def total_bonds(self):
        if self.total_bonds_value==None:
            self.total_bonds_value=Assets(self.mem).saldo_todas_inversiones_bonds(self.last_day())
        return self.total_bonds_value

    def total_no_losses(self):
        if self.no_loses_value==None:
            self.no_loses_value=Assets(self.mem).invested(self.last_day())+self.total_accounts()
        return self.no_loses_value

## Set of 12 totalmonths in the same year
class TotalYear:
    def __init__(self, mem, year):
        self.mem=mem
        self.year=year
        self.arr=[]
        self.total_last_year=Assets(self.mem).saldo_total(self.mem.data.investments,  date(self.year-1, 12, 31))
        self.generate()

    def generate(self):
        for i in range(1, 13):
            self.arr.append(TotalMonth(self.mem, self.year, i))

    def find(self, year, month):
        for m in self.arr:
            if m.year==year and m.month==month:
                return m
        return None

    def expenses(self):
        result=Money(self.mem, 0, self.mem.localcurrency)
        for m in self.arr:
            result=result+m.expenses()
        return result

    def i_d_g_e(self):
        return self.incomes()+self.dividends()+self.gains()+self.expenses()

    def funds_revaluation(self):
        return self.mem.data.investments_active().revaluation_annual(2, self.year)#2 if type funds

    def incomes(self):
        result=Money(self.mem, 0, self.mem.localcurrency)
        for m in self.arr:
            result=result+m.incomes()
        return result

    def gains(self):
        result=Money(self.mem, 0, self.mem.localcurrency)
        for m in self.arr:
            result=result+m.gains()
        return result        

    def dividends(self):
        result=Money(self.mem, 0, self.mem.localcurrency)
        for m in self.arr:
            result=result+m.dividends()
        return result

    def d_g(self):
        """Dividends+gains"""
        return self.gains()+self.dividends()

    def difference_with_previous_month(self, totalmonth):
        """Calculates difference between totalmonth and the total with previous month"""
        if totalmonth.month==1:
            totalprevious=self.total_last_year
        else:
            previous=self.find(self.year, totalmonth.month-1)
            totalprevious=previous.total()
        return totalmonth.total()-totalprevious

    def difference_with_previous_year(self):
        """Calculates difference between totalmonth of december and the total last year"""
        return self.find(self.year, 12).total()-self.total_last_year

    def assets_percentage_in_month(self, month):
        """Calculates the percentage of the assets in this month from total last year"""
        m=self.find(self.year, month)
        return Percentage(m.total()-self.total_last_year, self.total_last_year)

class TotalGraphic:
    """Set of totalmonths to generate a graphic"""
    def __init__(self, mem, startyear, startmonth):
        self.mem=mem
        self.startyear=startyear
        self.startmonth=startmonth
        self.arr=[]
        self.generate()

    def generate(self):
        dt=date(self.startyear, self.startmonth, 1)-timedelta(days=1)#Previous month last day
        while date.today()>=dt:
            self.arr.append(TotalMonth(self.mem, dt.year, dt.month))
            dt=date_first_of_the_next_x_months(dt.year, dt.month, 1)#Next month first day

    def find(self, year, month):
        for m in self.arr:
            if m.year==year and m.month==month:
                return m
        return None

    def length(self):
        return len(self.arr)

class wdgTotal(QWidget, Ui_wdgTotal):
    def __init__(self, mem,  parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.mem=mem   

        dtFirst=Assets(self.mem).first_datetime_allowed_estimated()  
        dtLast=Assets(self.mem).last_datetime_allowed_estimated()              

        self.setData=None#Será un TotalYear
        self.setGraphic=None #Será un TotalGraphic
        
        self.mqtw.setSettings(self.mem.settings, "wdgTotal", "mqtw")
        self.mqtw.table.cellDoubleClicked.connect(self.on_mqtw_cellDoubleClicked)
        self.mqtw.table.customContextMenuRequested.connect(self.on_mqtw_customContextMenuRequested)
        self.mqtw.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.mqtw.table.itemSelectionChanged.connect(self.on_mqtw_itemSelectionChanged)
        self.mqtwTargets.setSettings(self.mem.settings, "wdgTotal", "mqtwTargets")
        self.mqtwTargetsPlus.setSettings(self.mem.settings, "wdgTotal", "mqtwTargetsPlus")
        self.mqtwInvestOrWork.setSettings(self.mem.settings,  "wdgTotal", "mqtwInvestOrWork")
        self.mqtwMakeEndsMeet.setSettings(self.mem.settings, "wdgTotal", "mqtwMakeEndsMeet")
        
        self.annualtarget=None#AnnualTarget Object
        
        self.wyData.initiate(dtFirst.year,  dtLast.year, date.today().year)
        self.wyChart.initiate(dtFirst.year,  dtLast.year, date.today().year-3)
        self.wyChart.label.setText(self.tr("Data from selected year"))

        self.wdgTS.setSettings(self.mem.settings, "wdgTotal", "wdgTS")

        self.tab.setCurrentIndex(0)
        self.tabData.setCurrentIndex(0)
        self.tabPlus.setCurrentIndex(0)
        
        self.pd= QProgressDialog("Loading data", None, 0,13    )
        self.pd.setWindowIcon(QIcon(":/xulpymoney/coins.png"))
        self.pd.setModal(True)
        self.pd.setWindowTitle(QApplication.translate("Mem","Generating total report..."))
        self.pd.forceShow()
        self.progress_bar_update()

        self.load_data()
        self.load_targets()
        self.load_targets_with_funds_revaluation()
        self.load_invest_or_work()
        self.load_make_ends_meet()
        self.progress_bar_update()
        self.wyData.changed.connect(self.on_wyData_mychanged)#Used my due to it took default on_wyData_changed
        self.wyChart.changed.connect(self.on_wyChart_mychanged)

    ## One step forward
    def progress_bar_update(self):
        self.pd.setValue(self.pd.value()+1)
        self.pd.update()
        QApplication.processEvents()

        

    def load_data(self):
        inicio=datetime.now()
        self.setData=TotalYear(self.mem, self.wyData.year)
        
        hh=[self.tr("January"),  self.tr("February"), self.tr("March"), self.tr("April"), self.tr("May"), self.tr("June"), self.tr("July"), self.tr("August"), self.tr("September"), self.tr("October"), self.tr("November"), self.tr("December"), self.tr("Total")]
        hv=[self.tr("Incomes"), self.tr("Gains"), self.tr("Dividends"), self.tr("Expenses"), self.tr("I+G+D+E"), "", self.tr("Accounts"), self.tr("Investments"), self.tr("Total"), self.tr("Monthly difference"), "", self.tr("% Year to date")]
        data=[]
        for i, m in enumerate(self.setData.arr):
            if m.year<date.today().year or (m.year==date.today().year and m.month<=date.today().month):
                row=[]
                row.append(m.incomes())
                row.append(m.gains())
                row.append(m.dividends())
                row.append(m.expenses())
                row.append(m.i_d_g_e())
                row.append("")
                row.append(m.total_accounts())
                row.append(m.total_investments())
                row.append(m.total())
                row.append(self.setData.difference_with_previous_month(m))
                row.append("")
                row.append(self.setData.assets_percentage_in_month(m.month))        
            else:
                row=[""]*12
            data.append(row)
            self.progress_bar_update()
        row=[]
        row.append(self.setData.incomes())
        row.append(self.setData.gains())
        row.append(self.setData.dividends())
        row.append(self.setData.expenses())
        row.append(self.setData.i_d_g_e())
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append(self.setData.difference_with_previous_year())
        row.append("")
        row.append(self.setData.assets_percentage_in_month(12))        
        data.append(row)
        data=lor_transposed(data)
        self.mqtw.setData(hh, hv, data)
        
        self.mqtw.table.setCurrentCell(6, date.today().month-1)
        self.lblPreviousYear.setText(self.tr("Balance at {0}-12-31: {1}".format(self.setData.year-1, self.setData.total_last_year)))


        invested=Assets(self.mem).invested(date.today())
        current=Assets(self.mem).saldo_todas_inversiones( date.today())
        s=self.tr("This year I've generated {}.").format(self.setData.gains()+self.setData.dividends())
        s=s+"\n"+self.tr("Difference between invested amount and current invesment balance: {} - {} = {}").format(invested,  current,  current-invested)
        self.lblInvested.setText(s)

        info("wdgTotal > load_data: {0}".format(datetime.now()-inicio))

    def load_targets(self):
        self.annualtarget=AnnualTarget(self.mem).init__from_db(self.wyData.year) 
        self.lblTarget.setText(self.tr("Annual target percentage of total assests balance at {}-12-31 ( {} )".format(self.annualtarget.year-1, self.annualtarget.lastyear_assests)))
        self.spinTarget.setValue(float(self.annualtarget.percentage))
        self.mqtwTargets.table.setColumnCount(13)
        self.mqtwTargets.table.setRowCount(5)
        for i, s in enumerate([self.tr("January"),  self.tr("February"), self.tr("March"), self.tr("April"), self.tr("May"), self.tr("June"), self.tr("July"), self.tr("August"), self.tr("September"), self.tr("October"), self.tr("November"), self.tr("December"), self.tr("Total")]):
            self.mqtwTargets.table.setHorizontalHeaderItem(i, QTableWidgetItem(s))
        for i, s in enumerate([self.tr("Monthly target"), self.tr("Total gains"), "", self.tr("Accumulated target"), self.tr("Accumulated total gains")]):
            self.mqtwTargets.table.setVerticalHeaderItem(i, QTableWidgetItem(s))
        self.mqtwTargets.table.verticalHeader().show()        
        self.mqtwTargets.table.clearContents()
        self.mqtwTargets.applySettings()
        inicio=datetime.now()     
        sumd_g=Money(self.mem, 0, self.mem.localcurrency)
        for i in range(1, 13): 
            m=self.setData.find(self.setData.year, i)
            sumd_g=sumd_g+m.d_g()
            self.mqtwTargets.table.setItem(0, i-1, self.mem.localmoney(self.annualtarget.monthly_balance()).qtablewidgetitem())
            self.mqtwTargets.table.setItem(1, i-1, self.mem.localmoney(m.d_g().amount).qtablewidgetitem_with_target(self.annualtarget.monthly_balance()))
            self.mqtwTargets.table.setItem(3, i-1, self.mem.localmoney(self.annualtarget.monthly_balance()*i).qtablewidgetitem())
            self.mqtwTargets.table.setItem(4, i-1, self.mem.localmoney(sumd_g.amount).qtablewidgetitem_with_target(self.annualtarget.monthly_balance()*i))
        self.mqtwTargets.table.setItem(0, 12, self.mem.localmoney(self.annualtarget.annual_balance()).qtablewidgetitem())
        self.mqtwTargets.table.setItem(1, 12, self.mem.localmoney(sumd_g.amount).qtablewidgetitem_with_target(self.annualtarget.annual_balance()))
        self.mqtwTargets.table.setCurrentCell(2, date.today().month-1)   
                
        s=""
        s=s+self.tr("This report shows if the user reaches the annual and monthly target.") +"\n\n"
        s=s+self.tr("Total gains are the result of adding dividends to gains")+"\n\n"
        s=s+self.tr("The cumulative target row shows compliance of the target in the year.")+"\n\n"
        s=s+self.tr("Green color shows that target has been reached.")
        self.lblTargets.setText(s)
        
        info("wdgTargets > load_data_targets: {0}".format(datetime.now()  -inicio))
        
    def load_targets_with_funds_revaluation(self):        
        self.mqtwTargetsPlus.table.setColumnCount(13)
        self.mqtwTargetsPlus.table.setRowCount(7)
        for i, s in enumerate([self.tr("January"),  self.tr("February"), self.tr("March"), self.tr("April"), self.tr("May"), self.tr("June"), self.tr("July"), self.tr("August"), self.tr("September"), self.tr("October"), self.tr("November"), self.tr("December"), self.tr("Total")]):
            self.mqtwTargetsPlus.table.setHorizontalHeaderItem(i, QTableWidgetItem(s))
        for i, s in enumerate([self.tr("Monthly target"), self.tr("Total gains"), self.tr("Funds revaluation"), self.tr("Total"), "",  self.tr("Accumulated target"), self.tr("Accumulated total gains")]):
            self.mqtwTargetsPlus.table.setVerticalHeaderItem(i, QTableWidgetItem(s))
        self.mqtwTargetsPlus.table.verticalHeader().show()       
        self.mqtwTargetsPlus.table.clearContents()
        self.mqtwTargetsPlus.applySettings()
        inicio=datetime.now()     

        sumd_g=Money(self.mem, 0, self.mem.localcurrency)
        sumf=Money(self.mem, 0, self.mem.localcurrency)
        for i in range(1, 13): 
            m=self.setData.find(self.setData.year, i)
            sumd_g=sumd_g+m.d_g()
            sumf=sumf+m.funds_revaluation()
            self.mqtwTargetsPlus.table.setItem(0, i-1, self.mem.localmoney(self.annualtarget.monthly_balance()).qtablewidgetitem())
            self.mqtwTargetsPlus.table.setItem(1, i-1,m.d_g().qtablewidgetitem())
            self.mqtwTargetsPlus.table.setItem(2, i-1, m.funds_revaluation().qtablewidgetitem())
            self.mqtwTargetsPlus.table.setItem(3, i-1, self.mem.localmoney(m.d_g().amount+m.funds_revaluation().amount).qtablewidgetitem_with_target(self.annualtarget.monthly_balance()))
            
            self.mqtwTargetsPlus.table.setItem(5, i-1, self.mem.localmoney(self.annualtarget.monthly_balance()*i).qtablewidgetitem())
            self.mqtwTargetsPlus.table.setItem(6, i-1, self.mem.localmoney(sumd_g.amount+sumf.amount).qtablewidgetitem_with_target(self.annualtarget.monthly_balance()*i))
        self.mqtwTargetsPlus.table.setItem(0, 12, self.mem.localmoney(self.annualtarget.annual_balance()).qtablewidgetitem())
        self.mqtwTargetsPlus.table.setItem(1, 12, sumd_g.qtablewidgetitem())
        self.mqtwTargetsPlus.table.setItem(2, 12, sumf.qtablewidgetitem())
        self.mqtwTargetsPlus.table.setItem(3, 12, self.mem.localmoney(sumd_g.amount+sumf.amount).qtablewidgetitem_with_target(self.annualtarget.annual_balance()))
        self.mqtwTargetsPlus.table.setCurrentCell(2, date.today().month-1)   
                
        s=""
        s=s+self.tr("This report shows if the user reaches the annual and monthly target.") +"\n\n"
        s=s+self.tr("Total is the result of adding dividends to gain and funds revaluation")+"\n\n"
        s=s+self.tr("The cumulative target row shows compliance of the target in the year.")+"\n\n"
        s=s+self.tr("Green color shows that target has been reached.")
        self.lblTargetsPlus.setText(s)
        
        info("wdgTargets > load_data_targets_with_funds_revaluation: {0}".format(datetime.now()  -inicio))

    def load_invest_or_work(self):
        def qresult(dg_e):
            """Returns a qtablewidgetitem with work or invest
            dg_e=dividends+gains-expenses
            dg_i=dividends+gains-incomes
            """
            item=qcenter("")
            if dg_e.isZero():
                return item
            if not dg_e.isGETZero():
                item.setText(self.tr("Work"))
                item.setBackground(eQColor.Red)
            else:
                item.setText(self.tr("Invest"))
                item.setBackground(eQColor.Green)
            return item            
        ##------------------------------------------------
        inicio=datetime.now()            
        self.mqtwInvestOrWork.table.setColumnCount(13)
        self.mqtwInvestOrWork.table.setRowCount(6)
        for i, s in enumerate([self.tr("January"),  self.tr("February"), self.tr("March"), self.tr("April"), self.tr("May"), self.tr("June"), self.tr("July"), self.tr("August"), self.tr("September"), self.tr("October"), self.tr("November"), self.tr("December"), self.tr("Total")]):
            self.mqtwInvestOrWork.table.setHorizontalHeaderItem(i, QTableWidgetItem(s))
        for i, s in enumerate([self.tr("Total gains"), self.tr("Expenses"), "",  self.tr("Total gains - Expenses"), "",  self.tr("Result")]):
            self.mqtwInvestOrWork.table.setVerticalHeaderItem(i, QTableWidgetItem(s))
        self.mqtwInvestOrWork.table.verticalHeader().show()       
        self.mqtwInvestOrWork.table.clearContents()
        self.mqtwInvestOrWork.applySettings()
        for i in range(1, 13): 
            m=self.setData.find(self.setData.year, i)
            self.mqtwInvestOrWork.table.setItem(0, i-1, m.d_g().qtablewidgetitem())
            self.mqtwInvestOrWork.table.setItem(1, i-1, m.expenses().qtablewidgetitem())
            self.mqtwInvestOrWork.table.setItem(3, i-1, (m.d_g()+m.expenses()).qtablewidgetitem())#Es mas porque es - y gastos -
            self.mqtwInvestOrWork.table.setItem(5, i-1, qresult(m.d_g()+m.expenses()))
        self.mqtwInvestOrWork.table.setItem(0, 12, self.setData.d_g().qtablewidgetitem())
        self.mqtwInvestOrWork.table.setItem(1, 12, self.setData.expenses().qtablewidgetitem())
        self.mqtwInvestOrWork.table.setItem(3, 12, (self.setData.d_g()+self.setData.expenses()).qtablewidgetitem())
        self.mqtwInvestOrWork.table.setItem(5, 12, qresult(self.setData.d_g()+self.setData.expenses()))
        self.mqtwInvestOrWork.table.setCurrentCell(2, date.today().month-1)   
        
        s=""
        s=s+self.tr("This report shows if the user could retire due to its investments") +"\n\n"
        s=s+self.tr("Total gains are the result of adding dividends to gains")+"\n\n"
        s=s+self.tr("Difference between total gains and expenses shows if user could cover his expenses with his total gains")+"\n\n"
        s=s+self.tr("Investment taxes are not evaluated in this report")
        self.lblInvestOrWork.setText(s)
        info ("wdgTotal > load invest or work: {0}".format(datetime.now()  -inicio))

    def load_make_ends_meet(self):
        def qresult(res):
            """Returns a qtablewidgetitem with yes or no
            """
            item=qcenter("")
            if res.isZero():
                return item
            if not res.isGETZero():
                item.setText(self.tr("No"))
                item.setBackground(eQColor.Red)
            else:
                item.setText(self.tr("Yes"))
                item.setBackground(eQColor.Green)
            return item            
        ##------------------------------------------------
        inicio=datetime.now()    
        self.mqtwMakeEndsMeet.table.setColumnCount(13)
        self.mqtwMakeEndsMeet.table.setRowCount(6)
        for i, s in enumerate([self.tr("January"),  self.tr("February"), self.tr("March"), self.tr("April"), self.tr("May"), self.tr("June"), self.tr("July"), self.tr("August"), self.tr("September"), self.tr("October"), self.tr("November"), self.tr("December"), self.tr("Total")]):
            self.mqtwMakeEndsMeet.table.setHorizontalHeaderItem(i, QTableWidgetItem(s))
        for i, s in enumerate([self.tr("Incomes"), self.tr("Expenses"), "",  self.tr("Incomes - Expenses"), "",  self.tr("Result")]):
            self.mqtwMakeEndsMeet.table.setVerticalHeaderItem(i, QTableWidgetItem(s))
        self.mqtwMakeEndsMeet.table.verticalHeader().show()      
        self.mqtwMakeEndsMeet.table.clearContents()
        self.mqtwMakeEndsMeet.applySettings()
        for i in range(1, 13): 
            m=self.setData.find(self.setData.year, i)
            self.mqtwMakeEndsMeet.table.setItem(0, i-1, m.incomes().qtablewidgetitem())
            self.mqtwMakeEndsMeet.table.setItem(1, i-1, m.expenses().qtablewidgetitem())
            self.mqtwMakeEndsMeet.table.setItem(3, i-1, (m.incomes()+m.expenses()).qtablewidgetitem())#Es mas porque es - y gastos -
            self.mqtwMakeEndsMeet.table.setItem(5, i-1, qresult(m.incomes()+m.expenses()))
        self.mqtwMakeEndsMeet.table.setItem(0, 12, self.setData.incomes().qtablewidgetitem())
        self.mqtwMakeEndsMeet.table.setItem(1, 12, self.setData.expenses().qtablewidgetitem())
        self.mqtwMakeEndsMeet.table.setItem(3, 12, (self.setData.incomes()+self.setData.expenses()).qtablewidgetitem())
        self.mqtwMakeEndsMeet.table.setItem(5, 12, qresult(self.setData.incomes()+self.setData.expenses()))
        self.mqtwMakeEndsMeet.table.setCurrentCell(2, date.today().month-1)   
        
        s=""
        s=s+self.tr("This report shows if the user makes ends meet") +"\n\n"
        s=s+self.tr("Difference between incomes and expenses shows if user could cover his expenses with his incomes")
        self.lblMakeEndsMeet.setText(s)
        info("wdgTotal > load_make_ends_meet: {0}".format(datetime.now()  -inicio))


    def load_graphic(self, animations=True):               
        inicio=datetime.now()  
        
        self.setGraphic=TotalGraphic(self.mem, self.wyChart.year, 1)

        self.wdgTS.clear()
        self.wdgTS.ts.setAnimations(animations)
        
        #Series creation
        last=self.setGraphic.find(date.today().year, date.today().month)
        lsNoLoses=self.wdgTS.ts.appendTemporalSeries(self.tr("Total without losses assets")+": {}".format(last.total_no_losses()))
        lsMain=self.wdgTS.ts.appendTemporalSeries(self.tr("Total assets")+": {}".format(last.total()))
        lsZero=self.wdgTS.ts.appendTemporalSeries(self.tr("Zero risk assets")+": {}".format(last.total_zerorisk()))
        lsBonds=self.wdgTS.ts.appendTemporalSeries(self.tr("Bond assets")+": {}".format(last.total_bonds()))
        lsRisk=self.wdgTS.ts.appendTemporalSeries(self.tr("Risk assets")+": {}".format(last.total()-last.total_zerorisk()-last.total_bonds()))

        progress = QProgressDialog(self.tr("Filling report data"), self.tr("Cancel"), 0,self.setGraphic.length())
        progress.setModal(True)
        progress.setWindowTitle(self.tr("Calculating data..."))
        progress.setWindowIcon(QIcon(":/xulpymoney/coins.png"))
        for m in self.setGraphic.arr:
            if progress.wasCanceled():
                break
            progress.setValue(progress.value()+1)
            epoch=dtaware_day_end_from_date(m.last_day(), self.mem.localzone_name)
            total=m.total().amount
            zero=m.total_zerorisk().amount
            bonds=m.total_bonds().amount
            self.wdgTS.ts.appendTemporalSeriesData(lsMain, epoch, m.total().amount)
            self.wdgTS.ts.appendTemporalSeriesData(lsZero, epoch, m.total_zerorisk().amount)
            self.wdgTS.ts.appendTemporalSeriesData(lsBonds, epoch, m.total_bonds().amount)
            self.wdgTS.ts.appendTemporalSeriesData(lsRisk, epoch, total-zero-bonds)
            self.wdgTS.ts.appendTemporalSeriesData(lsNoLoses, epoch, m.total_no_losses().amount)
        self.wdgTS.display()
        
        info("wdgTotal > load_graphic: {0}".format(datetime.now()-inicio))

    def on_wyData_mychanged(self):
        self.load_data()    
        self.load_targets()
        self.load_targets_with_funds_revaluation()
        self.load_invest_or_work()
        self.load_make_ends_meet()

    def on_wyChart_mychanged(self):
        self.load_graphic()      
        
    def on_cmdTargets_released(self):
        self.annualtarget.percentage=self.spinTarget.value()
        self.annualtarget.save()
        self.mem.con.commit()
        self.load_targets()
        self.load_targets_with_funds_revaluation()

    def on_tab_currentChanged(self, index):
        if  index==1 and self.wdgTS.isEmpty(): #If has not been plotted, plots it.
            self.on_wyChart_mychanged()
        
    @pyqtSlot() 
    def on_actionShowIncomes_triggered(self):
        newtab = QWidget()
        horizontalLayout = QHBoxLayout(newtab)
        wdg = mqtwObjects(newtab)
        wdg.setSettings(self.mem.settings, "wdgTotal","mqtwShowIncomes")
        wdg.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        
        id_tiposoperaciones=2
        set=AccountOperationManagerHeterogeneus(self.mem)
        if self.month==13:#Year
            tabtitle=self.tr("Incomes of {}").format(self.wyData.year)
            set.load_from_db("""select id_opercuentas, datetime, id_conceptos, id_tiposoperaciones, importe, comentario, id_cuentas 
                                                    from opercuentas 
                                                    where id_tiposoperaciones={0} and 
                                                        date_part('year',datetime)={1} and
                                                        id_conceptos not in ({2}) 
                                                union all select id_opercuentas, datetime, id_conceptos, id_tiposoperaciones, importe, comentario, id_cuentas 
                                                    from opertarjetas,tarjetas 
                                                    where opertarjetas.id_tarjetas=tarjetas.id_tarjetas and 
                                                        id_tiposoperaciones={0} and 
                                                        date_part('year',datetime)={1}""".format (id_tiposoperaciones, self.wyData.year, list2string(self.mem.conceptos.considered_dividends_in_totals())))
        else:#Month
            tabtitle=self.tr("Incomes of {0} of {1}").format(self.mqtw.table.horizontalHeaderItem(self.month-1).text(), self.wyData.year)
            set.load_from_db("""select id_opercuentas, datetime, id_conceptos, id_tiposoperaciones, importe, comentario, id_cuentas 
                                                    from opercuentas 
                                                    where id_tiposoperaciones={0} and 
                                                        date_part('year',datetime)={1} and 
                                                        date_part('month',datetime)={2} and 
                                                        id_conceptos not in ({3}) 
                                                union all select id_opercuentas, datetime, id_conceptos, id_tiposoperaciones, importe, comentario, id_cuentas 
                                                    from opertarjetas,tarjetas 
                                                    where opertarjetas.id_tarjetas=tarjetas.id_tarjetas and 
                                                        id_tiposoperaciones={0} and 
                                                        date_part('year',datetime)={1} and 
                                                        date_part('month',datetime)={2}""".format (id_tiposoperaciones, self.wyData.year, self.month, list2string(self.mem.conceptos.considered_dividends_in_totals())))
        set.myqtablewidget(wdg,  True)
        wdg.drawOrderBy(0, False)
        horizontalLayout.addWidget(wdg)
        self.tab.addTab(newtab, tabtitle)
        self.tab.setCurrentWidget(newtab)            

       
    @pyqtSlot() 
    def on_actionShowExpenses_triggered(self):     
        newtab = QWidget()
        horizontalLayout = QHBoxLayout(newtab)
        wdg = mqtwObjects(newtab)
        wdg.setSettings(self.mem.settings, "wdgTotal","mqtwShowExpenses")
        wdg.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        
        id_tiposoperaciones=1
        set=AccountOperationManagerHeterogeneus(self.mem)
        if self.month==13:#Year
            tabtitle=self.tr("Expenses of {0}").format(self.wyData.year)
            set.load_from_db("""select id_opercuentas, datetime, id_conceptos, id_tiposoperaciones, importe, comentario, id_cuentas , -1 as id_tarjetas 
                                                from opercuentas 
                                                where id_tiposoperaciones={0} and 
                                                           date_part('year',datetime)={1} 
                                                union all 
                                                select id_opercuentas, datetime, id_conceptos, id_tiposoperaciones, importe, comentario, id_cuentas ,tarjetas.id_tarjetas as id_tarjetas 
                                                from opertarjetas,tarjetas 
                                                where opertarjetas.id_tarjetas=tarjetas.id_tarjetas and 
                                                            id_tiposoperaciones={0} and 
                                                            date_part('year',datetime)={1}
                                                order by datetime""".format (id_tiposoperaciones, self.wyData.year))
        else:#Month
            tabtitle=self.tr("Expenses of {0} of {1}").format(self.mqtw.table.horizontalHeaderItem(self.month-1).text(), self.wyData.year)
            set.load_from_db("""select id_opercuentas, datetime, id_conceptos, id_tiposoperaciones, importe, comentario, id_cuentas , -1 as id_tarjetas 
                                                from opercuentas 
                                                where id_tiposoperaciones={0} and 
                                                           date_part('year',datetime)={1} and 
                                                           date_part('month',datetime)={2} 
                                                union all 
                                                select id_opercuentas, datetime, id_conceptos, id_tiposoperaciones, importe, comentario, id_cuentas ,tarjetas.id_tarjetas as id_tarjetas 
                                                from opertarjetas,tarjetas 
                                                where opertarjetas.id_tarjetas=tarjetas.id_tarjetas and 
                                                            id_tiposoperaciones={0} and 
                                                            date_part('year',datetime)={1} and 
                                                            date_part('month',datetime)={2}
                                                order by datetime""".format (id_tiposoperaciones, self.wyData.year, self.month))
        set.myqtablewidget(wdg,  True)
        wdg.drawOrderBy(0, False)
        horizontalLayout.addWidget(wdg)
        self.tab.addTab(newtab, tabtitle)
        self.tab.setCurrentWidget(newtab)

    @pyqtSlot() 
    def on_actionShowSellingOperations_triggered(self):
        def show_all():
            newtab = QWidget()
            horizontalLayout = QVBoxLayout(newtab)
            wdg = mqtwObjects(newtab)
            wdg.setSettings(self.mem.settings, "wdgTotal","tblShowShellingOperations")
            
            positive=Money(self.mem, 0, self.mem.localcurrency)
            negative=Money(self.mem, 0, self.mem.localcurrency)
            lbl=QLabel(newtab)
            
            set=InvestmentOperationHistoricalHeterogeneusManager(self.mem)
            for i in self.mem.data.investments.arr:
                for o in i.op_historica.arr:
                    if self.month==13:#Year
                        tabtitle=self.tr("Selling operations of {0}").format(self.wyData.year)
                        if o.fecha_venta.year==self.wyData.year:
                            set.arr.append(o)
                            if o.consolidado_bruto().isGETZero():
                                positive=positive+o.consolidado_bruto().local()
                            else:
                                negative=negative+o.consolidado_bruto().local()
                    else:#Month
                        tabtitle=self.tr("Selling operations of {0} of {1}").format(self.mqtw.table.horizontalHeaderItem(self.month-1).text(), self.wyData.year)
                        if o.fecha_venta.year==self.wyData.year and o.fecha_venta.month==self.month:#Venta y traspaso fondos inversion
                            set.arr.append(o)
                            if o.consolidado_bruto().isGETZero():
                                positive=positive+o.consolidado_bruto().local()
                            else:
                                negative=negative+o.consolidado_bruto().local()
            set.order_by_fechaventa()
            set.myqtablewidget(wdg)
            horizontalLayout.addWidget(wdg)
            lbl.setText(self.tr("Positive gross selling operations: {}. Negative gross selling operations: {}.").format(positive, negative))
            horizontalLayout.addWidget(lbl)
            self.tab.addTab(newtab, tabtitle)
            self.tab.setCurrentWidget(newtab)

        def show_more():
            newtab = QWidget()
            horizontalLayout = QVBoxLayout(newtab)
            wdg= mqtwObjects(newtab)
            wdg.table.setSelectionBehavior(QAbstractItemView.SelectItems)
            
            positive=Decimal(0)
            negative=Decimal(0)
            lbl=QLabel(newtab)
            
            set=InvestmentOperationHistoricalHeterogeneusManager(self.mem)
            for i in self.mem.data.investments.arr:
                for o in i.op_historica.arr:
                    if self.month==13:#Year
                        tabtitle=self.tr("Selling operations of {0}  (Sold after a year)").format(self.wyData.year)
                        if o.fecha_venta.year==self.wyData.year and o.tipooperacion.id in (5, 8)  and o.less_than_a_year()==False:#Venta y traspaso fondos inversion
                            set.arr.append(o)
                            if o.consolidado_bruto()>=0:
                                positive=positive+o.consolidado_bruto()
                            else:
                                negative=negative+o.consolidado_bruto()
                    else:#Month
                        tabtitle=self.tr("Selling operations of {0} of {1} (Sold after a year)").format(self.mqtw.table.horizontalHeaderItem(self.month-1).text(), self.wyData.year)
                        if o.fecha_venta.year==self.wyData.year and o.fecha_venta.month==self.month and o.tipooperacion.id in (5, 8)  and o.less_than_a_year()==False:#Venta y traspaso fondos inversion
                            set.arr.append(o)
                            if o.consolidado_bruto()>=0:
                                positive=positive+o.consolidado_bruto()
                            else:
                                negative=negative+o.consolidado_bruto()
            set.order_by_fechaventa()
            set.myqtablewidget(wdg, "wdgTotal")
            horizontalLayout.addWidget(wdg)
            lbl.setText(self.tr("Positive gross selling operations: {}. Negative gross selling operations: {}.").format(self.mem.localmoney(positive), self.mem.localmoney(negative)))
            horizontalLayout.addWidget(lbl)
            self.tab.addTab(newtab, tabtitle)
            self.tab.setCurrentWidget(newtab)
        def show_less():
            newtab = QWidget()
            horizontalLayout = QVBoxLayout(newtab)
            wdg = mqtwObjects(newtab)
            wdg.setSettings(self.mem.settings, "wdgTotal","tblShowSellingLessOperations")
            wdg.table.setSelectionBehavior(QAbstractItemView.SelectItems)
            
            positive=Decimal(0)
            negative=Decimal(0)
            lbl=QLabel(newtab)
            
            set=InvestmentOperationHistoricalHeterogeneusManager(self.mem)
            for i in self.mem.data.investments.arr:
                for o in i.op_historica.arr:
                    if self.month==13:#Year
                        tabtitle=self.tr("Selling operations of {0} (Sold before a year)").format(self.wyData.year)
                        if o.fecha_venta.year==self.wyData.year and o.tipooperacion.id in (5, 8) and o.less_than_a_year()==True:#Venta y traspaso fondos inversion
                            set.arr.append(o)
                            if o.consolidado_bruto()>=0:
                                positive=positive+o.consolidado_bruto()
                            else:
                                negative=negative+o.consolidado_bruto()
                    else:#Month
                        tabtitle=self.tr("Selling operations of {0} of {1} (Sold before a year)").format(self.mqtw.table.horizontalHeaderItem(self.month-1).text(), self.wyData.year)
                        if o.fecha_venta.year==self.wyData.year and o.fecha_venta.month==self.month and o.tipooperacion.id in (5, 8) and o.less_than_a_year()==True:#Venta y traspaso fondos inversion
                            set.arr.append(o)
                            if o.consolidado_bruto()>=0:
                                positive=positive+o.consolidado_bruto()
                            else:
                                negative=negative+o.consolidado_bruto()
            set.order_by_fechaventa()
            set.myqtablewidget(wdg)
            horizontalLayout.addWidget(wdg)
            lbl.setText(self.tr("Positive gross selling operations: {}. Negative gross selling operations: {}.").format(self.mem.localmoney(positive), self.mem.localmoney(negative)))
            horizontalLayout.addWidget(lbl)
            self.tab.addTab(newtab, tabtitle)
            self.tab.setCurrentWidget(newtab)            
        ##################################
        if self.mem.gainsyear==True:
            show_less()
            show_more()
        else:
            show_all()

    @pyqtSlot() 
    def on_actionShowDividends_triggered(self):
        newtab = QWidget()
        horizontalLayout = QHBoxLayout(newtab)
        wdg = mqtwObjects(newtab)
        wdg.setSettings(self.mem.settings,"wdgTotal","mqtwShowDividends")
        wdg.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        
        set=DividendHeterogeneusManager(self.mem)
        for inv in self.mem.data.investments.arr:
            for dividend in inv.dividends.arr:
                if self.month==13:
                    tabtitle=self.tr("Dividends of {0}").format(self.wyData.year)
                    if dividend.datetime.year==self.wyData.year:
                        set.append(dividend)
                else:# With mounth
                    tabtitle=self.tr("Dividends of {0} of {1}").format(self.mqtw.table.horizontalHeaderItem(self.month-1).text(), self.wyData.year)
                    if dividend.datetime.year==self.wyData.year and dividend.datetime.month==self.month:
                        set.append(dividend)
        set.order_by_datetime()
        set.myqtablewidget(wdg,  True)
        horizontalLayout.addWidget(wdg)
        self.tab.addTab(newtab, tabtitle)
        self.tab.setCurrentWidget(newtab)            

    @pyqtSlot() 
    def on_actionShowComissions_triggered(self):
        newtab = QWidget()
        vlayout = QVBoxLayout(newtab)
        wdg = mqtwObjects(newtab)
        wdg.setSettings(self.mem.settings,"wdgTotal","mqtwShowComissions")
        wdg.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        wdg.table.verticalHeader().show()
        
        wdg.table.setColumnCount(13)
        wdg.table.setHorizontalHeaderItem(0, QTableWidgetItem(self.tr( "January" )))
        wdg.table.setHorizontalHeaderItem(1, QTableWidgetItem(self.tr( "February" )))
        wdg.table.setHorizontalHeaderItem(2, QTableWidgetItem(self.tr( "March" )))
        wdg.table.setHorizontalHeaderItem(3, QTableWidgetItem(self.tr( "April" )))
        wdg.table.setHorizontalHeaderItem(4, QTableWidgetItem(self.tr( "May" )))
        wdg.table.setHorizontalHeaderItem(5, QTableWidgetItem(self.tr( "June" )))
        wdg.table.setHorizontalHeaderItem(6, QTableWidgetItem(self.tr( "July" )))
        wdg.table.setHorizontalHeaderItem(7, QTableWidgetItem(self.tr( "August" )))
        wdg.table.setHorizontalHeaderItem(8, QTableWidgetItem(self.tr( "September" )))
        wdg.table.setHorizontalHeaderItem(9, QTableWidgetItem(self.tr( "October" )))
        wdg.table.setHorizontalHeaderItem(10, QTableWidgetItem(self.tr( "November" )))
        wdg.table.setHorizontalHeaderItem(11, QTableWidgetItem(self.tr( "December" )))
        wdg.table.setHorizontalHeaderItem(12, QTableWidgetItem(self.tr( "Total" )))
        
        wdg.table.setRowCount(4)
        wdg.table.setVerticalHeaderItem(0, QTableWidgetItem(self.tr( "Bank commissions" )))
        wdg.table.setVerticalHeaderItem(1, QTableWidgetItem(self.tr( "Custody fees" )))
        wdg.table.setVerticalHeaderItem(2, QTableWidgetItem(self.tr( "Invesment operation commissions" )))
        wdg.table.setVerticalHeaderItem(3, QTableWidgetItem(self.tr( "Total" )))
        wdg.applySettings()
        (sum_bank_commissions, sum_custody_fees, sum_investment_commissions)=(Decimal("0"), Decimal("0"), Decimal("0"))

        for column in range (12):
            bank_commissions=none2decimal0(self.mem.con.cursor_one_row("""select sum(importe) 
                                                                                                            from opercuentas 
                                                                                                            where id_conceptos=%s and 
                                                                                                                date_part('year',datetime)=%s and 
                                                                                                                date_part('month',datetime)=%s;""", (38, self.wyData.year, column+1))[0])
            wdg.table.setItem(0, column, self.mem.localmoney(bank_commissions).qtablewidgetitem())
            sum_bank_commissions=sum_bank_commissions+bank_commissions
            
            custody_fees=none2decimal0(self.mem.con.cursor_one_row("""select sum(importe) 
                                                                                                            from opercuentas 
                                                                                                            where id_conceptos=%s and 
                                                                                                                date_part('year',datetime)=%s and 
                                                                                                                date_part('month',datetime)=%s;""", (59, self.wyData.year, column+1))[0])
            wdg.table.setItem(1, column, self.mem.localmoney(custody_fees).qtablewidgetitem())
            sum_custody_fees=sum_custody_fees+custody_fees
            
            investment_commissions=-none2decimal0(self.mem.con.cursor_one_row("""select sum(comision) 
                                                                                                            from operinversiones  
                                                                                                            where date_part('year',datetime)=%s and 
                                                                                                                date_part('month',datetime)=%s;""", (self.wyData.year, column+1))[0])
            wdg.table.setItem(2, column, self.mem.localmoney(investment_commissions).qtablewidgetitem())
            sum_investment_commissions=sum_investment_commissions+investment_commissions
            
            wdg.table.setItem(3, column, self.mem.localmoney(bank_commissions+custody_fees+investment_commissions).qtablewidgetitem())    
        wdg.table.setItem(0, 12, self.mem.localmoney(sum_bank_commissions).qtablewidgetitem()) 
        wdg.table.setItem(1, 12, self.mem.localmoney(sum_custody_fees).qtablewidgetitem())    
        wdg.table.setItem(2, 12, self.mem.localmoney(sum_investment_commissions).qtablewidgetitem())
        wdg.table.setItem(3, 12, self.mem.localmoney(sum_bank_commissions+sum_custody_fees+sum_investment_commissions).qtablewidgetitem())
        vlayout.addWidget(wdg)

        #Number of operations
        num_operations=0
        settypes=self.mem.types.with_operation_commissions_types()
        for i, type in enumerate(settypes.arr):
            for inv in self.mem.data.investments.arr:
                if inv.product.type.id==type.id:
                    for o in inv.op.arr:
                        if o.datetime.year==self.wyData.year and o.tipooperacion.id in (4, 5):#Purchase and sale
                            num_operations=num_operations+1            
        if num_operations>0:
            label=QLabel(newtab)
            font = QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setWeight(75)
            label.setFont(font)
            label.setAlignment(Qt.AlignCenter)
            cs=self.mem.localmoney
            label.setText(self.tr("Number of purchase and sale investment operations: {}. Commissions average: {}".format(int(num_operations), cs(sum_investment_commissions/num_operations))))
            vlayout.addWidget(label)
            
        self.tab.addTab(newtab, self.tr("Commision report of {}").format(self.wyData.year))
        self.tab.setCurrentWidget(newtab)        
        

    @pyqtSlot() 
    def on_actionGainsByProductType_triggered(self):
        newtab = QWidget()
        vlayout = QVBoxLayout(newtab)
        wdg = mqtwObjects(newtab)
        wdg.setSettings(self.mem.settings,"wdgTotal","mqtwGainsByProductType")
        wdg.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        wdg.table.setColumnCount(5)
        
        wdg.table.setHorizontalHeaderItem(0, QTableWidgetItem(self.tr( "Product type" )))
        wdg.table.setHorizontalHeaderItem(1, QTableWidgetItem(self.tr( "Gross gains" )))
        wdg.table.setHorizontalHeaderItem(2, QTableWidgetItem(self.tr("Gross dividends")))
        wdg.table.setHorizontalHeaderItem(3, QTableWidgetItem(self.tr( "Net gains" )))
        wdg.table.setHorizontalHeaderItem(4, QTableWidgetItem(self.tr("Net dividends")))
        wdg.applySettings()
        sum_gains=Money(self.mem)
        sum_dividens=Money(self.mem)
        sum_netgains=Money(self.mem)
        sum_netdividends=Money(self.mem)
        
        settypes=self.mem.types.investment_types()
        wdg.table.setRowCount(settypes.length()+1)
        
        for i, type in enumerate(settypes.arr):
            wdg.table.setItem(i, 0, qleft(type.name))    
            gains=Money(self.mem,  0,  self.mem.localcurrency)
            netgains=Money(self.mem, 0, self.mem.localcurrency)
            dividends=Money(self.mem,  0,  self.mem.localcurrency)
            netdividens=Money(self.mem,  0, self.mem.localcurrency)
            for inv in self.mem.data.investments.arr:
                if inv.product.type.id==type.id:
                    #gains
                    for o in inv.op_historica.arr:
                        if o.fecha_venta.year==self.wyData.year:
                            gains=gains+o.consolidado_bruto(eMoneyCurrency.User)
                            netgains=netgains+o.consolidado_neto(eMoneyCurrency.User)
                    #dividends
                    inv.needStatus(3)
                    for d in inv.dividends.arr:
                        if d.datetime.year==self.wyData.year:
                            dividends=dividends+d.gross(eMoneyCurrency.User)
                            netdividens=netdividens+d.net(eMoneyCurrency.User)
            wdg.table.setItem(i, 1, gains.qtablewidgetitem())
            wdg.table.setItem(i, 2, dividends.qtablewidgetitem())
            wdg.table.setItem(i, 3, netgains.qtablewidgetitem())
            wdg.table.setItem(i, 4, netdividens.qtablewidgetitem())
            sum_gains=sum_gains+gains
            sum_netgains=sum_netgains+netgains
            sum_dividens=sum_dividens+dividends
            sum_netdividends=sum_netdividends+netdividens
            
        wdg.table.setItem(i+1, 0, qleft(self.tr("Total")))
        wdg.table.setItem(i+1, 1, sum_gains.qtablewidgetitem())
        wdg.table.setItem(i+1, 2, sum_dividens.qtablewidgetitem())
        wdg.table.setItem(i+1, 3, sum_netgains.qtablewidgetitem())
        wdg.table.setItem(i+1, 4, sum_netdividends.qtablewidgetitem())
        
        label=QLabel(newtab)
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        label.setText(self.tr("Gross gains + Gross dividends: {} + {} = {}\nNet gains + Net dividens: {} + {} = {}".format(sum_gains, sum_dividens, sum_gains+sum_dividens, sum_netgains, sum_netdividends, sum_netgains+sum_netdividends)))
            
        vlayout.addWidget(wdg)
        vlayout.addWidget(label)
        self.tab.addTab(newtab, self.tr("Gains by product type of {}").format(self.wyData.year))
        self.tab.setCurrentWidget(newtab)        
            
    @pyqtSlot() 
    def on_actionShowTaxes_triggered(self):
        newtab = QWidget()
        horizontalLayout = QVBoxLayout(newtab)
        wdg = mqtwObjects(newtab)
        wdg.setSettings(self.mem.settings,"wdgTotal","myqtwShowPaidTaxes")
        wdg.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        wdg.table.verticalHeader().show()        
        
        wdg.table.setColumnCount(13)
        wdg.table.setHorizontalHeaderItem(0, QTableWidgetItem(self.tr( "January" )))
        wdg.table.setHorizontalHeaderItem(1, QTableWidgetItem(self.tr( "February" )))
        wdg.table.setHorizontalHeaderItem(2, QTableWidgetItem(self.tr( "March" )))
        wdg.table.setHorizontalHeaderItem(3, QTableWidgetItem(self.tr( "April" )))
        wdg.table.setHorizontalHeaderItem(4, QTableWidgetItem(self.tr( "May" )))
        wdg.table.setHorizontalHeaderItem(5, QTableWidgetItem(self.tr( "June" )))
        wdg.table.setHorizontalHeaderItem(6, QTableWidgetItem(self.tr( "July" )))
        wdg.table.setHorizontalHeaderItem(7, QTableWidgetItem(self.tr( "August" )))
        wdg.table.setHorizontalHeaderItem(8, QTableWidgetItem(self.tr( "September" )))
        wdg.table.setHorizontalHeaderItem(9, QTableWidgetItem(self.tr( "October" )))
        wdg.table.setHorizontalHeaderItem(10, QTableWidgetItem(self.tr( "November" )))
        wdg.table.setHorizontalHeaderItem(11, QTableWidgetItem(self.tr( "December" )))
        wdg.table.setHorizontalHeaderItem(12, QTableWidgetItem(self.tr( "Total" )))
        
        wdg.table.setRowCount(5)
        wdg.table.setVerticalHeaderItem(0, QTableWidgetItem(self.tr( "Investment operation retentions" )))
        wdg.table.setVerticalHeaderItem(1, QTableWidgetItem(self.tr( "Dividend retentions" )))
        wdg.table.setVerticalHeaderItem(2, QTableWidgetItem(self.tr( "Other paid taxes" )))
        wdg.table.setVerticalHeaderItem(3, QTableWidgetItem(self.tr( "Returned taxes" )))
        wdg.table.setVerticalHeaderItem(4,  QTableWidgetItem(self.tr( "Total" )))

        wdg.applySettings()
        (sum_io_retentions, sum_div_retentions, sum_other_taxes,  sum_returned_taxes)=(Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0"))

        for column in range (12):
            io_retentions=-none2decimal0(self.mem.con.cursor_one_row("""select sum(impuestos) 
                                                                                                                                from operinversiones  
                                                                                                                                where date_part('year',datetime)=%s and 
                                                                                                                                    date_part('month',datetime)=%s;""", (self.wyData.year, column+1))[0])
            wdg.table.setItem(0, column, self.mem.localmoney(io_retentions).qtablewidgetitem())
            sum_io_retentions=sum_io_retentions+io_retentions
            
            div_retentions=-none2decimal0(self.mem.con.cursor_one_row("""select sum(retencion) 
                                                                                                            from dividends 
                                                                                                            where date_part('year',fecha)=%s and 
                                                                                                                date_part('month',fecha)=%s;""", (self.wyData.year, column+1))[0])
            wdg.table.setItem(1, column, self.mem.localmoney(div_retentions).qtablewidgetitem())
            sum_div_retentions=sum_div_retentions+div_retentions
            
            other_taxes=none2decimal0(self.mem.con.cursor_one_row("""select sum(importe) 
                                                                                                            from opercuentas 
                                                                                                            where id_conceptos=%s and 
                                                                                                                date_part('year',datetime)=%s and 
                                                                                                                date_part('month',datetime)=%s;""", (37, self.wyData.year, column+1))[0])
            wdg.table.setItem(2, column, self.mem.localmoney(other_taxes).qtablewidgetitem())
            sum_other_taxes=sum_other_taxes+other_taxes         
            
            returned_taxes=none2decimal0(self.mem.con.cursor_one_row("""select sum(importe) 
                                                                                                            from opercuentas 
                                                                                                            where id_conceptos=%s and 
                                                                                                                date_part('year',datetime)=%s and 
                                                                                                                date_part('month',datetime)=%s;""", (6, self.wyData.year, column+1))[0])
            wdg.table.setItem(3, column, self.mem.localmoney(returned_taxes).qtablewidgetitem())
            sum_returned_taxes=sum_returned_taxes+returned_taxes
            
            wdg.table.setItem(4, column, self.mem.localmoney(io_retentions+div_retentions+other_taxes+returned_taxes))    
        
        wdg.table.setItem(0, 12, self.mem.localmoney(sum_io_retentions).qtablewidgetitem())
        wdg.table.setItem(1, 12, self.mem.localmoney(sum_div_retentions).qtablewidgetitem())
        wdg.table.setItem(2, 12, self.mem.localmoney(sum_other_taxes).qtablewidgetitem())
        wdg.table.setItem(3, 12, self.mem.localmoney(sum_returned_taxes).qtablewidgetitem())
        wdg.table.setItem(4, 12, self.mem.localmoney(sum_io_retentions+sum_div_retentions+sum_other_taxes+sum_returned_taxes).qtablewidgetitem())

        horizontalLayout.addWidget(wdg)
        self.tab.addTab(newtab, self.tr("Taxes report of {}").format(self.wyData.year))
        self.tab.setCurrentWidget(newtab)        
            

    def on_tab_tabCloseRequested(self, index):
        """Only removes dinamic tabs"""
        if index in (0, 1):
            qmessagebox(self.tr("You can't close this tab"))
        else:
            self.tab.setCurrentIndex(0)
            self.tab.removeTab(index)
            
    def on_mqtw_cellDoubleClicked(self, row, column):
        if row==0:#incomes
            self.on_actionShowIncomes_triggered()
        elif row==1:#Gains
            self.on_actionShowSellingOperations_triggered()
        elif row==2:#Dividends
            self.on_actionShowDividends_triggered()
        elif row==3: #Expenses
            self.on_actionShowExpenses_triggered()
        elif row==7: #Investments
            totalmonth=self.setData.arr[column]
            qmessagebox(self.tr("High Low Investments aren't sumarized here, due to they have daily adjustments in accounts.") + "\n\n" + self.tr("Their balance at the end of {}-{} is {}").format(totalmonth.year, totalmonth.month, totalmonth.total_investments_high_low()))
        else:
            qmessagebox(self.tr("You only can double click in incomes, gains, dividends and expenses.") + "\n\n" + self.tr("Make right click to see commission and tax reports"))

    def on_mqtw_customContextMenuRequested(self,  pos):
        menu=QMenu()
        menu.addAction(self.actionShowComissions)
        menu.addSeparator()
        menu.addAction(self.actionShowTaxes)
        menu.addSeparator()
        menu.addAction(self.actionGainsByProductType)
        menu.exec_(self.mqtw.table.mapToGlobal(pos))

    @pyqtSlot()
    def on_mqtw_itemSelectionChanged(self):
        debug("NOW")
        self.month=None
        for i in self.mqtw.table.selectedItems():#itera por cada item no row.
            self.month=i.column()+1
        debug("Selected month: {0}.".format(self.month))
