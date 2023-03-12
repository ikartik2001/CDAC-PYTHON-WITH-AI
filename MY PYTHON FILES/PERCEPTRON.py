class Neuron():              # creted a class Neuron
    input_size=3              # defined its input size
    n1_input_list=[]           # creted empty list to hold inputs
    n1_weight_list=[]

    def takeinput(self):       # crated behaviour to take inputs from user
         
     for i in range(n1.input_size):
       x=int(input("enter your inputs"))
       self.n1_input_list.append(x)
     print(self.n1_input_list)
     
     
     def takeweight(self):       # crated behaviour to take inputs from user
          
      for i in range(n1.input_size):
        y=int(input("enter your inputs"))
        self.n1_weight_list.append(y)
      print(self.n1_weight_list)
    




n1=Neuron()                  # created first neuron in class neuron


n1.takeinput()

 

    


    

    