# #1
# class Search:
#     def Binary_Search(self,k,arr,n):
#         start=0
#         end=len(arr)
#         while start <= end:
#             mid = (start + end) // 2

#             if arr[mid] == n:
#                 return mid+1
#             elif arr[mid] < n:
#                 start = mid + 1
#             else:
#                 end = mid -1
#         return None

# if __name__=='__main__':
#     arr=list(map(int, input().split()))
#     n=int(input())

#     k=len(arr)//2
#     search=Search()
#     print(search.Binary_Search(k,arr,n))
    
#2
# class Sort:
#     def Quick_Sort(self,arr):
#         if len(arr)<=1:
#             return arr

#         pivot=arr[0]
#         high=[ i for i in arr[1:] if i>pivot]
#         low =[ i for i in arr[1:] if i<pivot]
#         return self.Quick_Sort(low)+[pivot]+self.Quick_Sort(high)

# if __name__=='__main__':
#     arr=list(map(int, input().split()))
#     sort=Sort()
#     print(sort.Quick_Sort(arr))

#3
# class Sort:
#     def Merge(self,left,right):
#         result=[]
#         l,r=0,0
#         while l<len(left) and r<len(right):
#             if left[l]<right[r]:
#                 result.append(left[l])
#                 l+=1
#             else:
#                 result.append(right[r])
#                 r+=1
#         if l<len(left):
#             result+=left[l:]
#         elif r<len(right):
#             result+=right[r:]

#         return result

#     def divide(self,arr):
#         if len(arr)<=1:
#             return arr
        
#         left= self.divide(arr[ : len(arr)//2])
#         right=self.divide(arr[len(arr)//2 : ])
#         return self.Merge(left,right)

    
# if __name__=='__main__':
#     arr=list(map(int, input().split()))
#     sort=Sort()
#     print(sort.divide(arr))

#4
# class binary_tree:
#     def inorder(self, x,arr):
#         if 2*x<len(arr):
#             self.inorder(2*x,arr)
#         print(arr[x])
#         if 2*x+1<len(arr):
#             self.inorder(2*x+1,arr)

#     def preorder(self, x,arr):
#         print(arr[x])
#         if 2*x<len(arr):
#             self.preorder(2*x,arr)
#         if 2*x+1<len(arr):
#             self.preorder(2*x+1,arr)
#     def postorder(self,x,arr):
#         if 2*x<len(arr):
#             self.postorder(2*x,arr)
#         if 2*x+1<len(arr):
#             self.postorder(2*x+1,arr)
#         print(arr[x])
# if __name__=='__main__':
#     arr=[0,15,1,37,61,26,59,48]
#     visit=binary_tree()
#     print('Preorder Traverse')
#     visit.preorder(1,arr)
#     print('Inorder Traverse')
#     visit.inorder(1,arr)
#     print('Postorder Traverse')
#     visit.postorder(1,arr)

#5

# class lect:
#     def Lect(self):
#         n=int(input())
#         arr=[0]*n
#         for i in range(n):
#             num,start,end=list(map(int,input().split()))
#             arr[num-1]=(num,start,end)
#         arr=sorted(arr, key = lambda x : x[2])

#         result=[arr[0]]
#         ans=[arr[0][0]]
#         for i in range(1,n):
#             if arr[i][1]>=result[-1][2]: 
#                 result.append(arr[i])
#                 ans.append(arr[i][0])
#         print(len(result))
#         print(ans)

# if __name__=='__main__':
#     a=lect()
#     a.Lect()
    
#6
class pattern:
    def __init__(self):
        self.n=int(input())
        self.arr=[]

    def pattern(self):
        for _ in range(self.n):
            self.arr=input()
            
            if '100'==self.arr[0:3]:
                if '1' in self.arr[3:]:
                    print('DANGER')
                else:
                    print('PASS')
            elif '01'==self.arr[0:2]:
                print('DANGER')
            
            else:
                print('PASS')


if __name__=='__main__':
    Pattern=pattern()
    Pattern.pattern()