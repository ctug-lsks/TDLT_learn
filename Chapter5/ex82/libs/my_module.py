def calc_bill(type,old_num,new_num):
    sodien=new_num-old_num
    if type==1:
        result=sodien * 2.271
    else:
        if sodien<=50:
            result = sodien * 1.549
        elif 51<=sodien<=100:
            result = (50 * 1.549) + (sodien - 50) * 1.6
        elif 101<=sodien<=200:
            result = (50 * 1.549) + (50 * 1.6) + (sodien - 100) * 1.858
        elif 201<=sodien<=300:
            result = (50 * 1.549) + (50 * 1.6) + (100 * 1.858) + (sodien - 200) * 2.340
        elif 301<=sodien<=400:
            result = (50 * 1.549) + (50 * 1.6) + (100 * 1.858) + (100 * 2.340) + (sodien - 300) * 2.615
        else:
            result = (50 * 1.549) + (50 * 1.6) + (100 * 1.858) + (100 * 2.340) + (100 * 2.615) + (sodien - 400) * 2.701
    return result