
'''
트리란? 나무 구조를 거꾸로 뒤집어놓은 형태
최상단 = root node
최하단 = leaf node
link = edge

binary tree(이진트리)
: 최대 두개의 노드로 구성, 
    complete binary tree(완전 이진트리)나 full binary tree(포화 이진트리)는 sub tree 두개로 나눌 수 있음
    ㄴ[?] 일반 이진 트리는 나눌수도, 못 나눌 수도 있음?
    1) root 왼쪽의 sub tree, 오른쪽 sub tree

    한편으로만 링크되는 skewed binary tree(편향 이진 트리)도 있음
    ㄴ[?] 쓰는 이유가 뭐임?

    높이 계산할때는 root빼고 다른 층 개수만 계산


'''
# --------------------------------------------------------------------------------
import random as rd


#전역변수
Ary = [i for i in range(10)]#데이터 array 생성

class TreeNode():
    def __init__(self, data, root = False):
        self.root = root #root node 일땐 True
        self.data = data
        self.llink = None
        self.rlink = None
# ---------------------------------------------------------------------------------

'''
일반 binary tree 만들기
'''
#for문 안에서 계산되는 값들을 각 변수에 담을때 사용
#전역변수 선언은 globals()['변수명'+str(i)]
#지역변수 선언은 locals()['변수명'+str(i)]
for i in range(len(Ary)):
    if i == 0:
        globals()['Node'+str(i)] =  TreeNode(Ary[i], True)
    else:
        globals()['Node'+str(i)] =  TreeNode(Ary[i])
    
num = 0
for i in range(len(Ary)):
    current = globals()['Node'+str(i)]
    print('Node'+str(i), )
    if i < len(Ary)-3:
        current.llink = globals()['Node'+str(num*2+1)]
        current.rlink = globals()['Node'+str(num*2+2)]
    num += 1

# ---------------------------------------------------------------------------------
'''
일반 binary tree구조
'''
print(Ary)

Node0.root #true

for i in range(len(Ary)):
    if (globals()['Node'+str(i)].data*2 + 1) > len(Ary):
        break
    if globals()['Node'+str(i)].data != None:
        print('Node'+str(i)+':', globals()['Node'+str(i)].data)
        if (globals()['Node'+str(i)].llink != None):   
            print('llink', globals()['Node'+str(i)].llink.data, end=',')
        if (globals()['Node'+str(i)].rlink != None):
            print('rlink', globals()['Node'+str(i)].rlink.data)
            print()
# ---------------------------------------------------------------------------------
# 전위순회 (루트 > 왼쪽 서브트리 > 오른쪽 서브트리)
# 재귀함수
def preorder(node):
    if node == None:
        return
    print(node.data, end= '->')
    preorder(node.llink)
    preorder(node.rlink)

preorder(Node0)
print('end')
# ---------------------------------------------------------------------------------
# 중위순회 (왼쪽 서브트리 > 루트 > 오른쪽 서브트리)
def inorder(node):
    if node == None:
        return
    inorder(node.llink)
    print(node.data, end= '->')
    inorder(node.rlink)

inorder(Node0)
print('end')
# ---------------------------------------------------------------------------------
# 후위순회 (왼쪽 서브트리 > 오른쪽 서브트리 > 루트)
def postorder(node):
    if node == None:
        return
    postorder(node.llink)
    postorder(node.rlink)
    print(node.data, end= '->')

postorder(Node0)
print('end')