def knap_sack (weight_arr , value_arr , weight_bag , num):
    
    K = [[0 for x in range(weight_bag + 1)] for x in range(num + 1)] 

    if (num==0 or weight_bag==0):
        return 0

    for i in range(num + 1): 
        for w in range(weight_bag+ 1):
            if(K[i][w]!=0):
                print(K[i][w])
                return K[i][w]

    else:
        
        if (weight_arr[num-1]<=weight_bag):
            
            K[i][w]= max(value_arr[num-1]+knap_sack(weight_arr , value_arr , weight_bag-weight_arr[num-1] , num-1),
            knap_sack(weight_arr , value_arr , weight_bag , num-1))
            return K[i][w]

        
        elif(weight_arr[num-1]>weight_bag):

            K[i][w]=knap_sack(weight_arr , value_arr , weight_bag , num-1)
            return K[i][w]
     
   

weight_arr=[20,30,15,25,36]
value_arr=[25,15,50,54,60]
weight_bag=300
num=len(weight_arr)

max_profit=knap_sack(weight_arr , value_arr , weight_bag , num)
print(max_profit)
 