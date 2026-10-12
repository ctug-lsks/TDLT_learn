price_dl = 85000
price_sp = 100000
num_sold_dl = 0
num_sold_sp = 0
revenue_dl = 0
revenue_sp = 0
total_revenue = 0
def calc_order(num_dl, num_sp):
    global revenue_dl, revenue_sp, total_revenue, num_sold_dl, num_sold_sp,price_dl,price_sp
    revenue_dl=num_dl*price_dl
    revenue_sp=num_sp*price_sp
    total_revenue=revenue_dl+revenue_sp
    num_sold_dl+=num_dl
    num_sold_sp+=num_sp
    revenue_dl+=revenue_dl
    revenue_sp+=revenue_sp
    total_revenue+=total_revenue
    return num_sold_dl, num_sold_sp, revenue_dl,revenue_sp, total_revenue

def reset_order():
    global revenue_dl, revenue_sp, total_revenue, num_sold_dl, num_sold_sp
    revenue_dl = 0
    revenue_sp = 0
    total_revenue = 0
    num_sold_dl = 0
    num_sold_sp = 0