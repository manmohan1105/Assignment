import collections 
parent=collections.defaultdict(list)
fees=collections.defaultdict(int)
weight=collections.defaultdict(int)
transc=[]
with open('mempool.csv') as f:
        
        cnt=0
        for line in f:
           cnt+=1
           if cnt==1:
               continue
           l=line.strip().split(",")
       
           l2=str(l[3]).split(";")
           transc.append([l[0],int(l[1])])
           parent[l[0]]+=l2
           fees[l[0]]=int(l[1])
           weight[l[0]]=int(l[2])
        f.close()
        transc.sort(key=lambda x:-x[1])
        
        visited=set()
        ans=[]
        def helper(parentt,visited,stack):
            if parentt==['']:
                return
            visited.add(parentt)
            
            for parentofparent in parent[parentt]:
                if parentofparent not in visited:
                    helper(parentofparent,visited,stack)
            stack.append(parentt) 
            return       
        tweight=0
        ans=[]
        f=0
        for tranid,fees in transc:
            if tranid not in visited:
                
                    stack=[]
                    helper(tranid,visited,stack)
                    
                    for tid in stack:
                        tweight+=weight[tid]
                        if tweight >4000000:
                           
                            f=1
                            break
                   
                    ans+=stack    
                    if f==1:
                        i=ans.index(tranid)
                        for j in range(i+1,len(ans)):
                           visited.remove(ans[j])
                        ans=ans[:i]
        
        with open('block.txt', 'w') as f:
         for line in ans:
           f.write(line)
           f.write('\n')  
         f.close()  

                     




        

                    



        


             
