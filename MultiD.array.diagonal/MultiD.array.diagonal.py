#!/usr/bin/python3

#MultiD.array.diagonal.py
#Multi dimensional Array 
#Add diagonal numbers 

ar2 = [[1,2,3],[4,5,6],[7,8,9]]

class Hello():
    def diagonal_sum(self,ar2):
        
        sum = 0
        for i in range(len(ar2)): #i = 0 to 3
            for j in range(len(ar2[i])):  # j = 0 to 3 
                if i == j:
                    sum += ar2[i][j]
                else:
                    continue
        print (sum)


#Another option or program
    def diagonal2(self,ar3):
        for i in range(len(ar2)):
            sum += ar3[i][i]
        print (sum)



def main():
    c = Hello()
    c.diagonal_sum(ar2)
    c.diagonal_sum(ar2)



if __name__ == "__main__":

    main()
