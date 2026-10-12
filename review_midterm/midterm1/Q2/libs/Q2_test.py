from review_midterm.midterm1.Q2.libs.Q2 import calc_order

num_sp=10
num_dl=5
dl, sp, total=calc_order(num_dl,num_sp)
print(f"Total revenue of Dalat flowers: {dl}")
print(f"Total revenue of Sapa flowers: {sp}")
print(f"Total revenue: {total}")
