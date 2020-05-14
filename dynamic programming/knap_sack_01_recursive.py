def knap_sack (weight_arr , value_arr , weight_bag , num):
    if (num==0 or weight_bag==0):
        return 0
    else:
        
        if (weight_arr[num-1]<=weight_bag):
            
            return max(value_arr[num-1]+knap_sack(weight_arr , value_arr , weight_bag-weight_arr[num-1] , num-1),
            knap_sack(weight_arr , value_arr , weight_bag , num-1))
        
        elif(weight_arr[num-1]>weight_bag):

            return knap_sack(weight_arr , value_arr , weight_bag , num-1)

weight_arr=[20,30,15,25,36]
value_arr=[25,15,50,54,60]
weight_bag=300
num=len(weight_arr)

max_profit=knap_sack(weight_arr , value_arr , weight_bag , num)
print(max_profit)
 