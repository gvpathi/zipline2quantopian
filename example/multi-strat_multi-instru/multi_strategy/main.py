from necessary_import import *; from context import *; from strat1.strat1_core import *; from strat2.strat2_core import *; 

def handle_data(context, data):
    
    context.portf.order_management.update()
    
    # visually check for accidental "borrowing of cash
    check_cash_status(context) 
    record(leverage=context.account.leverage)

    context.performance_analysis.update_ds(data.items()[0][1]['dt'].date(), context.portfolio.portfolio_value)
    return
              
   
def initialize(context):
    
    context.portf = PortfolioManager(context)
    allocation = 0.9/2    
    
    s1 = strat1(context)
    context.portf.add_strategy(s1, allocation=allocation)
    
    s2 = strat2(context)
    context.portf.add_strategy(s2, allocation=allocation)
           
    context.global_fund_managed = context.portf.get_portf_allocation()                                             
    context.instrument = context.portf.get_instruments()  
        
    # store portfolio_value when fast_backtest is activated    
    context.performance_analysis = []
        
    context.cagr_period = 0
    context.env = get_environment('platform')
    set_init_common (context)

    return