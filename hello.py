def total_calc(billamount,tip):
    total=billamount*(1+0.01*tip)
    total=round(total,2)
    print(f"please pay ${total}")
total_calc(150,20)