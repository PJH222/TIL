## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre
    # Case 1 : 하필... 찾는 애가 Head인 경우
    if findData == head.data :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # case 2 : 찾는 애가 중간에 있는 경우
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    # case 3 : 없는 노드 앞에 삽입
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData):
    global memory, head, current, pre
    # case 1 : 머리를 삭제하기
    if deleteData == head.data :
        current = head
        head = head.link
        del(current)
        return
    # case 2 : 중간을 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del current
            return
    # case 3 : 없는 노드 삭제하기
    return

def findNode(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current

    while current.link != None:
        current = current.link
        if current.data == findData:
            return current

    return Node()


## 변수
memory = []
head , current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효']

## 메인
#* 연결 리스트 생성

node=Node()
node.data = dataArray[0]
head = node
memory.append(node) # 안 중요함 (생략 가능)


for data in dataArray[1:] :
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)
# insertNode('다현','화사')
# insertNode('사나','솔라')

#* 데이터 삽입
# insertNode('재남','문별')
# printNodes(head)

# deleteNode('다현') # 삭제할 데이터
# deleteNode('쯔위')
# deleteNode('재남')
# printNodes(head)
# print(current)


retNode = findNode('사나')
print(retNode.data, '뮤비가 나옵니다. 쿵짝쿵짝~~~')