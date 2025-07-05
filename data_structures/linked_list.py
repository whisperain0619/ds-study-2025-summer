class Node:
    """
    연결 리스트의 각 요소를 나타내는 노드.
    하나의 데이터 값과 다음 노드를 가리키는 포인터(next)를 가집니다.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    노드들로 이루어진 연결 리스트.
    리스트의 시작점(head)을 가리키는 포인터를 가집니다.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        리스트의 맨 끝에 새로운 노드를 추가합니다.
        """
        # TODO: 이 부분을 직접 구현해보세요.
        # 1. 새로운 노드를 만듭니다.
        # 2. 리스트가 비어있다면(head가 None이라면), head를 새 노드로 지정합니다.
        # 3. 리스트가 비어있지 않다면, 맨 마지막 노드를 찾아서 그 노드의 next를 새 노드로 지정합니다.
        pass

    def print_all(self):
        """
        리스트의 모든 노드 데이터를 출력합니다.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# --- 테스트 코드 ---
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.print_all()  # 예상 출력: 10 -> 20 -> 30 -> None
